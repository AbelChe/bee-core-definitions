"""统一社会信用代码相关定义和工具函数"""

# 参考文件：https://www.cods.org.cn/c/2020-10-29/12575.html

# 统一社会信用代码字典
DICT_CODES = {
    "11": "机关",
    "12": "事业单位",
    "13": "中央编办直接管理机构编制的群众团体",
    "19": "其他机构",
    "51": "社会团体",
    "52": "民办非企业单位",
    "59": "其他民政单位",
    "53": "基金会",
    "91": "企业",
    "92": "个体工商户",
    "93": "农民专业合作社",
    "Y1": "其他",
}


def get_unit_type(credit_code):
    """通过统一社会信用代码识别单位类型
    
    Args:
        credit_code: 统一社会信用代码字符串
        
    Returns:
        str: 单位类型名称，如果无法识别返回 "UNKNOWN"，如果输入为空返回空字符串
        
    Examples:
        >>> get_unit_type("91110000000000000X")
        '企业'
        >>> get_unit_type("12345678901234567A")
        '事业单位'
        >>> get_unit_type("")
        ''
        >>> get_unit_type("99110000000000000X")
        'UNKNOWN'
    """
    if credit_code:
        for k, v in DICT_CODES.items():
            if credit_code[:2] == k:
                return v
        return "UNKNOWN"
    return ""
