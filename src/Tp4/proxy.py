import os

class Ping:
    def execute(self, ip):
        if not ip.startswith("192."):
            print(f"IP no válida para método execute: {ip}")
            return
        for i in range(10):
            os.system(f"ping -c 1 {ip}")

    def executefree(self, ip):
        for i in range(10):
            os.system(f"ping -c 1 {ip}")

class PingProxy:
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip):
        if ip == "192.168.0.254":
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(ip)
