from .load_themes import aviable_themes
from .apply import load_theme, set_theme, write_yaml, get_group

def list_themes():
    for _ in range(len(aviable_themes)):
        print(f"[{_}] -> {aviable_themes[_][0:-5]}")

    try:
        theme = int(input(f"Select a theme (0-{len(aviable_themes) - 1}): "))
        return chtheme(aviable_themes[theme][0:-5])
    except ValueError:
        print("Insert a number!")

def chopacity(opacity):
    try:
        opacity = float(opacity)
        padding = get_group()["padding"]
        if opacity >= 0.0 and opacity <= 1:
            return write_yaml("window", { "opacity": opacity, "padding": padding })
        else:
            print("Index out of range!")

    except ValueError:
        print("Insert a number in range 0.0 - 1")

def chpadding(padding):
    try:
        padding = int(padding)
        opacity = get_group()["opacity"]
        if padding >= 1 and padding <= 200:
            return write_yaml("window",  { "padding": { "x": padding, "y": padding }, "opacity": opacity })
        else:
            print("Index out of range, please insert in range (1, 200)!")
    except ValueError:
        print("Insert a number!")

def chtheme(theme):
    if f"{theme}.yaml" in aviable_themes:
        return write_yaml("colors", load_theme(theme))
    else:
        print(f"Theme {theme} not found!")


def showcurrent():
    print("Esto funciona")

