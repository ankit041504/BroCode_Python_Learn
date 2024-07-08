class A:
    def __init__(ankit):
        print("auto call")

obj = A()

class B:
    def sumf(a, b):
        print("executing function body")
        c = a + b
        print(c)

obj2 = B.sumf(5,5)






