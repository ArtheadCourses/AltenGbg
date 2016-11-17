
def func(x, y):
    if y == 0:
        raise ValueError
    else:
        z = x / y
        print(z)
    print("Done in func")

def main():
    try:
        func(5, 0)
    except ZeroDivisionError:
        print("Zero Division Error")
    except ValueError:
        print("Value Error")
        #raise
    print("Done")
    
if __name__ == '__main__':
    main()