"""
Модуль, выполняющий основную работу по экстракции и преобразованию данных из API GooglePlay
"""
import re
import json
import types
from typing import List, Dict, Optional

from aiohttp import ClientSession

from pictures import save_picture
from custom_types import BlockType, PermissionsType

MAGIC_APP_STRING = r'[[["xdSrCf","[[null,[\"{0}\",7],[]]]",null,"vm96le:0|ww"]]]'

PERMISSION_URL = 'https://play.google.com/_/PlayStoreUi/data/batchexecute'

DEFAULT_REQUEST_PARAMS = types.MappingProxyType({
    'f.sid': '7185783150060508621',
    'bl': 'boq_playuiserver_20180827.08_p0',
    'authuser': '',
    'soc-app': '121',
    'soc-platform': '1',
    'soc-device': '1',
    '_reqid': '202915',
    'rt': 'c',
})


async def get_permissions(app_id: str, language: str) -> Optional[Dict[str, BlockType]]:
    """
    Возвращает словарь блоков разрешений по идентификатору приложения и языку
    """
    raw_response = await request_app_data(app_id, language)
    permission_data = extract_permission_data(raw_response)

    if not permission_data:
        return None

    return await extract_permission_blocks(permission_data, language)


async def request_app_data(app_id: str, language: str) -> str:
    """
    Возвращает запрошенные данные о приложении через внутреннее API GooglePlay Store
    """
    app_id_data = {
        'f.req': MAGIC_APP_STRING.format(app_id),
        '': '',
    }
    search_params = {
        **DEFAULT_REQUEST_PARAMS,
        'hl': language,
    }

    async with ClientSession() as session:
        async with session.post(
            url=PERMISSION_URL,
            params=search_params,
            data=app_id_data,
        ) as resp:
            return await resp.text()


def extract_permission_data(raw_response: str) -> Optional[List]:
    """
    Преобразует сырую строку ответа в список блоков разрешений
    """
    raw = re.findall(r'\"(\[.*\\n)\"', raw_response)
    if not raw:
        return None
    json_payload = raw[0].replace(r'\n', '').replace('\\', '')
    return json.loads(json_payload)


async def extract_permission_blocks(permission_data: List, language: str) -> PermissionsType:
    """
    Извлекает из странного списка блоков разрешений структурированный словарь блоков
    """
    blocks: dict = {}
    basic, other, *other_extension = permission_data
    await _parse_basic_and_other(basic, other, blocks)
    _parse_other_extension(other_extension, language, blocks)
    return blocks


async def _parse_basic_and_other(basic: Optional[List], other: Optional[List], blocks: dict):
    """
    Парсит основной блок разрешений и блок "Другое". Оба могут прийти пустыми, но парсятся по
    одной схеме
    """
    basic = basic or []
    other = other or []
    for line in basic + other:
        if not line:
            continue
        name = line[0]
        picture = await save_picture(line[1][3][2])
        permissions = [permission_line[1] for permission_line in line[2]]
        if name not in blocks:
            blocks[name] = {'picture': picture, 'permissions': permissions}
        else:
            blocks[name]['permissions'].extend(permissions)


def _parse_other_extension(other_extension: Optional[List], language: str, blocks: dict):
    """
    Парсит третий, опциональный элемент сырых данных -- расширение блока "Другое". Может
    присутствовать при отсутствии первых двух блоков, поэтому необходимо прокидывать язык для
    правильной вставки в итоговый словарь.
    """
    if not other_extension:
        return

    for line in other_extension[0]:
        if language == 'en':
            blocks['Other']['permissions'].append(line[1])
        else:
            blocks['Другое']['permissions'].append(line[1])
