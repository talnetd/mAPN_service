import socket
import ssl
from mAPN_service.modules.signleton import Singleton


class RouterOsApi(Singleton):
    '''Ref: https://github.com/BenMenking/routeros-api/blob/master/routeros_api.class.php
    '''

    debug = False
    connected = False
    port = 8728
    ssl = False
    timeout = 3
    attempts = 5
    delay = 3
    socket = None
    error_no = None
    error_str = None

    def debug(self, text):
        if self.debug:
            print(text)

    def encode_length(self, length):
        chr_length = None

        if length < 0x80:
            chr_length = chr(length)
        elif length < 0x4000:
            length |= 0x8000
            chr_length = chr((length >> 8) & 0xFF) + chr(length & 0xFF)
        elif length < 0x200000:
            length |= 0xC00000
            chr_length = chr((length >> 16) & 0xFF) + chr((length >> 8) & 0xFF) + chr(length & 0xFF)
        elif length < 0x10000000:
            length |= 0xE0000000
            chr_length = chr((length >> 24) & 0xFF) + chr((length >> 16) & 0xFF) + chr((length >> 8) & 0xFF) + chr(length & 0xFF)
        elif length >= 0x10000000:
            chr_length = chr(0xF0) + chr((length >> 24) & 0xFF) + chr((length >> 16) & 0xFF) + chr((length >> 8) & 0xFF) + chr(length & 0xFF)

        return chr_length

    def _creat_socket(self):
        self.socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )
        self.socket.settimeout(self.timeout)

    def connect(self, ip, login, password):
        for i in range(self.attempts):
            self.connected = False
            socket = self._creat_socket()

    def disconnect(self):
        pass

    def parse_response(self, response):
        pass

    def parse_response_v2(self, response):
        pass

    def array_change_key_name(self, array):
        pass

    def read(self, parse=True):
        pass

    def write(self, command, param2=True):
        pass

    def comm(self, com, arr=[]):
        pass

    def __del__(self):
        self.disconnect()
