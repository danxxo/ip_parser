import ipaddress


def get_ip_from_subnet(subnet):
    subnet = ipaddress.ip_network(subnet)
    ip_list = list(subnet.hosts())
    random_ip = str(ip_list[0])
    return random_ip

def parse_ip(input_string: str):

    try:
        ipaddress.ip_address(input_string)
        return input_string
    except ValueError:
        ip = get_ip_from_subnet(input_string)
        return ip
    