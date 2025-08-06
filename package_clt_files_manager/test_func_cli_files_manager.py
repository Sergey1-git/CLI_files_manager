import unittest
import os
from func_cli_files_manager import preparing_for_work, path_folder_test

class TestPreparing_for_work(unittest.TestCase):
    def test_preparing_for_work(self):
        print('Проверка, что функция preparing_for_work создает папку folder_test.')
        # создание папки folder_test
        preparing_for_work()
        self.assertIn('folder_test',path_folder_test)