# Напишите 3 функции

# 1-ая должна принимать список. Добавлять в этот список элементы 'Element', 'start', 'finish'. Все элементы
# первоначального списка должны находиться между элементами 'start', 'finish'

list = ['Element', 'start', 'finish']
def append_str(str):
    list.insert(2, str)

append_str('John')
append_str('hello')
print(list)

# print(func(['hello', 5, 'John', ])) # ['Element', 'start', 'hello', 5, 'John', 'finish']
# 2-ая должна принимать производное количество аргументов и возвращать словарь, где ключами являются принятые
# аргументы, а значениями числа от 1 до количества принятых аргументов

def func (lsst):
    a = 0
    dic = {}
    for i in lsst:
        a = a + 1
        dic.update({i:a})
    print(dic)

lsst = ['x', 5, 'John',]
dict = func(list)


# print(func('x', 5, 'John')) # {'x':1, 5:2, 'John':3}
# 3я должна принять кортеж. Превращать этот кортеж в список и, используя анономные функции, выдавать нам на выход
# 2 списка. 1-ый список должен состоять из всех чётных чисел введённого кортежа. 2-ой со всеми элементами введённого
# кортежа возведёнными в квадратную степень

def tuple_pep(i):
    a = list(filter(lambda x:x % 2 == 0, i))
    b = list(map(lambda x:x **2, i))
    print(a)
    print(b)
tuple_pep((1, 2, 3, 4, 5))

