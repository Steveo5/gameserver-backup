import subprocess
import string
import random
from os import system
import time
from rcon import Client


class RconClient:
    host = '127.0.0.1'
    port = 25565
    password = 'minecraft'

    def __init__(self, host, port, password):
        self.host = host
        self.port = port
        self.password = password

    def execute(self, command):
        print('Executing the command: ' + command)

        with Client(self.host, self.port, passwd=self.password) as client:
            response = client.run(command)

        return response
