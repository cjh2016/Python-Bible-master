import my_name


def print_name():
    my_name.print_name()
    print("python_main.py__name__:", __name__)


if __name__ == '__main__':
    print_name()
