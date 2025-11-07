"""测试协议名称转换功能"""

import pytest
from bee_core_definitions.protocol import (
    PROTOCOLS_MAP,
    protocol_name_translate,
    protocol_name_translate_fast,
    get_protocol_aliases,
    is_valid_protocol,
    get_all_standard_protocols,
)


class TestProtocolsMap:
    """测试 PROTOCOLS_MAP 字典"""
    
    def test_protocols_map_exists(self):
        """测试协议映射字典是否存在"""
        assert PROTOCOLS_MAP is not None
        assert isinstance(PROTOCOLS_MAP, dict)
    
    def test_protocols_map_content(self):
        """测试协议映射字典内容"""
        assert "https" in PROTOCOLS_MAP
        assert "mysql" in PROTOCOLS_MAP
        assert "ssl/mysql" in PROTOCOLS_MAP
        assert "rdp" in PROTOCOLS_MAP


class TestProtocolNameTranslate:
    """测试 protocol_name_translate 函数"""
    
    def test_http_protocol(self):
        """测试 HTTP 协议转换"""
        assert protocol_name_translate("http") == "http"
    
    def test_https_variants(self):
        """测试 HTTPS 的各种变体"""
        assert protocol_name_translate("https") == "https"
        assert protocol_name_translate("ssl/http") == "https"
        assert protocol_name_translate("http/ssl") == "https"
    
    def test_mysql_variants(self):
        """测试 MySQL 的各种变体"""
        assert protocol_name_translate("mysql") == "mysql"
        assert protocol_name_translate("mysqls") == "ssl/mysql"
        assert protocol_name_translate("ssl/mysql") == "ssl/mysql"
    
    def test_rdp_variants(self):
        """测试 RDP 的各种变体"""
        assert protocol_name_translate("rdp") == "rdp"
        assert protocol_name_translate("ms-wbt-server") == "rdp"
        assert protocol_name_translate("ssl/ms-wbt-server") == "ssl/rdp"
    
    def test_mssql_variants(self):
        """测试 MSSQL 的各种变体"""
        assert protocol_name_translate("mssql") == "mssql"
        assert protocol_name_translate("ms-sql-s") == "mssql"
    
    def test_ssh_protocol(self):
        """测试 SSH 协议"""
        assert protocol_name_translate("ssh") == "ssh"
        assert protocol_name_translate("sshs") == "ssl/ssh"
    
    def test_ftp_variants(self):
        """测试 FTP 的各种变体"""
        assert protocol_name_translate("ftp") == "ftp"
        assert protocol_name_translate("ftps") == "ssl/ftp"
    
    def test_ldap_variants(self):
        """测试 LDAP 的各种变体"""
        assert protocol_name_translate("ldap") == "ldap"
        assert protocol_name_translate("ldaps") == "ssl/ldap"
        assert protocol_name_translate("ssl/ldap") == "ssl/ldap"
    
    def test_unknown_protocol(self):
        """测试未知协议"""
        assert protocol_name_translate("unknown-protocol") == "unknown-protocol"
        assert protocol_name_translate("xyz123") == "xyz123"


class TestProtocolNameTranslateFast:
    """测试 protocol_name_translate_fast 函数"""
    
    def test_consistency_with_slow_version(self):
        """测试快速版本与基础版本的一致性"""
        test_cases = [
            "http", "https", "ssl/http", "mysql", "mysqls",
            "rdp", "ssh", "ftp", "ftps", "unknown"
        ]
        for protocol in test_cases:
            assert protocol_name_translate(protocol) == protocol_name_translate_fast(protocol)
    
    def test_https_variants(self):
        """测试 HTTPS 的各种变体"""
        assert protocol_name_translate_fast("https") == "https"
        assert protocol_name_translate_fast("ssl/http") == "https"
    
    def test_unknown_protocol(self):
        """测试未知协议"""
        assert protocol_name_translate_fast("unknown") == "unknown"


