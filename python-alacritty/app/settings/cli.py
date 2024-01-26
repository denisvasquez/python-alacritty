from .load_themes import aviable_themes
from .load_fonts import aviable_fonts
from .apply import load_theme, set_theme, write_yaml, get_group, get_font, write_json

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
        write_json({ "theme": theme })
        return write_yaml("colors", load_theme(theme))
    else:
        print(f"Theme {theme} not found!")

def chfont(font):
    try:
        if int(font): # Verify if the user inserted a number
            print("Please not insert numbers!")
    except ValueError: # if catch error we go does the operation
        if font in aviable_fonts["headers_fonts"]:
            index = aviable_fonts["headers_fonts"].index(font)
            new_font = aviable_fonts["fonts"][index]
            config_font = get_font()
            config_font["normal"]["family"] = new_font
            config_font["bold"]["family"] = new_font
            config_font["italic"]["family"] = new_font
            return write_yaml("font", config_font)
        else:
            print("The font '{0}' not found!".format(font))

def chsizefont(size):
    configs_font = get_font()
    try:
        size = int(size)
        if size >= 8 and size <= 25:
            configs_font["size"] = int(size)
            return write_yaml("font", configs_font)
        else:
            print("Number out of range! Insert a number 8 - 25!")
    except ValueError:
        print("Insert a number!")
