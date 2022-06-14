import argparse
from .settings.cli import chtheme, list_themes, chopacity, chpadding, showcurrent

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--theme", nargs="?")
    parser.add_argument("-l", "--list", const=1, nargs="?")
    parser.add_argument("-o", "--opacity", nargs="?")
    parser.add_argument("-p", "--padding", nargs="?")
    parser.add_argument("-c", "--current", const="1", nargs="?")

    args = parser.parse_args()

    if args.theme:
        chtheme(args.theme)

    if args.list:
        list_themes()

    if args.opacity:
        chopacity(args.opacity)

    if args.padding:
        chpadding(args.padding)

    if args.current:
        showcurrent()

if __name__ == "__main__":
    main()

