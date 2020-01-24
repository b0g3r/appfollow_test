"""
aiohttp server приложение для обработки запросов от фронтенда
"""
from aiohttp import web
from aiohttp.web_request import Request
from marshmallow import ValidationError

from db_utils import get_permissions
from schemas import PermissionRequest

HTTP202_STATUS_CODE = 202
HTTP200_STATUS_CODE = 200
HTTP400_STATUS_CODE = 400

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
        return web.json_response({'errors': errors.messages}, status=HTTP400_STATUS_CODE)

    error, permissions = await get_permissions(permission_request)

    if error:
        return web.json_response({'errors': {'url': ['invalid url']}}, status=HTTP400_STATUS_CODE)

    if permissions is not None:
        return web.json_response(permissions, status=HTTP200_STATUS_CODE)

    return web.json_response({}, status=HTTP202_STATUS_CODE)


app = web.Application()
app.add_routes(routes)
