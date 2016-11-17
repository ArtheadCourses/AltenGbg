
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

    def __add__(self, other):
        print(self.first, other.first)
        if isinstance(other, Employee):
            return Employee("","",self.pay + other.pay)
        return NotImplemented


def main():
    emp1 = Employee("Sue", "Smith", 50000)
    emp2 = Employee("John", "Miller", 45000)
    emp3 = Employee("Sara", "Johnson", 55000)
    emp4 = Employee("Peter", "Davidsson", 75000)

    x = emp1 + emp2 + emp3 + emp4
    print(x)
if __name__ == '__main__':
    main()