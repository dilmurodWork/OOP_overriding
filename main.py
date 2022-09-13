# class A:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return '{}, {}'.format(self.name, self.age)
#
#     def __add__(self, other):
#         return A(self.name + other.name, self.age + other.age)
#
#     def __sub__(self, other):
#         return A(self.name+other.name, self.age-other.age)
#
#
# a = A('Jozef')
# b = A('Metyu',19)
# c = A('Yakob', 20)
# print(a+b-c-a)
#
# class B:
#     def __init__(self, name):
#         self.name = name
#
#     def __setattr__(self, attr, value):
#         if attr == 'name':
#             self.__dict__[attr] = value
#         else:
#             raise AttributeError
#
#
# d = B('yoyo')
# d.name = 'Koko'
# print(d.name)
# class C:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __setattr__(self, key, value):
#         self.__dict__['name'] = key
#         self.__dict__['age'] = value
#
#     def __str__(self):
#         return f'{self.name}: {self.age}'
#
#
# c = C('pep', 56)
# c.name = 'rop'
# c.weight = 45
# print(c)

# class Bolb:
#     def __init__(self, name, w, v):
#         self._name = name
#         self._w = w
#         self._v = v
#
#     def get_name(self):
#         return self._name
#
#     def get_v(self):
#         return self._v
#
#     def get_w(self):
#         return self._w
#
#     def __str__(self):
#         return f'{self._name} {self._w} {self._v}'
#
#     def __add__(self, other):
#         self._name = self._name + ' & ' + other.get_name()
#         self._v = self._v * other.get_v()
#         self._w = self._w * other.get_w()
#         return self
#
#
# c = Bolb('Folp', 34, 45)
# d = Bolb('Golp', 44, 65)
# print(c+d)
# class Number:
#     def __init__(self, n):
#         self.number = n
#
#     def __add__(self, other):  # a + b
#         self.number = self.number + other.number
#         return self
#
#     def __truediv__(self, other):  # a / b
#         self.number = self.number / other.number
#         return self
#
#     def __mul__(self, other):  # a * b
#         self.number = self.number * other.number
#         return self
#
#     def __sub__(self, other):  # a - b
#         try:
#             self.number = self.number - other.number
#         except AttributeError:
#             self.number = self.number - other
#         return self
#
#
# a = Number(9)
# b = Number(40)
# c = a / b
# print(c.number)
#
# r = a-b
# print(r.number)
# class Drob:
#     def __init__(self, p, z):
#         self.p = p
#         self.z = z
#
#     def __str__(self):
#         return '{}/{}'.format(self.p, self.z)
#
#     def __mul__(self, other):
#         self.p = self.p * other.p
#         self.z = self.z * other.z
#         return self
#
#     def __truediv__(self, other):
#         self.p = self.p / other.p
#         self.z = self.z / other.z
#         return self
#
#     def __add__(self, other):
#         global p
#         if self.z == other.z:
#             self.p = self.p + other.p
#         else:
#             z = self.z * other.z
#             p = self.p * other.z + other.p * self.z
#
#         return Drob(p, z)
#
#     def __sub__(self, other):
#         global p
#         if self.z == other.z:
#             self.p = self.p - other.p
#         else:
#             z = self.z * other.z
#             p = self.p * other.z - other.p * self.z
#
#         return Drob(p, z)
#
#
# d = Drob(7, 8)
# f = Drob(3, 5)
# print(d - f)
class Library:
    def __init__(self, name, adress='Amir Temur main street 1 ', kol=20):
        self.name = name
        self.adress = adress
        self.kol = kol

    def __str__(self):
        return f'books : {self.name}\nCount: {self.kol}\nAdress: {self.adress}'

    def __iadd__(self, other):
        self.name += ' & ' + other.name
        self.kol += other.kol
        return self

    def __isub__(self, other):
        self.name += ' & ' + other.name
        self.kol -= other.kol
        return self

    def __lt__(self, other):
        return self.kol < other.kol

    def __gt__(self, other):
        return self.kol > other.kol

    def __le__(self, other):
        return self.kol <= other.kol

    def __ge__(self, other):
        return self.kol >= other.kol

    def __eq__(self, other):
        return self.kol == other.kol

    def __ne__(self, other):
        return self.kol != other.kol

    def __len__(self):
        return self.kol


f = Library('Kolkata')
r = Library('Lakamorya', kol=33)

f -= r
print(f)

print(f.__len__())
