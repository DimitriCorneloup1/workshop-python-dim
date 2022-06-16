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
    def __init__(self, _hp=100, _attack=5, _stamina=100, _name="John Doe"):
        self._hp = _hp
        self._attack = _attack
        self._stamina = _stamina
        self._name = _name


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
    # seed(1)
    # for _ in range(100):
	#     value = randint(0, 100)
	#     print(value)

    print(Villager._name)