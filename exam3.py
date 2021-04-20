el = 'element'
strt = 'start'
fin = 'Finish'
def func1(list):
    list.append(fin)
    list.insert(0 , strt)
    list.insert(0, el)
    return (list)
print(func1([1 , 3 , 5 , 6]))



def func3(tuple_):
    lst = list(tuple_)
    a = list(filter(lambda x: x % 2 == 0, lst))
    b = list(map(lambda x: x ** 2, lst))
    return a, b


a, b = func3((1, 2, 3, 4, 5))
print(a)
print(b)