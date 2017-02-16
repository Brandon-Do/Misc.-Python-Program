def list_counter(lol):
    if not isinstance(lol, list):
        return 0
    count = 1
    for item in lol:
        if isinstance(item, list):
            count += list_counter(item)
    return count





def print_answers(list_of_examples, f):
    for item in list_of_examples:
        print(f(item))

ex_0 = [1, [2, [3]]]
ex_1 = [1, 2, 3, [[[[[[[[[[[[[[[[ ]]]]]]]]]]]]]]]]]
ex_2 = [1, 2, 3]
print(list_counter(ex_1))
li = [ex_0, ex_1, ex_2]

#print_answers(li, list_counter)