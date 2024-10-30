from flet import *


title_txtfield = TextField(
    text_style=TextStyle(font_family="Arial", size=24, weight=FontWeight.BOLD),
    border="none",
    autofocus=True,
    hint_text="Title",
    cursor_color="purple",
    selection_color=colors.PURPLE_400
)

textfield = TextField(
    text_style=TextStyle(font_family="Arial", size=18,),
    multiline=True,
    border="none",
    min_lines=40,
    cursor_color="purple",
    selection_color=colors.PURPLE_400
)

title = Container(
    content=title_txtfield,
    padding=padding.only(left=40, top=10)
)

text = Container(
    content=textfield,
    padding=padding.only(left=40)
)

def main(page: Page):
    page.title = "PuzzlED Notes"
    page.scroll = True
    page.theme_mode = ThemeMode.DARK

    def changetheme(e):
        page.theme_mode = (
            ThemeMode.LIGHT
            if page.theme_mode == ThemeMode.DARK
            else ThemeMode.DARK
        )

        toggleButton.selected = not toggleButton.selected
        page.update()


    toggleButton = IconButton(on_click=changetheme,
                                icon="LIGHT_MODE_OUTLINED",
                                selected_icon="NIGHTLIGHT",
                                style=ButtonStyle(color={"":colors.WHITE, "selected":colors.BLACK}))

    def save_text(e: ControlEvent):
        with open('save.txt', 'w') as f:
            f.write(f"{title_txtfield.value}\n{textfield.value}")

    def load_text():
        try:
            with open('save.txt', 'r') as f:
                lines = f.readlines()
                if lines:
                    title_text = lines[0].strip()
                    title_txtfield.value = title_text
                    textfield.value = ''.join(lines[1:])
                    textfield.hint_text = "Put your text here!"
                else:
                    textfield.value = ""
                    title_txtfield.value = ""
                    textfield.hint_text = "Put your text here!"
        except FileNotFoundError:
            textfield.value = ""
            textfield.hint_text = "Put your text here!"

    title_txtfield.on_change, textfield.on_change = save_text, save_text
    load_text()

    
    
    page.add(title, text,
        AppBar(
            leading=Icon(icons.TEXT_SNIPPET),
            title=Text("PuzzlED"),
            actions=[toggleButton],
            bgcolor=colors.SURFACE_VARIANT
        )
    )


app(target=main)