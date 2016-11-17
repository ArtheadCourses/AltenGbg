
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first.lower() + '.' + last.lower() + '@company.com'
        self.pay = pay

    def get_fullname(self):
        return "{} {}".format(self.first, self.last)

    def __repr__(self):
        return "Eployee({}, {}, {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return self.get_fullname() + ' has a sallery of ' + str(self.pay)

def main():
    emp1 = Employee("Sue", "Smith", 50000)
    print(emp1.email)
    print(repr(emp1))


if __name__ == '__main__':
    main()