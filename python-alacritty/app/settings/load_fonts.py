import yaml
from os import path
from .path import alacritty_path

path_fonts = path.join(path.expanduser("~"), ".config", "alacritty", "python-alacritty", "config", "fonts.yaml")

aviable_fonts = { "headers_fonts": [], "fonts": [] }
with open(path_fonts, "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)["fonts"]
    for i in range(len(list(config))):
        aviable_fonts["headers_fonts"].append(list(config.keys())[i].lower())
        aviable_fonts["fonts"].append(list(config.values())[i])

