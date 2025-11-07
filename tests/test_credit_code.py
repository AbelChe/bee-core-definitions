"""测试统一社会信用代码相关功能"""

import pytest
from bee_core_definitions.credit_code import DICT_CODES, get_unit_type


class TestDictCodes:
    """测试 DICT_CODES 字典"""
    
    def test_dict_codes_exists(self):
        """测试字典是否存在"""
        assert DICT_CODES is not None
        assert isinstance(DICT_CODES, dict)
    
    def test_dict_codes_content(self):
        """测试字典内容"""
        assert DICT_CODES["11"] == "机关"
        assert DICT_CODES["91"] == "企业"
        assert DICT_CODES["92"] == "个体工商户"


class TestGetUnitType:
    """测试 get_unit_type 函数"""
    
    def test_enterprise(self):
        """测试企业类型识别"""
        assert get_unit_type("91110000000000000X") == "企业"
    
    def test_government(self):
        """测试机关类型识别"""
        assert get_unit_type("11110000000000000X") == "机关"
    
    def test_institution(self):
        """测试事业单位类型识别"""
        assert get_unit_type("12110000000000000X") == "事业单位"
    
    def test_individual_business(self):
        """测试个体工商户类型识别"""
        assert get_unit_type("92110000000000000X") == "个体工商户"
    
    def test_cooperative(self):
        """测试农民专业合作社类型识别"""
        assert get_unit_type("93110000000000000X") == "农民专业合作社"
    
    def test_social_organization(self):
        """测试社会团体类型识别"""
        assert get_unit_type("51110000000000000X") == "社会团体"
    
    def test_foundation(self):
        """测试基金会类型识别"""
        assert get_unit_type("53110000000000000X") == "基金会"
    
    def test_unknown_code(self):
        """测试未知代码"""
        assert get_unit_type("99110000000000000X") == "UNKNOWN"
    
    def test_empty_string(self):
        """测试空字符串"""
        assert get_unit_type("") == ""
    
    def test_none_value(self):
        """测试 None 值"""
        assert get_unit_type(None) == ""
    
    def test_short_code(self):
        """测试短代码"""
        assert get_unit_type("91") == "企业"
    
    def test_other_type(self):
        """测试其他类型"""
        assert get_unit_type("Y1110000000000000X") == "其他"
