class nodo:
    def __init__(self,value):
        self.value=value
        self.next=None

    def __str__(self):
        return str(self.value)
    
class LinkList:
    def __init__(self):
        self.first=None
        self.size=0

    def Append(self,value):
        Mynode=nodo(value)
        if self.size==0:
            self.first=Mynode
        else:
            Current=self.first
            while Current.next!=None:
                Current=Current.next
            Current.next=Mynode
        self.size+=1
        return Mynode
    def remove(self,value):
        if self.size==0:
            return False
        else:
            Current=self.first
            try:
                while Current.next.value!=value:
                    if Current.next==None:
                        return False
                    else:
                        Current=Current.next
                deletenode=Current.next
                Current.next=deletenode.next
            except AttributeError:
                return False
            self.size-=1
        return deletenode
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        string="["
        Current=self.first
        for i in range(len(self)):
            string+=str(Current)
            if i !=len(self)-1:
                string+=str(",")
            Current=Current.next
        string+=("]")
        return string
    
mylist=LinkList()
mylist.Append(1)
mylist.Append([])
mylist.Append("f")
mylist.Append(3 )
print(type(mylist))
print(mylist)
mylist.remove(3)
print(mylist)