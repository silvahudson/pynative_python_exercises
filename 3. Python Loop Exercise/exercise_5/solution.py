def display_numbers(lst):
    for i in lst:
        if i > 500:
            break 
        elif i > 150:
            continue
        elif i % 5 == 0:
            print(i)

if __name__ == '__main__':
    numbers = [12, 75, 150, 180, 145, 525, 50]
    display_numbers(numbers)
    
    