class A:
    num = 10


class B(A):
    num = 88


class C(A):
    num = 1


class D(C, B):

    pass


print(D.num)
# print(D.mro())
