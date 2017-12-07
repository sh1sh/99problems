def print_1():
    print(u"Zmienna ma wartość 1")


def print_2():
    print(u"Zmienna ma wartość 2")


def print_default():
    print(u"Zmienna ma wartość nie 1 i nie 2")


case = {
    1: print_1,
    2: print_2,
}

zmienna = 3

case.get(zmienna, print_default)()