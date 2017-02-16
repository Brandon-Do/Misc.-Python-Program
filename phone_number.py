def reformat(s, fmt):

    result = ''
    s = list(s)
    fmt = list(fmt)

    for item in fmt:
        if item == '#':
            item = s[0]
            s = s[1:]

    if len(s) > 0:
        for item in s:
            result = result + item

    return result

answer = reformat('5035058120', '(###) ###-####')
print(answer)