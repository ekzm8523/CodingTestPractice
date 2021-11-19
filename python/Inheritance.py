
class A:
    id = 123

    def func(self):
        print("A function execute")

class B(A):

    def func(self):
        super().func()
        print("B function execute")

if __name__ == '__main__':
    a1 = A()
    a2 = A()

    print(a1.id)
    print(a2.id)
    A.id = 456
    print(a1.id)
    print(a2.id)

    A().func()
    B().func()