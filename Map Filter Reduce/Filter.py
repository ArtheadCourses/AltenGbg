
def div_by_3(n):
    return n % 3 == 0

def main():
    list_of_numbers = [23, 143, 13, 4, 33, 9, 16, 97]
    #result = list(filter(div_by_3, list_of_numbers))
    result = list(filter(lambda n: n % 3 == 0, list_of_numbers))
    print(result)

    result2 = [value for value in list_of_numbers if value % 3 == 0]
    print(result2)

if __name__ == '__main__':
    main()