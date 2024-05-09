import ipaddress


def get_ip_from_subnet(subnet):
    subnet = ipaddress.ip_network(subnet)

    # Получаем список всех IP-адресов в подсети.
    ip_list = list(subnet.hosts())

    # Выбираем случайный IP-адрес из списка.
    random_ip = str(ip_list[0])

    return random_ip

def parse_ip(input_string: str):

    try:
        ipaddress.ip_address(input_string)
        return input_string
    except ValueError:
        ip = get_ip_from_subnet(input_string)
        return ip
    