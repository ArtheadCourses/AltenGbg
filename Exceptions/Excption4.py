
class MyExcption(Exception):
    def __init__(self, value, location, msg):
        self.value = value
        self.location = location
        self.msg = msg

    def __str__(self):
        return "There is an error in {0} with code: {1}. Message: {2}".\
            format(self.location, self.value, self.msg)

def my_func():
    raise MyExcption(144, "my_func", "There was an error in my_func")

def my_other_func():
    raise MyExcption(33, "my_other_func", "Opps")


def main():
    try:
        my_func()
    except MyExcption as e:
        print(e)
    
if __name__ == '__main__':
    main()