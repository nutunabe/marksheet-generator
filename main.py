import sys
import os
from components.institute import Institute
from cli.add import add
from cli.get import get
__app_name__ = "marksheet-generator"
__version__ = "0.0.1"


def print_version():
    print(f"{__app_name__} v{__version__}")


def print_help():
    text = '''Usage: main.py [OPTIONS] COMMAND

Options:
    -v, --version       Show the application's version and exit.

    -h, --help          Show this message and exit.
    
Commands:
    add student
    add group
    get student'''
    print(text)


def main(*args):
    institute = Institute()
    def clear(): return os.system('cls')
    if len(args[0]) == 1:
        print("ERROR:\texample - main.py 1 2\ntry:\tmain.py -h")
        quit()
    if len(args[0]) == 2:
        if args[0][1] == '-v' or args[0][1] == '--version':
            print_version()
            quit()
        elif args[0][1] == '-h' or args[0][1] == '--help':
            print_help()
            quit()
    if len(args[0]) == 3:
        if args[0][1] == 'add':
            add(args[0][2], institute)
        if args[0][1] == 'get':
            get(args[0][2], institute)


if __name__ == "__main__":
    main(sys.argv)
