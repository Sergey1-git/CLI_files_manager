import unittest
import subprocess
import sys

class TestParser_CLI(unittest.TestCase):

    def test_operation_copy(self):
        print('Проверка, что при правильном вводе команды copy выводятся соответствующий результат.')
        cli_result = subprocess.run([sys.executable, 'parser_CLI.py', 'copy', 'folder_test', 'test1.txt','folder_test2' ],
                                    capture_output=True, text=True)
        text=cli_result.stdout.encode('windows-1251')
        cli_result=text.decode('utf-8')
        self.assertEqual('Файл test1.txt успешно скопирован в папку folder_test2.\n' , cli_result)


    def test_operation_copy_false(self):
        print('Проверка, что при вводе ошибочных параметров команды copy выводятся соответствующие уведомления.')
        test_cases = [
            (['folder_test4', 'test1.txt', 'folder_test4'], 'Невозможно выполнить копирование файла test1.txt,'
                                                            ' исходная папка folder_test4 не существует, либо находится'
                                                            ' за пределами folder_test.\n'),
            (['folder_test', 'test10.txt', 'folder_test4'], 'Невозможно выполнить копирование файла test10.txt,'
                                                            ' файл отсутствует в папке folder_test.\n'),
            (['folder_test', 'test1.txt', 'folder_test4'], 'Невозможно выполнить копирование файла test1.txt,'
                                                           ' папка записи folder_test4 не существует, либо находится'
                                                           ' за пределами folder_test.\n'),
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