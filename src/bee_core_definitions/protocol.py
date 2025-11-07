"""协议名称转换工具

将Go代码中的协议映射转换为Python实现,提供协议名称标准化功能
"""

# 协议映射字典
PROTOCOLS_MAP = {
    "http": ["http"],
    "https": ["ssl/http", "https", "http/ssl"],
    "ssh": ["ssh"],
    "rdp": ["ms-wbt-server", "rdp"],
    "ssl/rdp": ["ssl/ms-wbt-server", "ms-wbt-servers", "rdp/ssl"],
    "ftp": ["ftp"],
    "mysql": ["mysql"],
    "mssql": ["ms-sql-s", "mssql"],
    "postgresql": ["postgresql"],
    "mongodb": ["mongodb"],
    "redis": ["redis"],
    "oracle": ["oracle"],
    "oracle-tns": ["oracle-tns"],
    "ibm-db2": ["ibm-db2"],
    "docker": ["docker"],
    "hbase": ["hbase"],
    "ldap": ["ldap"],
    "ssl/ldap": ["ssl/ldap", "ldaps", "ldap/ssl"],
    "http-proxy": ["http-proxy"],
    "ssl/http-proxy": ["ssl/http-proxy", "http-proxys", "http-proxy/ssl"],
    "ssl/docker": ["ssl/docker", "dockers", "docker/ssl"],
    "ssl/mssql": ["ssl/ms-sql-s", "ms-sql-ss", "mssql/ssl"],
    "socks5": ["socks5"],
    "socks4": ["socks4"],
    "ssl/socks5": ["ssl/socks5", "socks5s", "socks5/ssl"],
    "ssl/socks4": ["ssl/socks4", "socks4s", "socks4/ssl"],
    "apachemq": ["apachemq"],
    "daytime": ["daytime"],
    "filezilla": ["filezilla"],
    "java-object": ["java-object"],
    "jdwp": ["jdwp"],
    "jboss-remoting": ["jboss-remoting"],
    "socks-proxy": ["socks-proxy"],
    "vnc": ["vnc"],
    "vmware-auth": ["vmware-auth"],
    "openvpn": ["openvpn"],
    "openvpn-management": ["openvpn-management"],
    "remoting": ["remoting"],
    "telnet": ["telnet"],
    "git": ["git"],
    "hadoop-ipc": ["hadoop-ipc"],
    "websocket": ["websocket"],
    "zabbix": ["zabbix"],
    "java-rmi": ["java-rmi"],
    "stomp": ["stomp"],
    "ajp13": ["ajp13", "ajp"],
    "ibm-mqseries": ["ibm-mqseries"],
    "kerberos-sec": ["kerberos-sec"],
    "h2": ["h2"],
    "microsoft-ds": ["microsoft-ds"],
    "msrpc": ["msrpc"],
    "netbios-ssn": ["netbios-ssn"],
    "spark": ["spark"],
    "memcached": ["memcached"],
    "ssl": ["ssl"],
    "ssl/vmware-auth": ["ssl/vmware-auth", "vmware-auths", "vmware-auth/ssl"],
    "ssl/apachemq": ["ssl/apachemq", "apachemqs", "apachemq/ssl"],
    "ssl/daytime": ["ssl/daytime", "daytimes", "daytime/ssl"],
    "ssl/filezilla": ["ssl/filezilla", "filezillas", "filezilla/ssl"],
    "ssl/java-object": ["ssl/java-object", "java-objects", "java-object/ssl"],
    "ssl/jdwp": ["ssl/jdwp", "jdwps", "jdwp/ssl"],
    "ssl/jboss-remoting": ["ssl/jboss-remoting", "jboss-remotings", "jboss-remoting/ssl"],
    "ssl/mysql": ["ssl/mysql", "mysqls", "mysql/ssl"],
    "ssl/ssh": ["ssl/ssh", "sshs", "ssh/ssl"],
    "ssl/socks-proxy": ["ssl/socks-proxy", "socks-proxys", "socks-proxy/ssl"],
    "ssl/vnc": ["ssl/vnc", "vncs", "vnc/ssl"],
    "ssl/openvpn": ["ssl/openvpn", "openvpns", "openvpn/ssl"],
    "ssl/openvpn-management": ["ssl/openvpn-management", "openvpn-managements", "openvpn-management/ssl"],
    "ssl/remoting": ["ssl/remoting", "remotings", "remoting/ssl"],
    "ssl/ftp": ["ssl/ftp", "ftps", "ftp/ssl"],
    "ssl/telnet": ["ssl/telnet", "telnets", "telnet/ssl"],
    "ssl/git": ["ssl/git", "gits", "git/ssl"],
    "ssl/hadoop-ipc": ["ssl/hadoop-ipc", "hadoop-ipcs", "hadoop-ipc/ssl"],
    "ssl/websocket": ["ssl/websocket", "websockets", "websocket/ssl"],
    "ssl/postgresql": ["ssl/postgresql", "postgresqls", "postgresql/ssl"],
    "ssl/mongodb": ["ssl/mongodb", "mongodbs", "mongodb/ssl"],
    "ssl/redis": ["ssl/redis", "rediss", "redis/ssl"],
    "ssl/zabbix": ["ssl/zabbix", "zabbixs", "zabbix/ssl"],
    "ssl/oracle": ["ssl/oracle", "oracles", "oracle/ssl"],
    "ssl/oracle-tns": ["ssl/oracle-tns", "oracle-tnss", "oracle-tns/ssl"],
    "ssl/ibm-db2": ["ssl/ibm-db2", "ibm-db2s", "ibm-db2/ssl"],
    "ssl/hbase": ["ssl/hbase", "hbases", "hbase/ssl"],
    "ssl/java-rmi": ["ssl/java-rmi", "java-rmis", "java-rmi/ssl"],
    "ssl/stomp": ["ssl/stomp", "stomps", "stomp/ssl"],
    "ssl/ajp13": ["ssl/ajp13", "ajp13s", "ajp13/ssl"],
    "ssl/ibm-mqseries": ["ssl/ibm-mqseries", "ibm-mqseriess", "ibm-mqseries/ssl"],
    "ssl/kerberos-sec": ["ssl/kerberos-sec", "kerberos-secs", "kerberos-sec/ssl"],
    "ssl/h2": ["ssl/h2", "h2s", "h2/ssl"],
    "ssl/microsoft-ds": ["ssl/microsoft-ds", "microsoft-dss", "microsoft-ds/ssl"],
    "ssl/msrpc": ["ssl/msrpc", "msrpcs", "msrpc/ssl"],
    "ssl/netbios-ssn": ["ssl/netbios-ssn", "netbios-ssns", "netbios-ssn/ssl"],
    "ssl/spark": ["ssl/spark", "sparks", "spark/ssl"],
    "ssl/memcached": ["ssl/memcached", "memcacheds", "memcached/ssl"],
}


