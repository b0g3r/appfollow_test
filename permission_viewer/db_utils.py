"""
Модуль, содержащий утилиты для работы с базой: запись и чтение
"""
from typing import Tuple, Dict

from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient('mongo')
db = client.AppFollow
collection = db.application_data


async def get_permissions(permission_request: Dict[str, str]) -> Tuple[bool, dict]:
    """
    Пытается достать данные о приложении из базы, при их отсутствии - кладет запрос.
    При ошибке запроса возвращает первым элементом ответа True. Второй элемент пуст,
    если разрешения ещё не запрошены.
    """
    application_data = await collection.find_one(permission_request)
    if application_data:
        if application_data.get('error'):
            return True, {}
        if not application_data.get('permissions'):
            return False, {}

        application_data.pop('_id')
        return False, application_data
    else:
        await collection.insert_one(permission_request)
        return False, {}
