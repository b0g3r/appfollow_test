"""
aiohttp server приложение для обработки запросов от фронтенда
"""
from aiohttp import web
from aiohttp.web_request import Request
from marshmallow import ValidationError

from db_utils import get_permissions
from schemas import PermissionRequest

routes = web.RouteTableDef()


@routes.post('/permissions')
async def main_view(request: Request):
    """
    FIXME: Need autodoc
    """
    request_data = await request.json()
    try:
        permission_request = PermissionRequest().load(request_data)
    except ValidationError as errors:
        return web.json_response({'errors': errors.messages}, status=400)

    error, permissions = await get_permissions(permission_request)

    if error:
        return web.json_response({'errors': {'url': ['invalid url']}}, status=400)

    if permissions:
        return web.json_response(permissions, status=200)
    else:
        return web.json_response({}, status=202)


app = web.Application()
app.add_routes(routes)
