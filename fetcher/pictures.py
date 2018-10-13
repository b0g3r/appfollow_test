"""
Модуль, сохраняющий файлы иконок локально, скачивая с Google CDN
"""
import os

import aiohttp


async def save_picture(picture_url: str) -> str:
    """
    Скачивает файл по ссылке и возвращает его имя
    """
    # TODO: возможно не стоит доверять .png, реальное расширение файла можно вытащить через
    # заголовок content-type (head?)
    filename = '{0}.png'.format(picture_url.rsplit('/', maxsplit=1)[1])
    filepath = os.path.join('/opt/pictures', filename)
    if not os.path.exists(filepath):
        picture = await download_file(picture_url)
        with open(filepath, 'wb') as picture_file:
            picture_file.write(picture)
    return filename


async def download_file(url) -> bytes:
    """
    Асинхронный выкачиватиль файла по ссылке
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.read()
