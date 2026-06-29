import ipaddress

try:
    ip_input = input("Enter IP with CIDR (Example: 192.168.1.10/24): ")

    network = ipaddress.ip_network(ip_input, strict=False)

    ip = ipaddress.ip_interface(ip_input).ip

    first_octet = int(str(ip).split('.')[0])

    # Determine class
    if 1 <= first_octet <= 126:
        ip_class = "A"
        default_cidr = 8

    elif 128 <= first_octet <= 191:
        ip_class = "B"
        default_cidr = 16

    elif 192 <= first_octet <= 223:
        ip_class = "C"
        default_cidr = 24

    elif 224 <= first_octet <= 239:
        ip_class = "D (Multicast)"
        default_cidr = None

    elif 240 <= first_octet <= 255:
        ip_class = "E (Experimental)"
        default_cidr = None

    else:
        ip_class = "Unknown"
        default_cidr = None

    print("\n----- Network Information -----")

    print("IP Address        :", ip)
    print("IP Class          :", ip_class)
    print("Network Address   :", network.network_address)
    print("Broadcast Address :", network.broadcast_address)
    print("Subnet Mask       :", network.netmask)
    print("CIDR Prefix       : /" + str(network.prefixlen))
    print("Total Addresses   :", network.num_addresses)

    hosts = list(network.hosts())

    if len(hosts) > 0:
        print("First Host        :", hosts[0])
        print("Last Host         :", hosts[-1])
        print("Usable Hosts      :", len(hosts))

    if default_cidr is not None:
        print("Default Class CIDR: /" + str(default_cidr))

        if network.prefixlen != default_cidr:
            print("\nWARNING:")
            print(
                f"IP belongs to Class {ip_class}, "
                f"whose default mask is /{default_cidr}, "
                f"but you entered /{network.prefixlen} (CIDR subnetting)."
            )

except ValueError as e:
    print("\nERROR:")
    print("Invalid IP Address or CIDR!")
    print(e)