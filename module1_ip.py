
def ip_to_list(ip):
    return list(map(int, ip.split(".")))


def list_to_ip(parts):
    return ".".join(map(str, parts))


def is_valid_ip(parts):
    return len(parts) == 4 and all(0 <= x <= 255 for x in parts)


def is_private(ip):
    a, b, _, _ = ip
    if a == 10:
        return True
    if a == 172 and 16 <= b <= 31:
        return True
    if a == 192 and b == 168:
        return True
    return False


def calculate_network(ip, mask):
    return [ip[i] & mask[i] for i in range(4)]


def calculate_broadcast(network, mask):
    return [network[i] | (255 - mask[i]) for i in range(4)]


def count_hosts(mask):
    # Count number of host bits
    host_bits = 0
    for part in mask:
        host_bits += bin(part).count('0') - 1

    usable = (2 ** host_bits) - 2
    return max(usable, 0)


def ip_subnet_validator(ip_input, mask_input):
    ip = ip_to_list(ip_input)
    mask = ip_to_list(mask_input)

    if not (is_valid_ip(ip) and is_valid_ip(mask)):
        print("Invalid IP or subnet mask")
        return

    network = calculate_network(ip, mask)
    broadcast = calculate_broadcast(network, mask)

    usable_hosts = count_hosts(mask)

    ip_type = "Private" if is_private(ip) else "Public"

    if ip == network:
        addr_type = "Network Address"
    elif ip == broadcast:
        addr_type = "Broadcast Address"
    else:
        addr_type = "Usable Host"

    
    print("IP Type:", ip_type)
    print("Network ID:", list_to_ip(network))
    print("Broadcast Address:", list_to_ip(broadcast))
    print("Total Usable Hosts:", usable_hosts)
    print("Address Type:", addr_type)




