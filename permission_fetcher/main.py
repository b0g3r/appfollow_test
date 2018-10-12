"""
Точка входа в приложение
"""
import asyncio
import pprint

from permission_fetcher.extractor import get_permissions


async def entry_point():
    """
    Прогоняет несколько тестовых приложений :shrug:
    """
    applications = [
        ('com.digitalchemy.calculator.freedecimal', 'en'),
        ('my.android.calc', 'ru'),
        ('com.wlxd.pomochallenge', 'ru'),
        ('ru.mail.deshevle', 'en'),
        ('com.locationcoin', 'ru'),
        ('org.telegram.messenger', 'en'),
        ('org.thunderdog.challegram', 'en'),
    ]
    for application_id, language in applications:
        pprint.pprint(await get_permissions(application_id, language))

if __name__ == '__main__':
    asyncio.ensure_future(entry_point())
    loop = asyncio.get_event_loop()
    try:
        loop.run_forever()
    except Exception:
        loop.close()
