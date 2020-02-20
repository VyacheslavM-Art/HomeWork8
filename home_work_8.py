# Задание 1
class My_date:
    def __init__(self, p_date):
        my_date = p_date

    @classmethod
    def change_format(cls, param):
        l = [int(i) for i in param.split("-")]
        return l

    @staticmethod
    def check_date(param):
        if param[1] in [1, 3, 5, 7, 8, 10, 12]:
            if param[0] in range(1, 32):
                return True
        elif param[1] in [4, 6, 9, 11]:
            if param[0] in range(1, 31):
                return True
        elif param[1] == 2:
            if param[2] % 4 == 0:
                if param[0] in range(1, 30):
                    return True
            else:
                if param[0] in range(1, 29):
                    return True
        return False


m = My_date.change_format("8-12-27")
print(My_date.check_date(m))


# Задание 2
class My_Error(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_a = input("a = ")
inp_b = input("b = ")

try:
    inp_a = int(inp_a)
    inp_b = int(inp_b)
    if inp_b == 0:
        raise My_Error("Попытка деления на 0")
except ValueError:
    print("Вы ввели не число")
except My_Error as err:
    print(err)
else:
    print(f"Все хорошо. Результат: ", inp_a / inp_b)


# Задание 3

class My_Error(Exception):
    def __init__(self, txt):
        self.txt = txt


print("Введите значения списка:")
my_list = []

while True:
    try:
        s = input()
        if s == "stop":
            break
        elif not s.isdigit():
            raise My_Error("Введено не число")
        else:
            my_list.append(int(s))
    except My_Error as err:
        print(err)

print("Список: \n", my_list)


# Задание 4 + 5 + 6
class Sklad:
    def __init__(self):
        self.slad = {}
        self.otdel = {}

    def priem(self, orgtek, count):
        if self.slad[orgtek.serial_number] == None:
            self.slad[orgtek.serial_number] = count
        else:
            self.slad[orgtek.serial_number] = self.slad[orgtek.serial_number] + count

    def in_otdel(self, named_otdel, orgtek, count):
        if self.otdel[named_otdel][orgtek.serial_number] == None:
            self.otdel[named_otdel][orgtek.serial_number] = count
        else:
            self.otdel[named_otdel][orgtek.serial_number] = self.otdel[named_otdel][orgtek.serial_number] + count


class Orgtekcnica():
    name = ""
    serial_number = ""
    firma = ""


class Printer(Orgtekcnica):
    def __init__(self, name, serial_number, firma, v_print, type_resource):
        self.name = name
        self.serial_number = serial_number
        self.firma = firma
        self.v_print = v_print
        self.type_resource = type_resource


class Scaner(Orgtekcnica):
    def __init__(self, name, serial_number, firma, kach):
        self.name = name
        self.serial_number = serial_number
        self.firma = firma
        self.kach = kach


class Copyer(Orgtekcnica):
    def __init__(self, name, serial_number, firma, v_print):
        self.name = name
        self.serial_number = serial_number
        self.firma = firma
        self.v_print = v_print


# Задание 7

class Complex_number:
    def __init__(self, x, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        if self.y > 0:
            return str(self.x) + " + " + str(self.y) + "i"
        elif self.y < 0:
            return str(self.x) + str(self.y) + "i"
        else:
            return str(self.x)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Complex_number(x, y)

    def __mul__(self, other):
        x=self.x*other.x-self.y*other.y
        y=self.x*other.y+self.y*other.x
        return Complex_number(x,y)

m=Complex_number(5,7)
f=Complex_number(9,2)
print("Sum = ",m+f,"\n Mul =",m*f)

