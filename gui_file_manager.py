import flet as ft
from flet import ElevatedButton, FilePicker, FilePickerResultEvent, Page, Row, Text,Icons
import os
import package_cli_files_manager as p_cli_fm


current_dialog=[]

def main(page: ft.Page):
    appbar_text_ref = ft.Ref[ft.Text]()



    def handle_menu_item_click(e):
        print(f"{e.control.content.value}.on_click")
        page.open(
            ft.SnackBar(content=ft.Text(f"{e.control.content.value} was clicked!"))
        )
        appbar_text_ref.current.value = e.control.content.value

        page.update()


    def pick_files_result(e: ft.FilePickerResultEvent):

        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Не выбрано"
        )
        selected_files.update()


    pick_files_dialog = ft.FilePicker(on_result=pick_files_result)

    selected_files = ft.Text('')
    page.overlay.append(pick_files_dialog)

    def get_directory_result(e: FilePickerResultEvent):
        directory_path.value = e.path if e.path else "Не выбрано"
        directory_path.update()

    get_directory_dialog = FilePicker(on_result=get_directory_result)
    directory_path = Text('')
    page.overlay.append( get_directory_dialog)


    def open_dialog(dialog):
        active_dialog=dialog
        if len(current_dialog)==0:
            current_dialog.append(active_dialog)
        else:
            current_dialog[0]=active_dialog

    page.appbar = ft.AppBar(
        title=ft.Text("Menus", ref=appbar_text_ref),
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
                # width=50,
                # height=50,
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

ft.app(main)