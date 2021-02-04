def my_func(param1='default'):
    print("my first function")
my_func()

def hello():
    print("hello")
hello()

#call function outside the scope of function

def hello():
    return "hello"

result = hello()

print(result)

