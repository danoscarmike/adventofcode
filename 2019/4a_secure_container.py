def is_increasing(number):
    x_str = str(number)
    increasing = True
    for i in range(0, len(x_str) - 1):
        if int(x_str[i]) > int(x_str[i+1]):
            increasing = False
            break
    return increasing


def has_repeat(number):
    x_str = str(number)
    adjacent = False
    for i in range(0, len(x_str) - 1):
        if int(x_str[i]) == int(x_str[i+1]):
            adjacent = True
            break
    return adjacent

if __name__ == "__main__":
    min = 165432
    max = 707912

    counter = 0
    for x in range(min, max + 1):
        if is_increasing(x) and has_repeat(x):
            counter += 1
    
    print(counter)
        
    