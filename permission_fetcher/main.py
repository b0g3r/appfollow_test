"""
Точка входа в приложение
"""
import asyncio

from extractor import get_permissions
from db_utils import permission_requests, save_permission


async def entry_point():
    """
    В цикле проходит по асинхронному итератору с запросами на получение разрешений
    """
    async for id_, application_id, language in permission_requests():
        permissions = await get_permissions(application_id, language)
        await save_permission(id_, permissions)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(entry_point())
    loop.close()
