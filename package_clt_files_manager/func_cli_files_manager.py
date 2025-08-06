import shutil
import os

# пути для создания папок и файлов, а так же их импорта
path_folder_test = os.path.join(os.getcwd(), "folder_test")
path_test1 = os.path.join(path_folder_test, "test1.txt")
path_test2 = os.path.join(path_folder_test, "test2.txt")
path_folder_test2 = os.path.join(path_folder_test, "folder_test2")
path_test3 = os.path.join(path_folder_test2, "test3.txt")
path_test4 = os.path.join(path_folder_test2, "test4.txt")
path_folder_test3 = os.path.join(path_folder_test2, "folder_test3")

# функция создания тестовой папки
def preparing_for_work():
    print('Подготовка к работе, создание папки для тестирования.')
    if "folder_test" not in os.listdir(os.getcwd()):
        os.mkdir("folder_test")
    with open(path_test1, "w") as file:
        file.write("hello world " * 10)
    with open(path_test2, "w") as file:
        file.write("hello world " * 10)
    if "folder_test2" not in os.listdir(path_folder_test):
        os.mkdir(path_folder_test2)
    open(path_test3, "w")
    with open(path_test3, "w") as file:
        file.write("hello world " * 1000)
    open(path_test4, "w")
    with open(path_test4, "w") as file:
        file.write("hello world " * 100)
    print('Папка для тестирования "folder_test" создана.')
    if "folder_test3" not in os.listdir(path_folder_test2):
        os.mkdir(path_folder_test3)

# функция справочной системы
def help_reference(name1, name2=None):
    comande_dict = {
        'copy': 'ввод команды copy - "copy" "наименование исходной папки", "наименование копируемого файла", "наименование папки записи"',
        'count': 'ввод команды count - "count" "наименование исходной папки',
        'delete': 'ввод команды delete - "delete" "наименование удаляемой папки", либо "delete" "наименование исходной папки", "наименование удаляемого файла"',
        'help': 'ввод команды help - "help" "наименование команды"', 'test': 'ввод команды test - "test"'}
    if name2==None:
        string=('Команды используемые при работе с CLI_files_manager:\n"help"- выводит справочную информацию.\n"copy"- осуществляет копирование файлов.\n'+
                '"test"- создает либо восстанавливает тестовую папку folder_test.\n'+
                '"count"- подсчитывает колличество файлов в указанной папке, включая папки вложенные.\n' +
                '"delete"- удаляет указанный файл или папку.\nБолее подробную информацию по конкретной команде можно получить выполнив "help" "наменование команды".\n' +
                'Перед использованием CLI_files_manager необходимо создать тестовую папку с помощью команды "test".\n')
        return string
    else:
        if name2 in comande_dict.keys():
            return comande_dict[name2]
        else:
            string=f'Ведённая команда {name2} не является командой CLI_files_manager. Поддерживаемые команды "copy, count, delete, help"'
            return string