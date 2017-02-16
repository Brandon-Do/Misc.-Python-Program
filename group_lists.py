def groups(li):
    if len(li) == 0:
        return li

    li.append(li[-1] + 1)

    sub_list = []
    return_list = []

    for n in range(1, len(li)):
        sub_list.append(li[n - 1])
        if li[n-1] != li[n]:
            return_list.append(sub_list)
            sub_list = []

    return return_list

answer = groups([1, 1, 1, 1, 1, 2, 3, 4, 5, 6, 6, 6, 7])
print(answer)
