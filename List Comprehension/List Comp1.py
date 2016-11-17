
def main():
    num_list = [1, 2, 3, 5, 7, 9]
    result1 = []
    for value in num_list:
        if value != 2:
            if value != 3:
                result1.append(value**2)
            else:
                result1.append(value**3)


    result = (value**2  if value != 3 else value**3 for value in num_list if value != 2)
    print(result1)
    for r in result:
        print(r)
    
if __name__ == '__main__':
    main()