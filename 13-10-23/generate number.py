class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlell:
    def __init__(self):
        self.head=None
    def creation(self):
        for i in range(1,7): 
            new_node=node(i)
            if self.head==None:
                self.head=new_node
            else:
                temp=self.head
                while(temp.next!=None):
                    temp=temp.next
                temp.next=new_node
    def create_number(self):
        st=""
        temp=self.head
        while(temp.next!=None):
            st+=str(temp.data)
            temp=temp.next
        print(st)
obj=singlell()
obj.creation()
obj.create_number()