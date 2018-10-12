"""
Модуль, содержащий схемы для валидации, сериализации и десериализации
"""
from typing import Optional

from urllib.parse import parse_qsl, urlparse

from marshmallow import Schema, fields, pre_load, ValidationError, validates


class PermissionRequest(Schema):
    """
    Схема для валидации и десериализации входящих данных
    """

    application_id = fields.String(data_key='id', required=True, allow_none=False)
    language = fields.String(data_key='hl', required=True, allow_none=False)

    @pre_load
    def parse_url(self, request_data: dict) -> dict:
        """
        Разбирает url на параметры, необходимые для запроса
        """
        url = request_data.get('url')
        if not url:
            raise ValidationError('"url" param must be set', ['url'])
        params = dict(parse_qsl(urlparse(url).query))
        return params

    @validates('language')
    def _validate_language(self, language: Optional[str]):
        if language not in {'en', 'ru'}:
            raise ValidationError('Invalid language, must be "en" or "ru"')
