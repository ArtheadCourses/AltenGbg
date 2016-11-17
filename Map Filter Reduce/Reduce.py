from functools import reduce

def get_max(a, b):
    if a > b:
        return a
    else:
        return b


def get_min(a, b):
    if a < b:
        return a
    else:
        return b

def get_sum(a, b):
    return a + b

def main():
    list_of_numbers = [23, 143, 13, 4, 33, 9, 16, 97]
    max = reduce(get_max, list_of_numbers)
    min = reduce(get_min, list_of_numbers)
    #sum = reduce(get_sum, list_of_numbers)
    sum = reduce(lambda a, b: a + b, list_of_numbers)
    print(max)
    print(min)
    print(sum)

if __name__ == '__main__':
    main()