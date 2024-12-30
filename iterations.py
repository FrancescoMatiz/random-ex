
def pari(v : int) -> bool:
    return v % 2 == 0
def dividi2(v : int) -> int:
    return int(v / 2)

l = [1,2,3,4,5,6,7,8]

for i in range(len(l)):
    print(l)


x = map(pari, l)
print(x)

any(map(pari, l))


# l = [1,2,3,4,5,6,7,8]
# l = filter(pari, l)
# # l = map(lambda x : int(x / 2), l)
# # print(list(l))
# # print(list(map(pari, l)))
# print(v)
# print(all(map(pari, l)))

# print(any([True, False]))
# print(all([True, False]))


# print(list(map(pari,filter(pari, l))))



# l = [1,2,3,4,5,6,7,8]
# l = filter(pari, l)
# print(list(map(pari, l)))


class Iteratore:
    def __init__(self, l: int):
        self.l:int = l
        self.i = -1
        
    def next(self):
        self.i += 1
        return self.i < self.l
    def get(self):
        return self.i

iteratore = Iteratore(10)
while iteratore.next():
    print(iteratore.get())