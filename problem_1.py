#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

k = 17
number_list = [10, 15, 3, 7]

def solver(list, num):
checker = False
    for number in list:
        for number2 in list:
            if number + number2 == num:
                checker = True
                return True
    if checker == False:
        return False

solver(number_list, k)
