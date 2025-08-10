from shutil import rmtree, copy
import os
import re

# функция создания тестовой папки
def preparing_for_work(path_folder):

    # пути для создания папок и файлов
    path_folder_test = os.path.join(path_folder, "folder_test")
    if "folder_test" not in os.listdir(path_folder):
        os.mkdir(path_folder_test)
    path_test1 = os.path.join(path_folder_test, "test1.txt")
    path_test2 = os.path.join(path_folder_test, "test2.txt")
    path_folder_test2 = os.path.join(path_folder_test, "folder_test2")
    path_test3 = os.path.join(path_folder_test2, "test3.txt")
    path_test4 = os.path.join(path_folder_test2, "test4.txt")
    path_folder_test3 = os.path.join(path_folder_test2, "folder_test3")
    print('Подготовка к работе, создание папки для тестирования.')

    with open(path_test1, "w") as file:
        file.write("hello world " * 10)
    with open(path_test2, "w") as file:
        file.write("hello world " * 10)
    if "folder_test2" not in os.listdir(path_folder_test):
        os.mkdir(path_folder_test2)
    with open(path_test3, "w") as file:
        file.write("hello world " * 1000)
    with open(path_test4, "w") as file:
        file.write("hello world " * 100)
    print('Папка для тестирования "folder_test" создана.')
    if "folder_test3" not in os.listdir(path_folder_test2):
        os.mkdir(path_folder_test3)

# функция справочной системы
def help_reference(name2=None):
    comande_dict = {
        'copy': 'ввод команды copy - "copy" "наименование исходной папки", "наименование копируемого файла",'
                ' "наименование папки записи"',
        'count': 'ввод команды count - "count" "наименование исходной папки',
        'delete': 'ввод команды delete - "delete" "наименование удаляемой папки", либо "delete" "наименование исходной'
                  ' папки", "наименование удаляемого файла"',
        'help': 'ввод команды help - "help" "наименование команды"', 'test': 'ввод команды test - "test"'}
    if name2 is None:
        string=('Команды используемые при работе с CLI_files_manager:\n"help"- выводит справочную информацию.\n"copy"-'
                ' осуществляет копирование файлов.\n'+
                '"test"- создает либо восстанавливает тестовую папку folder_test.\n'+
                '"count"- подсчитывает колличество файлов в указанной папке, включая папки вложенные.\n' +
                '"delete"- удаляет указанный файл или папку.\nБолее подробную информацию по конкретной команде'
                ' можно получить выполнив "help" "наменование команды".\n' +
                'Перед использованием CLI_files_manager необходимо создать тестовую папку с помощью команды "test".\n')
        return string
    else:
        if name2 in comande_dict.keys():
            return comande_dict[name2]
        else:
            string=(f'Ведённая команда {name2} не является командой CLI_files_manager. Поддерживаемые команды'
                    f' "copy, count, delete, help"')
            return string

# функция определения путей папок и файлов
def find_folders_and_files(folder_name, file_name):
    list_path = []
    for root, dirs, files in os.walk(editing_a_path()):
        if folder_name in dirs:
            if file_name is None:
                path_folder = os.path.join(root, folder_name)
                list_path.append(path_folder)
            else:
                path_folder = os.path.join(root, folder_name)
                if file_name in os.listdir(path_folder):
                    path_file_name = os.path.join(path_folder, file_name)
                    list_path.append(path_file_name)
    if len(list_path) == 1:
        return list_path[0]
    elif len(list_path) > 1:
        print('Найдено несколько подходящих объектов.', *list_path)
        while True:
            path=input('Ведите необходимый вам путь ')
            if path in list_path:
                return path
            else:
                print('Вы ввели не верный  путь, попробуйте снова.')
    else:
        return None


# функция определения корректного ввода аргументов команд
def name_verification_for_none(args):
    if args.operation=='copy' and args.name1 is not None and args.name2 is not None and args.name3 is not None:
        return True
    elif args.operation =='count' and args.name1 is not None:
        return True
    elif args.operation == 'delete' and args.name1 is not None:
        return True
    elif args.operation == 'findfile' and args.name1 is not None and args.name2 is not None:
        return True
    else:
        return False

# функция копирования фалов
def copy_file(path_root_folder,file_name,path_folder_record):
    path_file_name = os.path.join(path_root_folder,file_name)
    path_file_name_copy = os.path.join(path_folder_record,file_name)
    if path_file_name_copy == path_file_name:
        name = file_name
        name_parts = name.partition(".")
        name = f'{name_parts[0]}_копия{name_parts[1]}{name_parts[2]}'
        path_file_name_copy = os.path.join(path_folder_record, name)
        copy(path_file_name, path_file_name_copy)
        print(f"Файл {file_name} успешно скопирован в папку {os.path.basename(path_root_folder)} как {name}.")
    else:
        copy(path_file_name, path_file_name_copy)
        print(f"Файл {file_name} успешно скопирован в папку {os.path.basename(path_folder_record)}.")


# функция рекурсивного подсчета файлов в папке
def count_files_recursive(path_folder):
    total_files = 0
    for item in os.scandir(path_folder):
        item_path = os.path.join(path_folder, item)
        if os.path.isfile(item_path):
            total_files += 1
        elif os.path.isdir(item_path) and len(os.listdir(item_path)) != 0:
            total_files += count_files_recursive(item_path)
    return total_files


# функция удаления папок и файлов
def delete_folder_and_file(path_folder, file = None):
    path_folder_test = os.path.join(editing_a_path(), "folder_test")
    if path_folder_test in path_folder:
        if file is None:
            path_delete = path_folder
        else:
            path_delete = os.path.join(path_folder, file)
        if os.path.isfile(path_delete):
            os.remove(path_delete)
            print(f'Файл {file} удален из папки {os.path.basename(path_folder)}.')
        elif os.path.isdir(path_delete):
            rmtree(path_delete) #os.rmdir(path_delete)
            print(f'Папка {os.path.basename(path_folder)} удалена.')
    else:
        print(f'Невозможно выполнить удаление, так как объект не относится к директории {os.path.basename(path_folder_test)}.')

def search_files_by_criteria(path_folder, pattern, size1=None,size2=None):
    dict={}
    for root, dirs, files in os.walk(path_folder):
        lf = []
        for file in files:
            if re.search(pattern, file) and size1 is None and size2 is None:
                lf.append(file)
            elif re.search(pattern, file) and size1 is not None and size2 is None:
                if os.path.getsize(os.path.join(root, file)) >= int(size1):
                    lf.append(file)
            elif re.search(pattern, file) and size1 is not None and size2 is not None:
                if int(size1)<=os.path.getsize(os.path.join(root,file))<=int(size2):
                    lf.append(file)
        if len(lf)!=0:
            dict[root]=lf
    if len(dict) == 0:
        print('Файлы подпадающие под выбранные условия не найдены.')
    else:

        print('Файлы подпадающие под выбранные условия расположены в следующих папках:')
        for i in dict:
            txt = ','.join(dict[i])
            print(f'Папка {os.path.basename(i)} файлы: {txt}')


def editing_a_path():
    path_folder_test = os.getcwd()
    if 'package_cli_files_manager' in path_folder_test:
        folder_test = path_folder_test.replace('\\package_cli_files_manager', '')
        return folder_test
    else:
        folder_test = path_folder_test
        return folder_test