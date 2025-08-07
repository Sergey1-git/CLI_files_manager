import argparse
import os
import package_clt_files_manager as p_cli_fm
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
            print(p_cli_fm.help_reference(args.operation, args.name1))

        elif args.operation == operation[4]:
            p_cli_fm.preparing_for_work()

        elif os.path.isdir(p_cli_fm.path_folder_test):
            if p_cli_fm.name_verification_for_None(args):
                if args.operation == operation[0]:
                    path_root_folder = p_cli_fm.find_folders_and_files(args.name1, None)
                    path_folder_record = p_cli_fm.find_folders_and_files(args.name3, None)
                    if path_root_folder!=None and os.path.isdir(path_root_folder)==True:
                        if args.name2 in os.listdir(path_root_folder):
                            if path_folder_record !=None and os.path.isdir(path_folder_record)==True:
                                p_cli_fm.copy_file(path_root_folder,args.name2,path_folder_record)
                            else:
                                print(f'Невозможно выполнить копирование файла {args.name2}, папка записи {args.name3} не существует,'
                                      f' либо находится за пределами {os.path.basename(p_cli_fm.path_folder_test)}.')
                        else:
                            print(f'Невозможно выполнить копирование файла {args.name2}, файл отсутствует в папке {args.name1}.')
                    else:
                        print(f'Невозможно выполнить копирование файла {args.name2}, исходная папка {args.name1} не существует,'
                              f' либо находится за пределами {os.path.basename(p_cli_fm.path_folder_test)}.')
            else:
                print(f'Количество введенных аргументов команды {args.operation} не соответствует требуемому синтаксису.')
        else:
            print('Для работы требуется создать папку для тестов. Для создания папки используйте команду "test"')
    else:
        print(f'Ведённая команда {args.operation} не является командой CLI_files_manager. Поддерживаемые команды "help, test, copy, count, delete".')

if __name__ == '__main__':
    parser = parser_cli_file_manager()