def _create_reverse_mapping():
    """创建反向映射以提高查找效率
    
    Returns:
        dict: 别名到标准名称的映射字典
    """
    reverse_map = {}
    for standard_name, aliases in PROTOCOLS_MAP.items():
        for alias in aliases:
            reverse_map[alias] = standard_name
    return reverse_map


# 创建反向映射实例(用于提高性能)
_REVERSE_PROTOCOLS_MAP = _create_reverse_mapping()


def protocol_name_translate(name: str) -> str:
    """协议名称转换函数(基础版本)
    
    Args:
        name: 输入的协议名称
        
    Returns:
        str: 转换后的标准协议名称,如果未找到匹配则返回原名称
        
    Examples:
        >>> protocol_name_translate("https")
        'https'
        >>> protocol_name_translate("ssl/http")
        'https'
        >>> protocol_name_translate("mysqls")
        'ssl/mysql'
        >>> protocol_name_translate("unknown-protocol")
        'unknown-protocol'
    """
    for standard_name, aliases in PROTOCOLS_MAP.items():
        if name in aliases:
            return standard_name
    return name


def protocol_name_translate_fast(name: str) -> str:
    """快速协议名称转换函数(使用反向映射)
    
    推荐使用此函数,性能更好
    
    Args:
        name: 输入的协议名称
        
    Returns:
        str: 转换后的标准协议名称,如果未找到匹配则返回原名称
        
    Examples:
        >>> protocol_name_translate_fast("https")
        'https'
        >>> protocol_name_translate_fast("ssl/http")
        'https'
        >>> protocol_name_translate_fast("mysqls")
        'ssl/mysql'
        >>> protocol_name_translate_fast("unknown-protocol")
        'unknown-protocol'
    """
    return _REVERSE_PROTOCOLS_MAP.get(name, name)


def get_protocol_aliases(standard_name: str) -> list:
    """获取标准协议名称的所有别名
    
    Args:
        standard_name: 标准协议名称
        
    Returns:
        list: 协议别名列表,如果协议不存在则返回空列表
        
    Examples:
        >>> get_protocol_aliases("https")
        ['ssl/http', 'https', 'http/ssl']
        >>> get_protocol_aliases("mysql")
        ['mysql']
    """
    return PROTOCOLS_MAP.get(standard_name, [])


def is_valid_protocol(name: str) -> bool:
    """检查是否为有效的协议名称(包括别名)
    
    Args:
        name: 协议名称
        
    Returns:
        bool: 如果是有效的协议名称返回True,否则返回False
        
    Examples:
        >>> is_valid_protocol("https")
        True
        >>> is_valid_protocol("ssl/http")
        True
        >>> is_valid_protocol("unknown")
        False
    """
    return name in _REVERSE_PROTOCOLS_MAP


def get_all_standard_protocols() -> list:
    """获取所有标准协议名称列表
    
    Returns:
        list: 按字母顺序排序的标准协议名称列表
        
    Examples:
        >>> protocols = get_all_standard_protocols()
        >>> "https" in protocols
        True
        >>> "mysql" in protocols
        True
    """
    return sorted(PROTOCOLS_MAP.keys())
