import argparse
import os
from package_clt_files_manager.func_cli_files_manager import preparing_for_work, help_reference
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

    if args.operation in operation.values():
        if args.operation == operation[3]:
            print(help_reference(args.operation, args.name1))

        elif args.operation == operation[4]:
            preparing_for_work()
    else:
        print(f'Ведённая команда {args.operation} не является командой CLI_files_manager. Поддерживаемые команды "help, test, copy, count, delete".')

if __name__ == '__main__':
    parser = parser_cli_file_manager()