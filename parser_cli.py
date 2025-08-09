import argparse
import os
import package_cli_files_manager as p_cli_fm
operation={0: 'copy', 1: 'count', 2: 'delete',3: 'help', 4: 'test'}
path_folder_test=os.path.join(os.getcwd(), "folder_test")


def parser_cli_file_manager():
    parser = argparse.ArgumentParser(
                    prog='CLI_files_manager',
                    description='Файловый менеджер')

    parser.add_argument('operation',type=str)
    parser.add_argument('name1',type=str, nargs='?', default=None)
    parser.add_argument('name2',type=str, nargs='?', default=None)
    parser.add_argument('name3',type=str, nargs='?', default=None)
    args = parser.parse_args()

    path_folder = os.getcwd()
    if args.operation in operation.values():
        if args.operation == operation[3]:
            print(p_cli_fm.help_reference(args.name1))
        elif args.operation == operation[4]:
            p_cli_fm.preparing_for_work(path_folder)

        elif os.path.isdir(path_folder_test):
            if p_cli_fm.name_verification_for_none(args):

                if args.operation == operation[0]:
                    path_root_folder = p_cli_fm.find_folders_and_files(args.name1, None)
                    path_folder_record = p_cli_fm.find_folders_and_files(args.name3, None)
                    if path_root_folder is not None and os.path.isdir(path_root_folder)==True:
                        if args.name2 in os.listdir(path_root_folder):
                            if path_folder_record is not None and os.path.isdir(path_folder_record)==True:
                                p_cli_fm.copy_file(path_root_folder,args.name2,path_folder_record)
                            else:
                                print(f'Невозможно выполнить копирование файла {args.name2}, папка записи {args.name3} '
                                      f'не существует, либо находится за пределами {os.path.basename(path_folder_test)}.')
                        else:
                            print(f'Невозможно выполнить копирование файла {args.name2}, файл отсутствует в папке {args.name1}.')
                    else:
                        print(f'Невозможно выполнить копирование файла {args.name2}, исходная папка {args.name1} не существует,'
                              f' либо находится за пределами {os.path.basename(path_folder_test)}.')

                elif args.operation == operation[1]:
                    path_folder = p_cli_fm.find_folders_and_files(args.name1, None)
                    if path_folder is not None and os.path.isdir(path_folder) == True:
                        number = p_cli_fm.count_files_recursive(path_folder)
                        print(f'Количество файлов в папке {args.name1} равно {number}.')
                    else:
                        print(f'Невозможно выполнить подсчет файлов в папке {args.name1}, папка {args.name1} не существует,'
                              f' либо находится за пределами {os.path.basename(path_folder_test)}.')

                elif args.operation == operation[2]:
                    path_folder= p_cli_fm.find_folders_and_files(args.name1, None)
                    if path_folder is not None and os.path.isdir(path_folder) == True:
                        if args.name2 is not None:
                            if args.name2 in os.listdir(path_folder):
                                 p_cli_fm.delete_folder_and_file(path_folder,args.name2)
                            else:
                                print(f'Невозможно выполнить удаление файла {args.name2}, файл отсутствует в папке'
                                      f' {args.name1}, либо находится за пределами {os.path.basename(path_folder_test)}.')
                        else:
                            p_cli_fm.delete_folder_and_file(path_folder)
                    else:
                        print(f'Невозможно выполнить удаление папки, папка {args.name1} не существует, либо находится'
                              f' за пределами {os.path.basename(path_folder_test)}.')
            else:
                print(f'Количество введенных аргументов команды {args.operation} не соответствует требуемому синтаксису.')
        else:
            print('Для работы требуется создать папку для тестов. Для создания папки используйте команду "test"')
    else:
        print(f'Ведённая команда {args.operation} не является командой CLI_files_manager. Поддерживаемые команды'
              f' "help, test, copy, count, delete".')

if __name__ == '__main__':
    parser_cli_file_manager()