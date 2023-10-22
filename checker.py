import requests


class Server:

    def __init__(self, url):
        self.url = url

    def check_status(self):
        try:
            response = requests.get(self.url, timeout=5)
            if response.status_code == 200:
                return True, response.elapsed.total_seconds()
            else:
                return False, None
        except requests.RequestException:
            return False, None

