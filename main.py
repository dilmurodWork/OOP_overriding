class A:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def __str__(self):
        return '{}, {}'.format(self.name, self.age)

    def __add__(self, other):
        return A(self.name + other.name, self.age + other.age)

    def __sub__(self, other):
        return A(self.name+other.name, self.age-other.age)


a = A('Jozef')
b = A('Metyu',19)
c = A('Yakob', 20)
print(a+b-c-a)

