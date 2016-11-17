
class Employee:
    rasie_amnt = 1.04
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

    def give_raise(self):
        self.pay *= self.rasie_amnt

class Developer(Employee):
    rasie_amnt = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    pass


def main():
    emp1 = Developer("Sue", "Smith", 50000, 'Python')
    emp2 = Developer("John", "Miller", 45000, 'Java')
    emp3 = Developer("Sara", "Johnson", 55000, 'C++')
    emp4 = Manager("Peter", "Davidsson", 75000)

    print(emp1)
    emp1.give_raise()
    print(emp1)



if __name__ == '__main__':
    main()