# get padding according to matrix
def get_padding(number, current_num):
    if number == 4:
        if current_num == 0 or current_num == 3:
            return 120
        else:
            return 40
    elif number == 3:
        if current_num == 0 or current_num == 2:
            return 80
        else:
            return 0
    elif number == 2:
        return 40
    else:
        return 0


# get side for position according to matrix
def get_side(number, current_num):
    if number == 4:
        if current_num == 0 or current_num == 1:
            return 'right'
        else:
            return 'left'
    elif number == 3:
        if current_num == 0:
            return 'right'
        else:
            return 'left'
    elif number == 2:
        if current_num == 0:
            return 'right'
        else:
            return 'left'
    else:
        return 'left'
