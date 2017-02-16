def nested_list_set(lol, set):
    if isinstance(lol, int):
        set.append(lol)
        return set
    else:
        for k in range(len(lol)):
            if isinstance(lol[k], int):
                if lol[k] not in set:
                    set.append(lol[k])

            if isinstance(lol[k], list):
                for elem in nested_list_set(lol[k], set):
                    if not elem in set:
                        set.append(elem)
    return set

lists = [1, 2, 3, [4, 5, 6, [7, 8]], [], 9]
aset = set([])
print(aset)

print(nested_list_set(lists, aset))

def approx_log(x, n):

    neg = 1
    x = x - 1
    x_prod = x
    sum = 0.0

    for k in range(1, n):
        sum += neg * x / k
        x *= x_prod
        neg *= -1

    return sum

print(approx_log(1.8, 5))