import unittest
import os
from func_cli_files_manager import preparing_for_work, count_files_recursive,find_folders_and_files
#from CLI_files_manager.parser_cli import  path_folder_test
class TestPreparing_for_work(unittest.TestCase):
    def test_preparing_for_work(self):
        print('Проверка, что функция preparing_for_work создает папку folder_test.')
        # создание папки folder_test
        path_folder_test = os.getcwd()
        print('@@@',path_folder_test)
        #absolute_path = os.path.abspath('CLI_files_manager/folder_testh')
        if 'package_cli_files_manager' in path_folder_test:
            folder_test=path_folder_test.replace('\\package_cli_files_manager','')
            #folder_test = path_folder_test.replace('', '')
            print('@@@##',folder_test)
        else:
            folder_test=path_folder_test
        preparing_for_work(folder_test)
        print('@@@##AAA', folder_test)
        #self.assertTrue(os.path.exists(folder_test))
        self.assertIn('folder_test', os.listdir(folder_test))

class TestFind_Folders_And_Files(unittest.TestCase):
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

class TestCount_files_recursive(unittest.TestCase):
    def test_count_files_recursive(self):
    # подсчет файлов в папка 'folder_test'
        print('Проверка, что функция count_files_recursive возвращает количество файлов в папке.')
        total_files = 0
        for root,dirs, files in os.walk(path_folder_test):
            total_files+=len(files)
        self.assertEqual(count_files_recursive(path_folder_test),total_files)
