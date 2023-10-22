import time
from config import SERVERS, CHECK_INTERVAL
from checker import ServerChecker


class ServerManager:
    def __init__(self):
        self.servers = [ServerChecker(url) for url in SERVERS]

    def run(self):
        while True:
            for server in self.servers:
                is_up, response_time = server.check_status()
                if is_up:
                    print(f"[INFO] {server.url} is up. Response time: {response_time:.2f} seconds")
                else:
                    pass
            time.sleep(CHECK_INTERVAL)
