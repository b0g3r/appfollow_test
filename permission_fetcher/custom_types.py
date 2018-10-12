"""
Модуль для типов, используемых в проекте
"""
from typing import Dict, Union, List

BlockType = Dict[str, Union[str, List[str]]]
PermissionsType = Dict[str, BlockType]
