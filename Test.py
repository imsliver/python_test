def main(task):
    try:
        a, operation, b = task.split()
        if 1 <= int(a) <= 10 and 1 <= int(b) <= 10:
            return (
                {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '*': lambda a, b: a * b, '/': lambda a, b: a // b}
                [operation](int(a), int(b)))
        else:
            print('The numbers entered into the calculator must be in the range from 1 to 10. Try again')
    except:
        print('Oops, error. Try again')


print(main(input()))
