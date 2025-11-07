# bee-core-definitions

统一项目中不同代码的字典等定义。

## 安装

```bash
pip install bee-core-definitions
```

## 功能特性

### 1. 统一社会信用代码

提供统一社会信用代码的字典定义和识别功能。

```python
from bee_core_definitions import DICT_CODES, get_unit_type

# 查看所有单位类型代码
print(DICT_CODES)

# 获取单位类型
unit_type = get_unit_type("91110000000000000X")
print(unit_type)  # 输出: 企业

unit_type = get_unit_type("12110000000000000X")
print(unit_type)  # 输出: 事业单位
```

### 2. 协议名称转换

提供协议名称标准化功能,支持多种协议别名到标准名称的转换。

```python
from bee_core_definitions import (
    protocol_name_translate_fast,
    get_protocol_aliases,
    is_valid_protocol,
    get_all_standard_protocols,
)

# 转换协议名称(推荐使用快速版本)
protocol = protocol_name_translate_fast("ssl/http")
print(protocol)  # 输出: https

protocol = protocol_name_translate_fast("mysqls")
print(protocol)  # 输出: ssl/mysql

# 获取协议的所有别名
aliases = get_protocol_aliases("https")
print(aliases)  # 输出: ['ssl/http', 'https', 'http/ssl']

# 检查是否为有效协议
print(is_valid_protocol("https"))  # 输出: True
print(is_valid_protocol("unknown"))  # 输出: False

# 获取所有标准协议列表
protocols = get_all_standard_protocols()
print(f"支持 {len(protocols)} 个标准协议")
```

#### 支持的协议

包括但不限于:
- **Web协议**: http, https, websocket
- **数据库**: mysql, postgresql, mongodb, redis, oracle, mssql
- **远程访问**: ssh, rdp, vnc, telnet
- **代理**: http-proxy, socks4, socks5
- **其他**: ftp, ldap, docker, git 等

每个协议都支持 SSL/TLS 变体(如 `mysqls` → `ssl/mysql`)。

## 开发

```bash
# 克隆项目
git clone https://github.com/AbelChe/bee-core-definitions.git
cd bee-core-definitions

# 安装开发依赖
pip install -e .
pip install pytest

# 运行测试
pytest

# 运行测试并显示覆盖率
pytest --cov=bee_core_definitions tests/
```

## License

MIT
