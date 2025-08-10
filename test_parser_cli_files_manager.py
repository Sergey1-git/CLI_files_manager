import unittest
import subprocess
import sys
import os
from parser_cli import operation,path_folder_test
operation_test = {0: 'copy', 1: 'count', 2: 'delete', 3: 'help', 4: 'test'}


class TestParserCLI(unittest.TestCase):


    def test_operation_dict(self):
        print('Проверка, что словарь команд соответствует заданным параметрам.')
        self.assertEqual(operation_test, operation)


    def test_operation(self):
        print('Проверка, что вводимая команда не поддерживается CLI_files_manager.')
        test_cases = [
            ('copy', 'Количество введенных аргументов команды copy не соответствует требуемому синтаксису.\n'),
            ('del', 'Ведённая команда del не является командой CLI_files_manager.'
                    ' Поддерживаемые команды "help, test, copy, count, delete".\n'),
        ]
        for expression, result in test_cases:
            with self.subTest(expression=expression):
                cli_result = subprocess.run([sys.executable, 'parser_CLI.py', expression],
                                            capture_output=True, text=True)
                text = cli_result.stdout.encode('windows-1251')
                cli_result = text.decode('utf-8')
                self.assertEqual(result, cli_result)

    def test_operation_copy(self):
        print('Проверка, что при правильном вводе команды copy выводятся соответствующий результат.')
        cli_result = subprocess.run([sys.executable, 'parser_CLI.py', 'copy', 'folder_test', 'test1.txt',
                                     'folder_test2' ],capture_output=True, text=True)
        text=cli_result.stdout.encode('windows-1251')
        cli_result=text.decode('utf-8')
        self.assertEqual('Файл test1.txt успешно скопирован в папку folder_test2.\n' , cli_result)

    def test_operation_copy_false(self):
        print('Проверка, что при вводе ошибочных параметров команды copy выводятся соответствующие уведомления.')
        test_cases = [
            (['folder_test4', 'test1.txt', 'folder_test4'], 'Невозможно выполнить копирование файла test1.txt,'
                        ' исходная папка folder_test4 не существует, либо находится за пределами folder_test.\n'),
            (['folder_test', 'test10.txt', 'folder_test4'], 'Невозможно выполнить копирование файла test10.txt,'
                        ' файл отсутствует в папке folder_test.\n'),
            (['folder_test', 'test1.txt', 'folder_test4'], 'Невозможно выполнить копирование файла test1.txt,'
                      ' папка записи folder_test4 не существует, либо находится за пределами folder_test.\n'),
            (None, 'Количество введенных аргументов команды copy не соответствует требуемому синтаксису.\n')]
        for expression, result in test_cases:
            with self.subTest(expression=expression):
                if expression is not None:
                    cli_result = subprocess.run([sys.executable, 'parser_CLI.py', 'copy', *expression],
                                                capture_output=True, text=True)
                else:
                    cli_result = subprocess.run([sys.executable, 'parser_CLI.py', 'copy'], capture_output=True,
                                                text=True)
                text = cli_result.stdout.encode('windows-1251')
                cli_result = text.decode('utf-8')
                self.assertEqual(result, cli_result)


    def test_operation_count(self):
        print('Проверка, что при правильном вводе команды count выводятся соответствующий результат.')
        total_files = 0
        for root, dirs, files in os.walk(path_folder_test):
            total_files += len(files)
        cli_result = subprocess.run([sys.executable, 'parser_CLI.py', 'count', 'folder_test'], capture_output=True, text=True)
        text=cli_result.stdout.encode('windows-1251')
        cli_result=text.decode('utf-8')
        self.assertEqual(f"Количество файлов в папке folder_test равно {total_files}.\n" , cli_result)


    def test_operation_count_false(self):
        print('Проверка, что при вводе ошибочных параметров команды count выводятся соответствующие уведомления.')
        test_cases = [
            ('folder_test4', 'Невозможно выполнить подсчет файлов в папке folder_test4, папка folder_test4 не существует,'
             ' либо находится за пределами folder_test.\n'),
            (None, 'Количество введенных аргументов команды count не соответствует требуемому синтаксису.\n'),
            ]
        for expression, result in test_cases:
            with self.subTest(expression=expression):
                if expression is not None:
                    cli_result = subprocess.run([sys.executable, 'parser_CLI.py', 'count', expression], capture_output=True, text=True)
                else: cli_result = subprocess.run([sys.executable, 'parser_CLI.py', 'count'], capture_output=True, text=True)
                text = cli_result.stdout.encode('windows-1251')
                cli_result = text.decode('utf-8')
                self.assertEqual(result, cli_result)


    def test_operation_delete(self):
        print('Проверка, что при правильном вводе команды delete выводятся соответствующий результат.')
        path_folder_test2 = os.path.join(path_folder_test, 'folder_test2')
        path_test4 = os.path.join(path_folder_test2, 'test4.txt')
        with open(path_test4, "w") as file:
            file.write("hello world " * 100)
        cli_result = subprocess.run([sys.executable, 'parser_CLI.py', 'delete', 'folder_test2', 'test4.txt'], capture_output=True, text=True)
        text=cli_result.stdout.encode('windows-1251')
        cli_result=text.decode('utf-8')
        self.assertEqual('Файл test4.txt удален из папки folder_test2.\n', cli_result)


    def test_operation_delete_false(self):
        print('Проверка, что при вводе ошибочных параметров команды delete выводятся соответствующие уведомления.')
        test_cases = [
            ('folder_test10',
                'Невозможно выполнить удаление папки, папка folder_test10 не существует,'
                ' либо находится за пределами folder_test.\n'),
            (['folder_test', 'test10.txt'], 'Невозможно выполнить удаление файла test10.txt,'
                         ' файл отсутствует в папке folder_test, либо находится за пределами folder_test.\n'),
            (None, 'Количество введенных аргументов команды delete не соответствует требуемому синтаксису.\n')
        ]
        for expression, result in test_cases:
            with self.subTest(expression = expression):
                if expression is not None:
                    if  isinstance(expression, list):
                        cli_result = subprocess.run([sys.executable, 'parser_CLI.py', 'delete', *expression],
                                                    capture_output = True, text = True)
                    else:
                        cli_result = subprocess.run([sys.executable, 'parser_CLI.py', 'delete', expression],
                                                    capture_output = True, text = True)
                else:
                    cli_result = subprocess.run([sys.executable, 'parser_CLI.py', 'delete'], capture_output=True,
                                                    text=True)
                text = cli_result.stdout.encode('windows-1251')
                cli_result = text.decode('utf-8')
                self.assertEqual(result, cli_result)


    def test_search_files_by_criteria(self):
        print('Проверка, что при правильном вводе команды findfile выводятся соответствующий результат.')
        path_folder_test2 = os.path.join(path_folder_test, "folder_test2")
        path_test3=os.path.join(path_folder_test2, "test3.txt")
        with open(path_test3, "w") as file:
            file.write("hello world " * 2000)
        cli_result = subprocess.run([sys.executable, 'parser_cli.py', 'findfile', 'folder_test2', 'est', '15000','25000'], capture_output=True, text=True)
        text = cli_result.stdout.encode('windows-1251')
        cli_result = text.decode('utf-8')
        self.assertEqual('Файлы подпадающие под выбранные условия расположены в следующих папках:\n''Папка folder_test2 файлы: test3.txt\n' , cli_result)