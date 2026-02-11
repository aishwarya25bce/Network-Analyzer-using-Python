
from module1_ip import is_private, ip_to_list
from module2_connectivity import can_communicate

def security_check(device1, device2, routing_enabled,
                   blocked_vlans, blocked_ips, server_vlans):

    name1, ip1, vlan1 = device1
    name2, ip2, vlan2 = device2

    # First check connectivity possibility
    connectivity = can_communicate(device1, device2, routing_enabled)

    if connectivity == "ACCESS DENIED":
        return "ACCESS DENIED"

    # Convert IPs for checking
    ip1_list = ip_to_list(ip1)
    ip2_list = ip_to_list(ip2)

    # Rule 1: Block VLAN communication
    if (vlan1, vlan2) in blocked_vlans:
        return "ACCESS DENIED"

    # Rule 2: Block specific IPs
    if ip1 in blocked_ips or ip2 in blocked_ips:
        return "ACCESS DENIED"

    # Rule 3: Guest/student VLAN cannot access server VLAN
    if vlan1 not in server_vlans and vlan2 in server_vlans:
        return "ACCESS DENIED"

    return "ACCESS GRANTED"


# -------- APPLY SECURITY CHECK --------

def security_engine(devices, routing_enabled,
                    blocked_vlans, blocked_ips, server_vlans):

    print("\n--- Security Rule Results ---")

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

            print(f"{devices[i][0]} ↔ {devices[j][0]} : {result}")
