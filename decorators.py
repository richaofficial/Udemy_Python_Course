S= "Global variable"


def func():
    mylocal= 10
    print(locals())
    print(globals())

func()