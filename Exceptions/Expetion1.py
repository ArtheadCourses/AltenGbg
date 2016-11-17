
def func():
    x = 5
    y = 0
    try:
        z = x / y
    except ZeroDivisionError as e:
        print(e)
    else:
        print(z)
    finally:
        print("Close files etc...")

    print("Done in func")

def main():
    func()
    print("Done")
    
if __name__ == '__main__':
    main()