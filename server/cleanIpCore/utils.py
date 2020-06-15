from cleanIpCore.models import *
from cleanIpCore.consts import *


def get_free_ip():
    ips = [s.ip for s in Session.objects.all()]
    for port in range(S_MIN_PORT, S_MAX_PORT):
        new_ip = f'{S_BASE_IP}:{port}'
        if new_ip not in ips:
            return new_ip
    raise Exception("Free ip not found")

