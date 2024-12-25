lista : list[int] 
list = [5]


ls : list[float]
ls.append(1.0)
ls.append(2.0)
ls.append(3.0)
print(ls)

class LinkItem[T]:
    def __init__(self, value: T):
        self.value = value
        self.next_item : LinkItem[T] | None = None



class LinkList[T]:
    def __init__(self):
        self.first_item : LinkItem[T] | None = None

    def last_item(self) -> LinkItem[T] | None:
        if self.first_item == None: return None
        e = self.first_item
        while e.next_item != None:
            e = e.next_item
        return e
    
    def append(self, value: T):
        last_item = self.last_item()
        if last_item != None:
            last_item.next_item = LinkItem[T](value)
        else:
            self.first_item = LinkItem[T](value)

    def print(self):
        print(self.first_item)



l : LinkList[float] = LinkList()
l.append(1.0)
l.append(2.0)
l.append(3.0)
l.print()