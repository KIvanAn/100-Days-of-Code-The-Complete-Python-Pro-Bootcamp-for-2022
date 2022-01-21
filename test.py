import time


# def find_reverse_number(n):
#     n_list = 0
#     i = 0
#     while n_list < n:
#         if i == int(str(i)[::-1]):
#             n_list += 1
#         i += 1
#     return i - 1


def find_reverse_number(n):
    def get_reverse_number():
        number = 0
        while True:
            if number == int(str(number)[::-1]):
                yield number
            number += 1

    revers_num = get_reverse_number()
    i = 0
    res = 0
    while i < n:
        try:
            res = next(revers_num)
            i += 1
        except StopIteration:
            break

    return res


start_time = time.time()
print(find_reverse_number(100000000000))
print(time.time() - start_time)
