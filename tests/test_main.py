import pytest

from main import load_ya_token
from yadiskapi import YaDiskApi


class TestYaDiskApi:
    dir_list = ['test', 'some dir']
    
    @pytest.fixture(autouse=True)
    def get_ya_token(self):
        self.ya_disk_token = load_ya_token()
        self.ya_disk_api = YaDiskApi(self.ya_disk_token)
        
    # проверка что вернулся код об успешном создании папки (201)
    @pytest.mark.parametrize(
        'dir,expected', [(dir, 201) for dir in dir_list]
    )
    def test_ok_status_code(self, dir, expected):
        if self.ya_disk_api.check_dir(dir) == {'name': dir}:
            self.ya_disk_api.del_dir(dir)
        res = self.ya_disk_api.create_dir(dir)
        assert res == expected
    
    # проверка что созданная папка появилась на Яндекс.Диске
    @pytest.mark.parametrize(
        'dir,expected', [(dir, {'name': dir}) for dir in dir_list]
    )
    def test_check_if_dir_exists(self, dir, expected):
        self.ya_disk_api.create_dir(dir)
        res = self.ya_disk_api.check_dir(dir)
        assert res == expected
    
    # проверка что при попытку создать уже существующую папку
    # вернется код 409
    @pytest.mark.parametrize(
        'dir,expected', [(dir, 409) for dir in dir_list]
    )
    def test_dir_already_exists(self, dir, expected):
        res = self.ya_disk_api.create_dir(dir)
        assert res == expected