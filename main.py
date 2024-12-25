
























class LinkItem[T]:
    def __init__(self, item : T):
        self.item = item
        self.next_item_link : LinkItem[T] | None = None
    def __repr__(self) -> str:
        return format(f"{self.item}")


class LinkList[T]:
    def __init__(self):
        self.first_element : LinkItem[T] | None = None
    
    def search_last_element(self):
        if self.first_element == None: return None
        e = self.first_element
        while e.next_item_link != None:
            e = e.next_item_link
        return e
    
    def append(self, t : T):
        elem = self.search_last_element()
        if elem == None:
            self.first_element = LinkItem(t)
        else:
            elem.next_item_link = LinkItem(t)
    
    def remove(self, index:int):
        pass
    
    def print(self):
        e = self.first_element
        while e != None:
            print(e)
            e = e.next_item_link


l : LinkList[float] = LinkList()
l.append(1.0)
l.append(2.0)
l.append(3.0)
l.print()
