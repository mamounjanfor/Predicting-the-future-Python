"""
Author: Mamoun Janfor


"""


def tuition_doubled():
    a = int(input("Enter the Tuition: "))
    c = a * 2
    i = 0
    while a < c:
        a = (a * 1.07)
        i = i + 1
    print(i)


tuition_doubled()
