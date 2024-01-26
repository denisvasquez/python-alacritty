from .path import alacritty_path
from os import path
import yaml
import json

def showcurrent():
    with open(path.join(alacritty_path, "python-alacritty", "config", "theme.json"), "r") as c:
        current_theme = json.load(c)["theme"]

    with open(path.join(alacritty_path, "alacritty.yml"), "r") as ct:
        current_configs = yaml.load(ct, Loader=yaml.FullLoader)

    message = f"""theme: {current_theme}
font-family: {current_configs["font"]["normal"]["family"]}
font-size: {current_configs["font"]["size"]}
opacity: {current_configs["window"]["opacity"]}
padding:
    vertical: {current_configs["window"]["padding"]["y"]}
    horizontal: {current_configs["window"]["padding"]["x"]}
    """
    print(message)

def load_theme(theme):
    with open(path.join(alacritty_path, "python-alacritty", "config", "themes", f"{theme}.yaml")) as t:
        return yaml.load(t, Loader=yaml.FullLoader)["colors"]

def set_theme(configs):
    with open(path.join(alacritty_path, "alacritty.yml"), "w") as a:
        return yaml.dump(configs, a)

def write_json(config):
    with open(path.join(alacritty_path, "python-alacritty", "config", "theme.json"), "w") as c:
        json.dump(config, c)

def write_yaml(group, configs):
    with open(path.join(alacritty_path, "alacritty.yml"), "r") as a:
        yml = yaml.load(a, Loader=yaml.FullLoader)
        yml[group] = configs
    return set_theme(yml)

def get_group():
    with open(path.join(alacritty_path, "alacritty.yml")) as g:
        return yaml.load(g, Loader=yaml.FullLoader)["window"]

def get_font():
    with open(path.join(alacritty_path, "alacritty.yml")) as g:
        return yaml.load(g, Loader=yaml.FullLoader)["font"]


