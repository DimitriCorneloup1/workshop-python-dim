#!/usr/bin/python3


# def calculate(data):
#     res = 0
#     x = 0
#     if (len(data) == 1):
#         return False
#     while (x <= len(data)):
#         if (isdigit(x)):
#             res += data[x]
#     return res

class Villager:
    def __init__(self, _hp, _attack, _stamina, _name):
        self._hp = 100
        self._attack = 5
        self._stamina = 100
        self._name = "john"

if __name__ == '__main__':
    # i = 0
    # while (i <= 100):
    #     if (i % 3 == 0 and i % 5 == 0):
    #         print("ThreeFive")
    #         i += 1
    #     elif (i % 3 == 0):
    #         print("Three")
    #         i += 1
    #     elif (i % 5 == 0):

    #         print("five")
    #         i += 1
    #     else:
    #         print(i)
    #         i += 1
    # data = ['4', '3', '-2']
    # res = calculate(data)
    # print(res)

    # from random import seed
    # from random import randint
    # # seed random number generator
    # seed(1)
    # # generate some integers
    # for _ in range(10):
	#     value = randint(0, 100)
	#     print(value)
    print(Villager._name)