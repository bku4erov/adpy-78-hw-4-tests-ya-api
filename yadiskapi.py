import requests


class YaDiskApi:

    url = 'https://cloud-api.yandex.net/v1/disk/'

    def __init__(self, token):
        self.token = token
    
    def get_headers(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        return headers
    
    def create_dir(self, dir_name, dir_path = '/'):
        url_create_dir = self.url + 'resources'
        res = requests.put(
            url=url_create_dir,
            params={'path': f'{dir_path.rstrip("/")}/{dir_name}'},
            headers=self.get_headers()
        )
        return res.status_code

    def check_dir(self, dir_name, dir_path = '/'):
        url_get_metadata = self.url + 'resources'
        res = requests.get(
            url=url_get_metadata,
            params={'path': f'{dir_path.rstrip("/")}/{dir_name}', 'fields': 'name'},
            headers=self.get_headers(),
        )
        return res.json()
