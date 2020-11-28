def is_inc_and_repeating(number):
    x_str = str(number)
    increasing = True
    repeat = 1
    two_peat = False
    
    for i in range(0, len(x_str) - 1):
        if increasing and (int(x_str[i]) <= int(x_str[i+1])):
            increasing = True
        else:
            increasing = False

        if int(x_str[i]) == int(x_str[i+1]):
            repeat += 1
        else:
            if repeat == 2:
                two_peat = True
            repeat = 1
    
    if repeat == 2:
        two_peat = True
    
    if increasing and two_peat:
        return True
    else:
        return False


if __name__ == "__main__":
    min = 165432
    max = 707912

    counter = 0
    for x in range(min, max + 1):
        if is_inc_and_repeating(x):
            counter += 1
    
    print(counter)
        
    