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
    def display(self):
        if self.head is None:
            print("linked list is empty")
        else:
            temp=self.head
            while temp!=None:
                if temp.next!=None:
                    print(temp.data,"->",end="")
                else:
                    print(temp.data)
                temp=temp.next
            print()
    def median(self):
        length=self.length()
        current=self.head
        counter=(length//2-1)
        while counter!=0:
            current=current.next
            counter-=1
        if length%2==0:
            print("median",(current.data+current.next.data)/2)
        else:
           print("median",current.next.data)
            
        '''slow=self.head
        fast=self.head
        while(slow and fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        print("median:",slow.data)'''
    def reverse(self):
        '''temp=self.head
        l=[]
        while(temp!=None):
            l.append(temp.data)
            temp=temp.next
        l=l[::-1]
        print(l)'''
        prev=None
        next=None
        cur=self.head
        while(cur!=None):
            next = cur.next
            cur.next=prev
            prev=cur
            cur=next
        self.head =prev     
        self.display()
    def delete_middle(self):
        temp=self.head
        size=self.length()
        print(size)
        while(temp.next.data!=(size//2)):
            temp=temp.next
        if size%2==0:
             temp.next=temp.next.next
        else:
            temp.next=temp.next.next.next
        self.display()
    def length(self):
        temp=self.head
        count=0
        while(temp!=None):
            count+=1
            temp=temp.next
        return count
    def delete_position(self,n):
        temp=self.head.next
        prev=self.head
        for i in range(1,n-1):
            temp=temp.next
        print(prev.next.data)
        prev.next=temp.next
        print(temp.next.data)
        temp.next=None
        self.display()
    def insert_after(self,after_val,value_inserted):
        current=self.head
        while current.data!=after_val:
            current=current.next
        if current is None:
            print("After value doesn't exist")
        else:
            new_node=Node(value_inserted)
            new_node.next=current.next
            current.next=new_node
    #def delete_before_after(self,)
obj=singlell()
obj.creation()
obj.display()
obj.median()
#obj.reverse()
obj.length()
#obj.delete_middle()

obj.delete_position(3)
obj.insert_after(3,100)