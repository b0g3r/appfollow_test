"""
Модуль, выполняющий основную работу по экстракции и преобразованию данных из API GooglePlay
"""
import asyncio
import re
import json
from typing import List, Dict, Union

from aiohttp import ClientSession

from permission_fetcher.pictures import save_picture

BlockTyping = Dict[str, Union[str, List[str]]]


async def get_permissions(app_id: str, language: str) -> Dict[str, BlockTyping]:
    """
    Возвращает словарь блоков разрешений по идентификатору приложения и языку
    """
    raw_response = await request_app_data(app_id, language)
    permission_data = extract_permission_data(raw_response)
    permissions = await extract_permission_blocks(permission_data, language)
    return permissions


async def request_app_data(app_id: str, language: str) -> str:
    """
    Возвращает запрошенные данные о приложении через внутреннее API GooglePlay Store
    """
    params = {
        'f.sid': '7185783150060508621',
        'bl': 'boq_playuiserver_20180827.08_p0',
        'hl': language,
        'authuser': '',
        'soc-app': '121',
        'soc-platform': '1',
        'soc-device': '1',
        '_reqid': '202915',
        'rt': 'c',
    }
    post_data = {
        'f.req': r'[[["xdSrCf","[[null,[\"{0}\",7],[]]]",null,"vm96le:0|ww"]]]'.format(app_id),
        '': '',
    }

    async with ClientSession() as session:
        # TODO: нужен рефакторинг этого неприятного переноса
        async with session.post(
                url='https://play.google.com/_/PlayStoreUi/data/batchexecute',
                params=params,
                data=post_data,
        ) as resp:
            return await resp.text()


def extract_permission_data(raw_response: str) -> List:
    """
    Преобразует сырую строку ответа в список блоков разрешений
    """
    raw = re.findall(r'\"(\[.*\\n)\"', raw_response)
    json_payload = raw[0].replace('\\n', '').replace('\\', '')
    return json.loads(json_payload)


async def extract_permission_blocks(permission_data: List, language: str) -> Dict[str, BlockTyping]:
    """
    Извлекает из странного списка блоков разрешений структурированный словарь блоков
    """
    blocks: dict = {}
    # TODO: нужен рефакторинг, сейчас найдено три блока: основные разрешения, другие, расширение
    # других. Нужно разбить на три функции, видимо.
    for block in permission_data:
        # TODO: бывают пустые блоки
        if not block:
            continue
        for line in block:
            if len(line) > 2:
                name = line[0]
                picture = await save_picture(line[1][3][2])
                permissions = [permission_line[1] for permission_line in line[2]]
                if name not in blocks:
                    blocks[name] = {'picture': picture, 'permissions': permissions}
                else:
                    blocks[name]['permissions'].extend(permissions)
            elif len(line) == 2:
                if language == 'en':
                    blocks['Other']['permissions'].append(line[1])
                else:
                    blocks['Другое']['permissions'].append(line[1])
    return blocks


if __name__ == '__main__':
    asyncio.ensure_future(get_permissions('my.android.calc', 'ru'))
    loop = asyncio.get_event_loop()
    try:
        loop.run_forever()
    except Exception:
        loop.close()
