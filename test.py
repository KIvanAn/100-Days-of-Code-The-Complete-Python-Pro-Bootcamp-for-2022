import time


def find_reverse_number(n):
    n_list = 0
    i = 0
    while n_list < n:
        if i == int(str(i)[::-1]):
            n_list += 1
        i += 1
    return i - 1


# def find_reverse_number(n):
#     def get_reverse_number():
#         i = 0
#         for number in range(n):
#             if number == int(str(number)[::-1]):
#                 yield number
#                 i += 1
#     revers_num = get_reverse_number()
#     is_stop = False
#     # i = 0
#     while not is_stop:
#         try:
#             print(next(revers_num))
#             # next(revers_num)
#             # i += 1
#         except StopIteration:
#             is_stop = True
#
#     return next(revers_num)


start_time = time.time()
print(find_reverse_number(100))
print(time.time() - start_time)
