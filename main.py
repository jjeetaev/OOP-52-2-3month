# sudo apt install libmpv12
import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Мое первое приложение на Flet"    
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text("Привет, мир!", color="black")

    greeting_history = []

    history_text = ft.Text("История приветствий:")

    def on_button_click(e):
        name = name_input.value.strip()

        if name:
            current_hour = datetime.now().hour

            if 6 <= current_hour < 12:
                greeting = "Доброе утро"
                greeting_text.color = "yellow"
            elif 12 <= current_hour < 18:
                greeting = "Добрый день"
                greeting_text.color = "orange"
            elif 18 <= current_hour < 24:
                greeting = "Добрый вечер"
                greeting_text.color = "red"
            else:
                greeting = "Доброй ночи"
                greeting_text.color = "blue"

            greeting_text.value = f"{greeting}, {name}!"
            name_input.value = ""

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            greeting_history.append(f"{timestamp} - {name}")
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
        else:
            greeting_text.value = "Пожалуйста, введите имя."
            greeting_text.color = "black"

        page.update()

    name_input = ft.TextField(label="Введите ваше имя", autofocus=True, on_submit=on_button_click)

    def toggle_theme(_):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
        page.update()

    def clear_history(_):
        greeting_history.clear()
        history_text.value = "История приветствий:"
        page.update()

    def copy_greeting(_):
        page.set_clipboard(greeting_text.value)

    clear_button = ft.ElevatedButton("Очистить историю", icon=ft.Icons.DELETE, on_click=clear_history)

    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, tooltip='Сменить тему', on_click=toggle_theme)

    greet_button = ft.ElevatedButton("Поздороваться", icon=ft.Icons.HANDSHAKE, on_click=on_button_click)

    copy_button = ft.IconButton(icon=ft.Icons.COPY, tooltip='Скопировать приветствие', on_click=copy_greeting)

    page.add(
        ft.Row([greeting_text, copy_button], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([name_input, greet_button, theme_button, clear_button], alignment=ft.MainAxisAlignment.CENTER),
        history_text
    )

ft.app(target=main, view=ft.WEB_BROWSER)
