class A:
    def __init__(self,a):
        self.a=a

    def __lt__(self,other):
        if self.a < other.a:
            return "obj1 is less than obj2"
        else:
            return "obj1 is greater than obj2"
    def __eq__(self,other):
        if self.a == other.a:
            return 'obj1 is equal to obj2'
        else:
            return "not equal"

obj1=A(4)
obj2=A(5)
obj3=A(6)
obj4=A(7)
print(obj1<obj2)
print(obj3==obj4)