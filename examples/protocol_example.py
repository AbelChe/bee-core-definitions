#!/usr/bin/env python3
"""协议名称转换示例

演示如何使用 bee_core_definitions 包中的协议转换功能
"""

from bee_core_definitions import (
    protocol_name_translate_fast,
    get_protocol_aliases,
    is_valid_protocol,
    get_all_standard_protocols,
)


def main():
    """主函数"""
    # 测试用例
    test_cases = [
        "http",
        "ssl/http",
        "https",
        "mysql",
        "ssl/mysql",
        "mysqls",
        "rdp",
        "ms-wbt-server",
        "unknown-protocol"
    ]

    print("=" * 60)
    print("协议名称转换测试")
    print("=" * 60)

    for test_name in test_cases:
        result = protocol_name_translate_fast(test_name)
        is_valid = is_valid_protocol(test_name)
        status = "✓" if is_valid else "✗"
        print(f"{status} {test_name:20} -> {result:20}")

    print("\n" + "=" * 60)
    print("协议别名查询")
    print("=" * 60)

    # 查询一些常用协议的别名
    protocols_to_check = ["https", "mysql", "ssl/mysql", "rdp", "ssl/rdp"]
    for protocol in protocols_to_check:
        aliases = get_protocol_aliases(protocol)
        print(f"\n{protocol}:")
        for alias in aliases:
            print(f"  - {alias}")

    print("\n" + "=" * 60)
    print("支持的标准协议列表")
    print("=" * 60)

    all_protocols = get_all_standard_protocols()
    print(f"\n共支持 {len(all_protocols)} 个标准协议:\n")

    # 按类别分组显示
    web_protocols = [p for p in all_protocols if any(x in p for x in ["http", "websocket"])]
    db_protocols = [p for p in all_protocols if any(x in p for x in ["mysql", "postgresql", "mongodb", "redis", "oracle", "mssql", "db2"])]
    remote_protocols = [p for p in all_protocols if any(x in p for x in ["ssh", "rdp", "vnc", "telnet"])]

    print("Web 协议:")
    for p in web_protocols:
        print(f"  - {p}")

    print("\n数据库协议:")
    for p in db_protocols[:10]:  # 只显示前10个
        print(f"  - {p}")
    if len(db_protocols) > 10:
        print(f"  ... 还有 {len(db_protocols) - 10} 个")

    print("\n远程访问协议:")
    for p in remote_protocols:
        print(f"  - {p}")

    print(f"\n其他协议: {len(all_protocols) - len(web_protocols) - len(db_protocols) - len(remote_protocols)} 个")

    print("\n" + "=" * 60)
    print("实际应用场景")
    print("=" * 60)

    # 模拟从配置或扫描结果中获取的协议名称
    scan_results = [
        ("192.168.1.1", "ms-wbt-server"),
        ("192.168.1.2", "ssl/http"),
        ("192.168.1.3", "mysqls"),
        ("192.168.1.4", "postgresql"),
    ]

    print("\n扫描结果标准化:")
    for ip, protocol in scan_results:
        standard_name = protocol_name_translate_fast(protocol)
        print(f"{ip:15} {protocol:20} -> {standard_name}")


if __name__ == "__main__":
    main()
