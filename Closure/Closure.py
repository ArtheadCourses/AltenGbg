
def outer(pow):
    def inner(base):
        return base**pow
    return inner

def print_name(name):
    print("hi", name)

def main():
    print_name("Anna")
    square = outer(2)

    print(square(3))
    print(square(4))

    cube = outer(3)
    print(cube(3))
    print(cube(4))
    
if __name__ == '__main__':
    main()