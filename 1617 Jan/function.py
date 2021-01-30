"""block of code which only runs when it is called
    able to pass data, known as parameters, into a function.
    can return data as a result"""

name = input("Nama kamu adalah ")
def my_function (name = " "):
    print("Hello " + name)

my_function(name)