from module1_ip import ip_subnet_validator
from module2_connectivity import connectivity_checker
from module3_security import security_engine
from module3_security import security_check
from module4_innovation import detect_duplicate_ips


def get_devices():
    devices = []
    n = int(input("\nEnter number of devices: "))

    for _ in range(n):
        print("\nEnter device details:")
        name = input("Device name: ")
        ip = input("IP address: ")
        vlan = int(input("VLAN ID: "))
        devices.append((name, ip, vlan))
    return devices


def main():
    print("====== NETWORK ANALYZER ======")

    # ---------------- MODULE 1 ----------------
    print("\n=== MODULE 1 : IP & SUBNET ANALYSIS ===")

    ip_input = input("Enter IP address: ")
    mask_input = input("Enter subnet mask: ")

    ip_subnet_validator(ip_input, mask_input)

    # ---------------- DEVICE INPUT ----------------
    print("\n=== MODULE 2 : CONNECTIVITY CHECK ===")
    devices = get_devices()

    
    

    routing_enabled = input(
        "Enable inter-VLAN routing? (y/n): "
    ).lower() == "y"

    connectivity_checker(devices, routing_enabled)

    # ---------------- MODULE 3 ----------------
    from module3_security import security_check


    def run_module3(devices, routing_enabled):
        print("\n=== MODULE 3 : SECURITY ENGINE ===")

        # ---- VLAN restriction rules ----
        blocked_vlans = []
        rule_count = int(input("Number of VLAN access restrictions: "))

        for _ in range(rule_count):
            v1 = int(input("Blocked VLAN (source): "))
            v2 = int(input("Blocked VLAN (destination): "))
            blocked_vlans.append((v1, v2))

        # ---- Block specific IPs ----
        blocked_ips = []
        ip_count = int(input("Number of blocked IPs: "))
        for _ in range(ip_count):
            blocked_ips.append(input("Blocked IP: "))

        # ---- Server VLAN rule ----
        server_vlans = list(
            map(int, input("Server VLANs (space separated): ").split())
        )

        print("\n--- Security Results ---")

        total_connections = 0
        granted = 0
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

                total_connections += 1

                if result == "ACCESS GRANTED":
                    granted += 1
                else:
                    denied += 1

                print(f"{devices[i][0]} ↔ {devices[j][0]} : {result}")

        vlan_set = {vlan for _, _, vlan in devices}

        print("\n--- Security Summary ---")
        print("Total VLANs:", len(vlan_set))
        print("Total Connections:", total_connections)
        print("Access Granted:", granted)
        print("Access Denied:", denied)

    




    

    # ---------------- MODULE 4 ----------------
    print("\n=== MODULE 4 : DUPLICATE IP DETECTION ===")

    duplicates = detect_duplicate_ips(devices)

    if duplicates:
        print("Duplicate IPs found:", duplicates)
    else:
        print("No duplicate IPs detected.")

    print("\n====== ANALYSIS COMPLETE ======")


if __name__ == "__main__":
    main()


