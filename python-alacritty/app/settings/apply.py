from .path import alacritty_path
from os import path
import yaml

def load_theme(theme):
    with open(path.join(alacritty_path, "python-alacritty", "config", "themes", f"{theme}.yaml")) as t:
        return yaml.load(t, Loader=yaml.FullLoader)["colors"]

def set_theme(configs):
    with open(path.join(alacritty_path, "alacritty.yml"), "w") as a:
        return yaml.dump(configs, a)

def write_yaml(group, configs):
    with open(path.join(alacritty_path, "alacritty.yml"), "r") as a:
        yml = yaml.load(a, Loader=yaml.FullLoader)
        yml[group] = configs
    return set_theme(yml)

def get_group():
    with open(path.join(alacritty_path, "alacritty.yml")) as g:
        return yaml.load(g, Loader=yaml.FullLoader)["window"]

