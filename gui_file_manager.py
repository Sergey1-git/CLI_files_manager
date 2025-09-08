import flet as ft
from flet import ElevatedButton, FilePicker, FilePickerResultEvent, Page, Row, Text,Icons
import os
import package_cli_files_manager as p_cli_fm


current_dialog=[]

def main(page: ft.Page):
    # Ссылки на  виджеты.
    appbar_text_ref = ft.Ref[ft.Text]()
    my_text_ref = ft.Ref[ft.Text]()
    my_copy_ref = ft.Ref[ft.Text]()
    my_copy_path_ref = ft.Ref[ft.Text]()
    my_count_ref = ft.Ref[ft.Text]()
    my_delete_path_ref = ft.Ref[ft.Text]()
    my_delete_folder_ref = ft.Ref[ft.Text]()
    my_find_file_ref = ft.Ref[ft.Text]()
    my_find_file_folder_ref = ft.Ref[ft.Text]()
    my_find_file_name_ref = ft.Ref[ft.Text]()
    my_find_bytes1_ref = ft.Ref[ft.Text]()
    my_find_bytes2_ref = ft.Ref[ft.Text]()

    def handle_menu_item_click(e):
        print(f"{e.control.content.value}.on_click")
        page.open(
            ft.SnackBar(content=ft.Text(f"{e.control.content.value} was clicked!"))
        )
        appbar_text_ref.current.value = e.control.content.value
        # Условия очистки volue виджета с результатом при нажатии кнопок "Выбор файла" или "Выбор папки".
        if len(current_dialog) != 0:
            if e.control.content.value=="Выбор файла" and current_dialog[0]=='dlg_copy':
                my_copy_ref.current.value = ''
                dlg_copy.update()
            if e.control.content.value == "Выбор папки" and current_dialog[0]=='dlg_copy':
                my_copy_ref.current.value = ''
                dlg_copy.update()
            if e.control.content.value=="Выбор папки" and  current_dialog[0]=='dlg_count':
                my_count_ref.current.value = ''
                dlg_count.update()
            if e.control.content.value=="Выбор файла" and  current_dialog[0]=='dlg_delete_file':
                my_delete_path_ref.current.value = ''
                dlg_delete_file.update()
            if e.control.content.value=="Выбор папки" and  current_dialog[0]=='dlg_delete_folder':
                my_delete_folder_ref.current.value = ''
                dlg_delete_folder.update()
            if e.control.content.value == "Выбор папки" and current_dialog[0]=='dlg_find_file':
                my_find_file_ref.current.value = ''
                dlg_find_file.update()

        page.update()

    # Функция выбора файла при нажатии кнопки "Выбор файла".
    def pick_files_result(e: ft.FilePickerResultEvent):

        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Не выбрано"
        )
        selected_files.update()
        if current_dialog[0]=='dlg_copy':
            my_copy_path_ref.current.value=e.files[0].path if e.files else ""
            my_copy_path_ref.current.update()
        if current_dialog[0]=='dlg_delete_file':
            my_delete_path_ref.current.value=e.files[0].path if e.files else ""
            my_delete_path_ref.current.update()

    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)
    selected_files = ft.Text('')
    page.overlay.append(pick_files_dialog)


    # Функция выбора папки при нажатии кнопки "Выбор папки".
    def get_directory_result(e: FilePickerResultEvent):
        directory_path.value = e.path if e.path else "Не выбрано"
        directory_path.update()

    get_directory_dialog = FilePicker(on_result=get_directory_result)
    directory_path = Text('')
    page.overlay.append( get_directory_dialog)

    # Функция open_dialog фиксирует какое диалоговое окно открыто и очищает volue виджета диалогового окгна при открытии.
    def open_dialog(dialog):
        active_dialog=dialog
        if len(current_dialog)==0:
            current_dialog.append(active_dialog)
        else:
            current_dialog[0]=active_dialog
        print(active_dialog)
        if active_dialog=='dlg_copy':
            my_copy_ref.current.value=''
            my_copy_path_ref.current.value=''
            dlg_copy.update()
        if active_dialog=='dlg_count':
            my_count_ref.current.value=''
            dlg_count.update()
        if active_dialog=='dlg_delete_file':
            my_delete_path_ref.current.value=''
            dlg_delete_file.update()
        if active_dialog=='dlg_delete_folder':
            my_delete_folder_ref.current.value=''
            dlg_delete_folder.update()
        if active_dialog=='dlg_find_file':
            my_find_file_ref.current.value=''
            my_find_file_name_ref.current.value = ''
            my_find_bytes1_ref.current.value = ''
            my_find_bytes2_ref.current.value = ''
            dlg_find_file.update()
        if selected_files.value!='':
            selected_files.value = ''
            selected_files.update()
        if directory_path.value!='':
            directory_path.value = ''
            directory_path.update()

    # Функция вывода Help информации.
    def print_help(e):
        handle_menu_item_click(e)
        my_dict = {
            'general_information': (
                'Команды используемые при работе с CLI_files_manager:\n"help"- выводит справочную информацию.\n'+
                '"test"- создает либо восстанавливает тестовую папку folder_test.\n' +
                '"copy"- осуществляет копирование файлов.\n' +
                '"count"- подсчитывает колличество файлов в указанной папке, включая папки вложенные.\n' +
                '"delete"- удаляет указанный файл или папку.\n'
                '"find_file"-осуществляет поиск файла по параметрам.\n'+
                'Более подробную информацию по конкретной команде можно получить нажав на кнопку "Help" и в раскрывшемся'
                ' подменю выбрать интересующую команду.\n' +
                'Перед использованием CLI_files_manager необходимо создать тестовую папку с помощью команды "Test".\n'),
            'Help_test': (
                'Для выполнения команды нажмите кнопку "Test" и подтвердите выполнение действия в открывшемся'
                ' окне.\n' + 'В случае подтверждения произоойдет создание тестовой папки "folder_test".'),
            'Help_copy': (
                'Для выполнения команды нажмите кнопку "Copy_file".\n'
                +'В открывшемся окне нажмите кнопку "Выбора файла", и выберите файл который хотите скопировать.\n'
                +'Затем нажатием кнопки "Выбор папки" выберите папку в которую хотите скопировать выбранный файл,\n'
                'и нажатием кнопки "Выполнить копирование" осуществите копирование файла.\n'+
                'После завершения копирования файла нажатием кнопки "Закрыть окно" закройте окно.'),
            'Help_count': (
                    'Для выполнения команды нажмите кнопку "Count".\n'
                    + 'В открывшемся окне нажмите кнопку "Выбора папки" и выберите папку в которой необходимо'
                      ' посчитать количество файлов.\n'
                    + 'Затем нажатием кнопки "Выполнить подсчет" осуществите подсчет файлов в выбранной папке.\n'
                    + 'После завершения подсчета закройте окно нажатием кнопки "Закрыть окно".'),
            'Help_delete_file': (
                'Для выполнения команды нажмите кнопку "Delete", а затем в открывшемся меню нажмите кнопку'
                ' "delete_file".\n'
                + 'В открывшемся окне нажмите кнопку "Выбора файла", и выберети файл который хотите удалить.\n'
                + 'Затем нажатием кнопки "Выполнить удаление" осуществите удаление выбранного файла.\n'
                + 'После завершения удаления файла закройте окно нажатием кнопки "Закрыть окно"'),
            'Help_delete_folder': (
                'Для выполнения команды нажмите кнопку "Delete", а затем в открывшемся меню нажмите кнопку'
                ' "delete_folder".\n'
                + 'В открывшемся окне нажмите кнопку "Выбора папки", и выберите папку  которую хотите удалить.\n'
                + 'Затем нажатием кнопки "Выполнить удаление" осуществите удаление выбранной папки.\n'
                + 'После завершения удаления папки закройте окно нажатием кнопки "Закрыть окно".'),
            'Help_findfile': (
                'Для выполнения команды нажмите кнопку "Findfile".\n'
            + 'В открывшемся окне нажмите кнопку "Выбора папки",и выберите папку где будет выполнен поиск файла(ов).\n'
                +'В поля запроса наименования файла и его размера (в байтах) введите наобходимые данные.\n'
                + 'Затем нажатием кнопки "Выполнить поиск" осуществите поиск файла(ов).\n'
                + 'После завершения удаления папки закройте окно нажатием кнопки "Закрыть окно".'),
        }
        for i in page.controls:
            if isinstance(i,ft.core.text.Text):
                del page.controls[1]
            else:
                page.add(ft.Text(ref = my_text_ref, value = my_dict[e.control.content.value]))

    page.appbar = ft.AppBar(
        title=ft.Text("Поле отображения нажатого виджета", ref=appbar_text_ref),
        center_title=True,
        bgcolor=ft.Colors.ORANGE_100,
    )

    menubar = ft.MenuBar(
        expand=True,
        style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            bgcolor=ft.Colors.BLUE_300,
            mouse_cursor={
                ft.ControlState.HOVERED: ft.MouseCursor.WAIT,
                ft.ControlState.DEFAULT: ft.MouseCursor.ZOOM_OUT,
            },
        ),
        controls=[
            ft.SubmenuButton(
                content=ft.Text("Help"),
                style=ft.ButtonStyle(
                    alignment=ft.alignment.center_right),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("general_information"),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                        on_click=print_help,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Help_test"),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                        on_click=print_help,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Help_copy"),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                        on_click=print_help,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Help_count"),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                        on_click=print_help,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Help_delete_file"),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                        on_click=print_help,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Help_delete_folder"),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                        on_click=print_help,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Help_findfile"),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                        on_click=print_help,
                    ),
                ],
            ),
            ft.MenuItemButton(
                content=ft.Text("Test"),
                on_click=lambda e: (page.open(dlg_test), handle_menu_item_click(e))),
            ft.MenuItemButton(
                content=ft.Text("Copy_file"),
                on_click=lambda e: (page.open(dlg_copy), open_dialog('dlg_copy'), handle_menu_item_click(e))),
            ft.MenuItemButton(
                content=ft.Text("Count"),
                on_click=lambda e: (page.open(dlg_count), open_dialog('dlg_count'), handle_menu_item_click(e))),
            ft.SubmenuButton(
                content=ft.Text("Delete"),
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Delete_file"),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                        on_click=lambda e: (page.open(dlg_delete_file), open_dialog('dlg_delete_file'),
                                            handle_menu_item_click(e)),
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Delete_folder"),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                        on_click=lambda e: (page.open(dlg_delete_folder), open_dialog('dlg_delete_folder'),
                                            handle_menu_item_click(e)),
                    ),
                ],
            ),
            ft.MenuItemButton(
                content=ft.Text("Find_file"),
                on_click=lambda e: (page.open(dlg_find_file), open_dialog('dlg_find_file'), handle_menu_item_click(e)))
        ],
    )
    page.add(ft.Row([menubar]))


    # Функция copy_result проверяет корректность ввода данных и формирует полученный результат.
    def copy_result(path_root_folder,file_name,path_folder_record):
        print(path_root_folder,file_name,path_folder_record)
        path_folder_file = os.path.split(path_root_folder)[0]
        if file_name=="Не выбрано" or file_name=="":
            my_copy_ref.current.value = f"Не выбран файл, повторите выбор"
        elif path_folder_record == "Не выбрано" or path_folder_record == "":
            my_copy_ref.current.value = f"Не выбрана папка, повторите выбор"
        else:
            p_cli_fm.copy_file(path_folder_file,file_name,path_folder_record)
            my_copy_ref.current.value = f"Файл {file_name} успешно скопирован."
        dlg_copy.update()


    # Функция count_result проверяет корректность ввода данных и формирует полученный результат.
    def count_result(path_folder_count):
        print(path_folder_count)
        if path_folder_count == "Не выбрано" or path_folder_count=="":
            my_count_ref.current.value = str(f"Не выбрана папка, повторите выбор")
        else:
            my_count_ref.current.value = str(f"Количество файлов равно {p_cli_fm.count_files_recursive(path_folder_count)}.")
        dlg_count.update()

    # Функция delete_file_result проверяет корректность ввода данных и формирует полученный результат.
    def delete_file_result(file_name, path_file):
        path_folder_file=os.path.split(path_file)[0]
        if file_name == "Не выбрано" or file_name == "":
            my_delete_path_ref.current.value = f"Не выбран файл, повторите выбор"
        else:
            p_cli_fm.delete_folder_and_file(path_folder_file, file_name)
            my_delete_path_ref.current.value = f"Файл {file_name} успешно удален."
        dlg_delete_file.update()

    # Функция delete_folder_result проверяет корректность ввода данных и формирует полученный результат.
    def delete_folder_result(path_folder_delete):
        if path_folder_delete == "Не выбрано" or path_folder_delete == "":
            my_delete_folder_ref.current.value = f"Папка не выбрана, повторите выбор"
        else:
            p_cli_fm.delete_folder_and_file(path_folder_delete)
            folder_name = os.path.split(path_folder_delete)[1]
            my_delete_folder_ref.current.value = f"Папка {folder_name} успешно удалена."
        dlg_delete_folder.update()

    # Функция find_file_result проверяет корректность ввода данных и формирует полученный результат.
    def find_file_result(path_find_folder, file_name, bytes1,bytes2):
        result=[]
        if path_find_folder == "Не выбрано" or path_find_folder == "":
            my_find_file_ref.current.value = f"Папка не выбрана, повторите выбор"
        elif my_find_file_name_ref.current.value == "":
            my_find_file_ref.current.value = f"Имя файла не введено, повторите ввод"
        elif bytes1 =='' and bytes2 != '':
            my_find_file_ref.current.value = f"Перенесите ввдеденные данные о размере файла на одно поле выше"
        elif  bytes1 != '' and bytes1.isdigit() is False:
            my_find_file_ref.current.value=(f"При указании размера файла были введены символы\n"+
                                            "не являющиеся цифрами, повторите ввод")
        elif  bytes2 != '' and bytes2.isdigit() is False:
            my_find_file_ref.current.value=(f"При указании размера файла были введены символы\n"+
                                            "не являющиеся цифрами, повторите ввод")
        else:
            if bytes1 == '':
               result=p_cli_fm.search_files_by_criteria(path_find_folder, file_name)
            elif bytes1 != '' and bytes2 == '':
                result=p_cli_fm.search_files_by_criteria(path_find_folder, file_name, int(bytes1))
            elif bytes1 != '' and bytes2 != '':
                result=p_cli_fm.search_files_by_criteria(path_find_folder, file_name,int(bytes1),int(bytes2))
            if len(result) == 0:
               my_find_file_ref.current.value='Файлы подпадающие под выбранные условия не найдены.'
            else:
                s=''
                for i in result:
                    txt = ', '.join(result[i])
                    s1 = f'Папка {os.path.basename(i)} файлы: {txt}.\n'
                    s=s+s1
                my_find_file_ref.current.value = ("Файлы подпадающие под выбранные условия расположены в следующих"
                                                  " папках:\n") + s
        dlg_find_file.update()

    # Диалоговые окна
    dlg_test = ft.AlertDialog(
        modal=True,
        title=ft.Text("Пожалуйста, подтвердите выбранное действие"),
        content=ft.Text("Вы действительно хотите создать папку для тестов ?"),
        actions=[
            ft.TextButton("Выполнить", on_click=lambda e: (p_cli_fm.preparing_for_work(os.getcwd()), page.close(dlg_test))),
            ft.TextButton("Отменить", on_click=lambda e: page.close(dlg_test)),
        ],
    )

    dlg_copy = ft.AlertDialog(
        modal=True,
        title=ft.Text("Копирование файла в указанную папку."),
        content=ft.Text("Выберите файл и папку для копирования."),
        actions=[
            ft.Row([ft.TextButton("Выбор файла", content=ft.Text("Выбор файла"), on_click=lambda e:
            (pick_files_dialog.pick_files(allow_multiple=True), handle_menu_item_click(e))), selected_files,
                    ft.Text(ref=my_copy_path_ref, value='')]),
            ft.Row([ft.TextButton("Выбор папки", content=ft.Text("Выбор папки"), on_click=lambda e:
            (get_directory_dialog.get_directory_path(), handle_menu_item_click(e))), directory_path]),
            ft.Row([ft.TextButton("Выполнить копирование", on_click=lambda e:
            copy_result(my_copy_path_ref.current.value, selected_files.value, directory_path.value)),
                    ft.Text(ref=my_copy_ref, value='')]),
            ft.TextButton("Закрыть окно", on_click=lambda e: page.close(dlg_copy)),
        ],
    )
    dlg_count = ft.AlertDialog(
        modal=True,
        title=ft.Text("Выполнить подсчет колличества файлов в выбранной папке."),
        content=ft.Text("Выберите папку в которой хотите посчитать количество файлов."),
        actions=[
            ft.Row([ft.TextButton("Выбор папки", content=ft.Text("Выбор папки"), on_click=lambda e:
            (get_directory_dialog.get_directory_path(), handle_menu_item_click(e))), directory_path]),
            ft.Row([ft.TextButton("Выполнить подсчет", on_click=lambda e: count_result(directory_path.value)),
                    ft.Text(ref=my_count_ref, value='')]),
            ft.TextButton("Закрыть окно", on_click=lambda e: page.close(dlg_count)),
        ],
    )
    dlg_delete_file = ft.AlertDialog(
        modal=True,
        title=ft.Text("Удаление файла."),
        content=ft.Text("Выберите файл который хотите удалить."),
        actions=[
            ft.Row([ft.TextButton("Выбор файла", content=ft.Text("Выбор файла"), on_click=lambda e:
            (pick_files_dialog.pick_files(allow_multiple=True), handle_menu_item_click(e))), selected_files]),
            ft.Row([ft.TextButton("Выполнить удаление", on_click=lambda e: delete_file_result(selected_files.value,
                my_delete_path_ref.current.value)),
                    ft.Text(ref=my_delete_path_ref, value='')]),
            ft.TextButton("Закрыть окно", on_click=lambda e: page.close(dlg_delete_file)),
        ],
    )
    dlg_delete_folder = ft.AlertDialog(
        modal=True,
        title=ft.Text("Удаление папки."),
        content=ft.Text("Выберите папку которую хотите удалить."),
        actions=[
            ft.Row([ft.TextButton("Выбор папки", content=ft.Text("Выбор папки"), on_click=lambda e:
            (get_directory_dialog.get_directory_path(), handle_menu_item_click(e))), directory_path]),
            ft.Row([ft.TextButton("Выполнить удаление", on_click=lambda e:
            delete_folder_result(directory_path.value)), ft.Text(ref=my_delete_folder_ref, value='')]),
            ft.TextButton("Закрыть окно", on_click=lambda e: page.close(dlg_delete_folder)),
        ],
    )
    dlg_find_file = ft.AlertDialog(
        modal=True,
        title=ft.Text("Поиск  файла по параметрам."),
        content=ft.Text("Выберите исходную папку для поиска и введите параметры поиска."),
        actions=[
            ft.Row([ft.TextButton("Выбор папки", content=ft.Text("Выбор папки", ref=my_find_file_folder_ref),
                                  on_click=lambda e: (
                                  get_directory_dialog.get_directory_path(), handle_menu_item_click(e))),
                    directory_path]),
            ft.Row([ft.TextField(ref=my_find_file_name_ref, hint_text="Введите имя файла или его часть",
                                 border_color=ft.Colors.BLUE_300)]),
            ft.Row([ft.TextField(ref=my_find_bytes1_ref, hint_text="Если необходимо введите минимальный размер файла"
                                                                   " в байтах", border_color=ft.Colors.BLUE_300,
                                 max_lines=3)]),
            ft.Row([ft.TextField(ref=my_find_bytes2_ref, hint_text="Если необходимо введите максимальный размер файла"
                                                                   " в байтах", border_color=ft.Colors.BLUE_300,
                                 max_lines=3)]),
            ft.Row([ft.TextButton("Выполнить поиск", on_click=lambda e: find_file_result(directory_path.value,
                my_find_file_name_ref.current.value, my_find_bytes1_ref.current.value, my_find_bytes2_ref.current.value)),
                    ft.Text(ref=my_find_file_ref, value='')]),
            ft.TextButton("Закрыть окно", on_click=lambda e: page.close(dlg_find_file)),
        ],
    )

ft.app(main)