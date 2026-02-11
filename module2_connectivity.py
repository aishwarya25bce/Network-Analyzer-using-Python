
def can_communicate(device1, device2, routing_enabled):
    name1, ip1, vlan1 = device1
    name2, ip2, vlan2 = device2

    # Same VLAN
    if vlan1 == vlan2:
        return "ACCESS GRANTED"

    # Different VLAN
    if routing_enabled:
        return "ACCESS GRANTED"
    else:
        return "ACCESS DENIED"


def connectivity_checker(devices, routing_enabled):
    n = len(devices)

    for i in range(n):
        for j in range(i + 1, n):
            result = can_communicate(
                devices[i], devices[j], routing_enabled
            )
            print(f"{devices[i][0]} ↔ {devices[j][0]} : {result}")

devices = []



