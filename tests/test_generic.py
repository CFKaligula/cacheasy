from src import cacheasy as local_cacheasy
import os
import pytest


@pytest.fixture
def env_file_path():
    env_file_path = '.env'
    yield env_file_path
    os.remove(env_file_path)


def test_cache_folder():
    assert local_cacheasy.get_cache_folderpath() == 'cache'


def test_cache_folder_with_env(env_file_path):

    with open(env_file_path, 'w') as env_file:
        env_file.write('cache_folderpath = ok/cache')
    assert local_cacheasy.get_cache_folderpath() == os.path.join('ok', 'cache')


def test_cache_filepath():
    assert local_cacheasy.get_cache_filepath('a') == os.path.join('cache', 'a')
