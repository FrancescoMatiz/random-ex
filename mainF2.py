


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
        stampato : LinkItem[T] | None= self.first_item
        while stampato != None:
            print(stampato.value)
            stampato = stampato.next_item

    def remove_at(self,index : int):
        pass
        # ds : LinkItem[T] | None= self.first_item
        # it : int = 0
        # while it != index  and  ds != None:
        #     it += 1
        #     ds = ds.next_item
        


ls : list[float] = []
for e in ls:
    print(e)

l : LinkList[float] = LinkList()

l.print()