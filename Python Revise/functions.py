def greetHello():
    print("Hello")
    print("Good Morning")
    print("Good Afternoon")

print("Executing function....")
greetHello()
print("done..")

def greetHello2(name,end):
    print("Hello "+name)
    print("Good Morning")
    print("Good Afternoon")
    print(end)

 
def lettergen(name,date):
    st=f"This is {name} and I will not come to school on {date}"
    print(st)

print("Executing function 2...")
greetHello2("Amulya","Thank You")
print("-----again-------")
greetHello2("Akarsha","Thank You")
print("-----again-------")
lettergen("Amulya", "25thJanuary")
print("done..")


def add(a,b):
    c=a+b
    return c

print("Executing function 3...")
result=add(4,5)
print(result)