import json
import os

from yadiskapi import YaDiskApi

CONFIG_FILENAME = 'config.txt'

def load_ya_token():
    ya_disk_token = None

    # load Yandex.Disk token from config file
    if os.path.exists(CONFIG_FILENAME):
        try:
            with open(CONFIG_FILENAME, 'rt') as config_file:
                config = json.load(config_file)
                ya_disk_token = config['yandex disk token']
        except Exception as config_err:
            print(f'Error while reading config file:\n{type(config_err)}\n{config_err}')
    else:
        print('Config file not found. See "config_example.txt"')
    return ya_disk_token

if __name__ == '__main__':
    ya_disk_token = load_ya_token()

    user_ya_disk_api = YaDiskApi(ya_disk_token)

    res = user_ya_disk_api.create_dir('test')
    print(res)

    res = user_ya_disk_api.check_dir('test')
    print(res)