import argparse
import os
operation={0: 'copy', 1: 'count', 2: 'delete',3: 'help', 4: 'test'}

def parser_cli_file_manager():
    parser = argparse.ArgumentParser(
                    prog='CLI_files_manager',
                    description='Файловый менеджер')

    parser.add_argument('operation',type=str)  # positional argument
    parser.add_argument('name1',type=str, nargs='?', default=None)    # positional argument folder
    parser.add_argument('name2',type=str, nargs='?', default=None)  # positional argument
    parser.add_argument('name3',type=str, nargs='?', default=None)  # positional argument
    args = parser.parse_args()

if __name__ == '__main__':
    parser = parser_cli_file_manager()