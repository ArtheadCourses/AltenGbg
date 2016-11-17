
def main():
    x = -7

    for y in range(-7, 260):
        if id(x) == id(y):
            print(y, "Same")
        else:
            print(y, "Not same")
        x += 1
    
if __name__ == '__main__':
    main()