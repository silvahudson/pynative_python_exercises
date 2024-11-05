def count_digits(number):
    count = 0
    i = 0
    while i < len(str(number)):
        if str(number)[i].isdigit():
            count += 1
        i += 1
    return count    

if __name__ == '__main__':
    number = 75869
    print(count_digits(number))
    
    