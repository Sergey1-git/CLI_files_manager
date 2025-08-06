import unittest
import os
from func_cli_files_manager import preparing_for_work, path_folder_test,find_folders_and_files, path_test1

class TestPreparing_for_work(unittest.TestCase):
    def test_preparing_for_work(self):
        print('Проверка, что функция preparing_for_work создает папку folder_test.')
        # создание папки folder_test
        preparing_for_work()
        self.assertIn('folder_test',path_folder_test)

class TestFind_folders_and_files(unittest.TestCase):
    def test_find_folders(self):
        print('Проверка, что функция find_folders_and_files определяет пути папок.')
        folder_name='folder_test'
        file_name=None
        self.assertEqual(find_folders_and_files(folder_name, file_name), path_folder_test)


    def test_find_folders_None(self):
        print('Проверка, что функция find_folders_and_files возвращает None при отсутствии папки.')
        folder_name='folder_test4'
        file_name=None
        self.assertIsNone(find_folders_and_files(folder_name, file_name))


    def test_find_files(self):
        print('Проверка, что функция find_folders_and_files определяет путь файла.')
        file_name = 'test1.txt'
        folder_name='folder_test'
        self.assertEqual(find_folders_and_files(folder_name,file_name),path_test1)


    def test_find_file_None(self):
        print('Проверка,что функция find_folders_and_files возвращает None при отсутствии файла.')
        folder_name='folder_test3'
        file_name='test4.txt'
        self.assertIsNone(find_folders_and_files(folder_name, file_name))
