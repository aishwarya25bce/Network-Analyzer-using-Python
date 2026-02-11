
from module1_ip import ip_to_list, is_private
from module2_connectivity import can_communicate
from module3_security import security_check


# -------- DUPLICATE IP DETECTION --------
def detect_duplicate_ips(devices):
    seen = set()
    duplicates = set()

    for name, ip, vlan in devices:
        if ip in seen:
            duplicates.add(ip)
        else:
            seen.add(ip)

    return list(duplicates)


# -------- NETWORK ANALYSIS REPORT --------
def network_analysis_report(devices,
                            routing_enabled,
                            blocked_vlans,
                            blocked_ips,
                            server_vlans):

    report = {}

    report["total_devices"] = len(devices)

    # VLAN distribution
    vlan_map = {}
    for name, ip, vlan in devices:
        vlan_map.setdefault(vlan, []).append(name)

    report["total_vlans"] = len(vlan_map)
    report["devices_per_vlan"] = vlan_map

    # Private vs Public count
    private_count = 0
    public_count = 0

    for name, ip, vlan in devices:
        ip_list = ip_to_list(ip)
        if is_private(ip_list):
            private_count += 1
        else:
            public_count += 1

    report["private_devices"] = private_count
    report["public_devices"] = public_count

    # Connectivity summary
    allowed = 0
    denied = 0

    n = len(devices)

    for i in range(n):
        for j in range(i + 1, n):

            result = security_check(
                devices[i],
                devices[j],
                routing_enabled,
                blocked_vlans,
                blocked_ips,
                server_vlans
            )

            if result == "ACCESS GRANTED":
                allowed += 1
            else:
                denied += 1

    report["allowed_connections"] = allowed
    report["denied_connections"] = denied

    return report


# -------- MAIN MODULE 4 FUNCTION --------
def innovation_module(devices,
                      routing_enabled,
                      blocked_vlans,
                      blocked_ips,
                      server_vlans):

    duplicates = detect_duplicate_ips(devices)

    report = network_analysis_report(
        devices,
        routing_enabled,
        blocked_vlans,
        blocked_ips,
        server_vlans
    )

    return {
        "duplicate_ips": duplicates,
        "network_report": report
    }
