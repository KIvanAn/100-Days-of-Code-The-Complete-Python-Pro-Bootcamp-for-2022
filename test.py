def zero_plentiful(arr):
    return len([item for item in "".join(str(num) if num == 0 else "-" for num in arr).split("-") if len(item) >= 4])


print(zero_plentiful([0, 2, 0, 0, 0, 0, 3, 4, 5, 0, 0, 0, 0, 0]))
