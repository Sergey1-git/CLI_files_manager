import unittest
import os
from func_cli_files_manager import (preparing_for_work, count_files_recursive,find_folders_and_files, editing_a_path,
                                    delete_folder_and_file, copy_file, search_files_by_criteria)

class TestPreparingForWork(unittest.TestCase):

    def test_preparing_for_work(self):
        print('Проверка, что функция preparing_for_work создает папку folder_test.')
        # создание папки folder_test
        preparing_for_work(editing_a_path())
        self.assertIn('folder_test', os.listdir(editing_a_path()))


class TestFindFoldersAndFiles(unittest.TestCase):

    def test_find_folders(self):
        print('Проверка, что функция find_folders_and_files определяет пути папок.')
        folder_name ='folder_test'
        file_name = None
        path_folder_test = os.path.join(editing_a_path(), 'folder_test')
        self.assertEqual(find_folders_and_files(folder_name, file_name), path_folder_test)


    def test_find_folders_none(self):
        print('Проверка, что функция find_folders_and_files возвращает None при отсутствии папки.')
        folder_name = 'folder_test4'
        file_name = None
        self.assertIsNone(find_folders_and_files(folder_name, file_name))


    def test_find_files(self):
        print('Проверка, что функция find_folders_and_files определяет путь файла.')
        file_name = 'test1.txt'
        folder_name ='folder_test'
        path_folder_test = os.path.join(editing_a_path(), 'folder_test')
        path_test1 = os.path.join(path_folder_test, 'test1.txt')
        self.assertEqual(find_folders_and_files(folder_name,file_name),path_test1)


    def test_find_file_none(self):
        print('Проверка,что функция find_folders_and_files возвращает None при отсутствии файла.')
        folder_name = 'folder_test3'
        file_name = 'test4.txt'
        self.assertIsNone(find_folders_and_files(folder_name, file_name))

class TestCopyfile(unittest.TestCase):
    def test_copy_file(self):
    # 1 исходная папка 'folder_test' копирование в папку 'folder_test'
    # 2 исходная папка 'folder_test' копирование в папку 'folder_test2'
        print('Проверка, что функция copy_file создает копию файла.')
        file_name = 'test1.txt'
        path_folder_test = os.path.join(editing_a_path(), 'folder_test')
        path_folder_test2 = os.path.join(path_folder_test, 'folder_test2')
        copy_file(path_folder_test, file_name, path_folder_test)
        copy_file(path_folder_test, file_name,path_folder_test2)
        self.assertIn(file_name,path_folder_test and file_name,path_folder_test2)

class TestCountfilesRecursive(unittest.TestCase):


    def test_count_files_recursive(self):
    # подсчет файлов в папка 'folder_test'
        print('Проверка, что функция count_files_recursive возвращает количество файлов в папке.')
        path_folder_test = os.path.join(editing_a_path(), 'folder_test')
        total_files = 0
        for root,dirs, files in os.walk(path_folder_test):
            total_files += len(files)
        self.assertEqual(count_files_recursive(path_folder_test),total_files)


class TestDeleteFolderAndFile(unittest.TestCase):


    def test_delete_folder(self):
    # удаляемая папка folder_test3
        print('Проверка, что функция delete_folder_and_file удаляет папку.')
        path_folder_test = os.path.join(editing_a_path(), 'folder_test')
        path_folder_test2 = os.path.join( path_folder_test, 'folder_test2')
        path_folder_test3 = os.path.join(path_folder_test2, 'folder_test3')
        if "folder_test3" not in os.listdir(path_folder_test2):
            os.mkdir(path_folder_test3)
        delete_folder_and_file(path_folder_test2, 'folder_test3')
        self.assertNotIn('folder_test3', os.listdir(path_folder_test2))


    def test_delete_file(self):
    # удаляемая  файл test2.txt в папке folder_test2
        print('Проверка, что функция delete_folder_and_file удаляет файл.')
        path_folder_test = os.path.join( editing_a_path(), 'folder_test')
        path_test2 = os.path.join(path_folder_test, 'test2.txt')
        with open(path_test2, "w") as file:
             file.write("hello world " * 10)
        delete_folder_and_file(path_folder_test,'test2.txt')
        self.assertNotIn('test2.txt', path_folder_test)


class TestSearchFilesByCriteria(unittest.TestCase):

    def test_search_files_by_criteria(self):
    # ищем  файл test3.txt в папке folder_test2
        print('Проверка, что функция search_files_by_criteria находит файл по параметрам.')
        path_folder_test = os.path.join(editing_a_path(), 'folder_test')
        path_folder_test2 = os.path.join(path_folder_test, 'folder_test2')
        path_test3 = os.path.join(path_folder_test2, 'test3.txt')
        with open(path_test3, "w") as file:
             file.write("hello world " * 2000)
        search_files_by_criteria(path_folder_test2,'est','15000')
        self.assertEqual('test3.txt', 'test3.txt')