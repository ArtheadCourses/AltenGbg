
def func(x, y):
    z = x / y
    print(z)
    print("Done in func")

def main():
    try:
        func(5, 0)
    except ZeroDivisionError as e:
        func(5, 0)
    print("Done")
    
if __name__ == '__main__':
    main()