num = [8, 2, 3, 0, 7]
def sum(num_list):
    total = 0
    for num in num_list:
        total += num
    return total
print(sum(num))