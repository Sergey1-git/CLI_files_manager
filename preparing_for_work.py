import os
def preparing_for_work():
    print('Подготовка к работе создание папки для тестирования')
    if "Folder_test" in os.listdir(os.getcwd()):
        print("Папка Folder_test уже создана")
    else:
        print("Создание  тестовой папки Folder_test")
        os.mkdir("Folder_test")
        path_folder_test = os.path.join(os.getcwd(), "Folder_test")
        path_test1 = os.path.join(path_folder_test, "test1.txt")
        path_test2 = os.path.join(path_folder_test, "test2.txt")
        path_folder_test2 = os.path.join(path_folder_test, "Folder_test2")
        open(path_test1, "w")
        open(path_test2, "w")
        if "Folder_test2" in os.listdir(path_folder_test):
            print("Папка Folder_test уже создана")
        else:
            os.mkdir(path_folder_test2)
        path_test3 = os.path.join(path_folder_test2, "test3.txt")
        open(path_test3, "w")
        with open(path_test3, "w") as file:
            file.write("hello world"*1000)
        print(f"Файл {os.path.basename(path_test3)} записан")