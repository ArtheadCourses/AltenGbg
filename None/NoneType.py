
def test(name, name_list=None):
    if not name_list:
        name_list = []
    name_list.append(name)
    print(name_list)

def main():
    test_list = ['Eric']
    test('Anna')
    test('John')
    test('Peter')
    
if __name__ == '__main__':
    main()