class TestGetProtocolAliases:
    """测试 get_protocol_aliases 函数"""
    
    def test_https_aliases(self):
        """测试 HTTPS 的别名"""
        aliases = get_protocol_aliases("https")
        assert "https" in aliases
        assert "ssl/http" in aliases
        assert "http/ssl" in aliases
        assert len(aliases) == 3
    
    def test_mysql_aliases(self):
        """测试 MySQL 的别名"""
        aliases = get_protocol_aliases("mysql")
        assert aliases == ["mysql"]
    
    def test_ssl_mysql_aliases(self):
        """测试 SSL MySQL 的别名"""
        aliases = get_protocol_aliases("ssl/mysql")
        assert "ssl/mysql" in aliases
        assert "mysqls" in aliases
        assert "mysql/ssl" in aliases
    
    def test_unknown_protocol(self):
        """测试未知协议"""
        aliases = get_protocol_aliases("unknown")
        assert aliases == []


class TestIsValidProtocol:
    """测试 is_valid_protocol 函数"""
    
    def test_valid_protocols(self):
        """测试有效的协议名称"""
        assert is_valid_protocol("http") is True
        assert is_valid_protocol("https") is True
        assert is_valid_protocol("ssl/http") is True
        assert is_valid_protocol("mysql") is True
        assert is_valid_protocol("mysqls") is True
        assert is_valid_protocol("rdp") is True
        assert is_valid_protocol("ms-wbt-server") is True
    
    def test_invalid_protocols(self):
        """测试无效的协议名称"""
        assert is_valid_protocol("unknown") is False
        assert is_valid_protocol("xyz123") is False
        assert is_valid_protocol("") is False


class TestGetAllStandardProtocols:
    """测试 get_all_standard_protocols 函数"""
    
    def test_returns_list(self):
        """测试返回列表"""
        protocols = get_all_standard_protocols()
        assert isinstance(protocols, list)
        assert len(protocols) > 0
    
    def test_contains_common_protocols(self):
        """测试包含常见协议"""
        protocols = get_all_standard_protocols()
        assert "http" in protocols
        assert "https" in protocols
        assert "mysql" in protocols
        assert "ssh" in protocols
        assert "rdp" in protocols
    
    def test_is_sorted(self):
        """测试是否已排序"""
        protocols = get_all_standard_protocols()
        assert protocols == sorted(protocols)
    
    def test_no_duplicates(self):
        """测试没有重复项"""
        protocols = get_all_standard_protocols()
        assert len(protocols) == len(set(protocols))


class TestRealWorldScenarios:
    """测试真实场景"""
    
    def test_database_protocols(self):
        """测试数据库协议"""
        assert protocol_name_translate_fast("mysql") == "mysql"
        assert protocol_name_translate_fast("postgresql") == "postgresql"
        assert protocol_name_translate_fast("mongodb") == "mongodb"
        assert protocol_name_translate_fast("redis") == "redis"
        assert protocol_name_translate_fast("oracle") == "oracle"
    
    def test_ssl_database_protocols(self):
        """测试 SSL 数据库协议"""
        assert protocol_name_translate_fast("mysqls") == "ssl/mysql"
        assert protocol_name_translate_fast("postgresqls") == "ssl/postgresql"
        assert protocol_name_translate_fast("mongodbs") == "ssl/mongodb"
        assert protocol_name_translate_fast("rediss") == "ssl/redis"
    
    def test_web_protocols(self):
        """测试 Web 协议"""
        assert protocol_name_translate_fast("http") == "http"
        assert protocol_name_translate_fast("https") == "https"
        assert protocol_name_translate_fast("websocket") == "websocket"
        assert protocol_name_translate_fast("websockets") == "ssl/websocket"
    
    def test_remote_access_protocols(self):
        """测试远程访问协议"""
        assert protocol_name_translate_fast("ssh") == "ssh"
        assert protocol_name_translate_fast("rdp") == "rdp"
        assert protocol_name_translate_fast("vnc") == "vnc"
        assert protocol_name_translate_fast("telnet") == "telnet"
