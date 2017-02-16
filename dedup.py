def dedup(w):

    w = list(w)
    w.append('@')
    result = ''

    for k in range(1, len(w)):
        print(w[k-1], w[k])
        if w[k-1] != w[k]:

            result = result + w[k-1]

    return result

str = '0123456789'

print(str[5:])
print(str[:5])