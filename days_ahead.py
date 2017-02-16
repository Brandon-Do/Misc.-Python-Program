MONTHS = ["X","Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
DAYS = [ 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

def days_ahead( month, day, ahead ):
    if month == 'X':
        return days_ahead(MONTHS[1], day, ahead)

    month_num = 0
    for k in range(1, len(MONTHS)):
        if month == MONTHS[k]:
            month_num = k

    if ahead + day <= DAYS[month_num]:
        return '{} {}'.format(month, day + ahead)

    ahead -= DAYS[month_num] - day

    return days_ahead(MONTHS[month_num + 1], 0, ahead)


print(days_ahead(11,20,90))
