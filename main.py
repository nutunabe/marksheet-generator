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
    print("pawol naxyi")


def main(*args):
    institute = Institute()
    def clear(): return os.system('cls')
    # print(type(args[0]))
    # print(args[0])
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


        # while True:
        #     # clear()
        #     print("выавыа")
        #     _input = input()
        #     if _input == "0":
        #         quit()
        #     elif _input == "1":
        #         sadsadasd = ''
        #         print(1)
        #     else:
        #         asdasdsa = ''
        #         print('asds')

    # if len(args[0]) < 4:
    #     print('error: example - cmdline.py 1 2 3')
    #     quit()
    # try:
    #     a = int(args[0][1])
    # except:
    #     print('error: first argument must be integer!')
    #     quit()
    # try:
    #     b = int(args[0][2])
    # except:
    #     print('error: second argument must be integer!')
    #     quit()
    # try:
    #     c = int(args[0][3])
    # except:
    #     print('error: third argument must be integer!')
    #     quit()
    # finally:
    #     print('chiki puki')


if __name__ == "__main__":
    main(sys.argv)
