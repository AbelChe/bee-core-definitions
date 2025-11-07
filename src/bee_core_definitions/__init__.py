"""bee-core-definitions - 统一项目中不同代码的字典等定义"""

__version__ = "0.1.0"

from .credit_code import DICT_CODES, get_unit_type
from .protocol import (
    PROTOCOLS_MAP,
    protocol_name_translate,
    protocol_name_translate_fast,
    get_protocol_aliases,
    is_valid_protocol,
    get_all_standard_protocols,
)

__all__ = [
    # 统一社会信用代码
    "DICT_CODES",
    "get_unit_type",
    # 协议名称转换
    "PROTOCOLS_MAP",
    "protocol_name_translate",
    "protocol_name_translate_fast",
    "get_protocol_aliases",
    "is_valid_protocol",
    "get_all_standard_protocols",
]
