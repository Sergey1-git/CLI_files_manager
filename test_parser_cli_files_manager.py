import unittest
import subprocess
import sys

class TestParser_CLI(unittest.TestCase):

    def test_operation_copy(self):
        print('Проверка, что при правильном вводе команды copy выводятся соответствующий результат.')
        cli_result = subprocess.run([sys.executable, 'parser_CLI.py', 'copy', 'folder_test', 'test1.txt','folder_test2' ], capture_output=True, text=True)
        text=cli_result.stdout.encode('windows-1251')
        cli_result=text.decode('utf-8')
        self.assertEqual('Файл test1.txt успешно скопирован в папку folder_test2.\n' , cli_result)