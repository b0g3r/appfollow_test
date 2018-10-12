"""
Точка входа в приложение
"""

from aiohttp import web

from app import app

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8000)  # noqa: S104
