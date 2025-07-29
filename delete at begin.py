#Delete at begin


class Node:
    def __init__(s,data):
        s.data=data
        s.prev=None
        s.next=None
class DLL:
    
    def __init__(s):
        s.head=None
    def iab(s,data):
        newnode=Node(data)
        newnode.next=s.head
        if s.head:
            s.head.prev=newnode
        s.head=newnode 
    def dab(s):
        if not s.head:
            print("Cant perform delete in an empty list...")
        print(f"deleted:{s.head.data}")
        s.head=s.head.next
        if s.head:
            s.head.prev=None
    def display(s):
        temp=s.head
        print("Double Linked List:")
        while temp:
            print(temp.data,end="<->")
            temp=temp.next
        print("None")
dll=DLL()
n=int(input("enter the no of elements to insert at begin:"))
for i in range(n):
    val=int(input(f"enter element {i+1}:"))
    dll.iab(val)
dll.display()
d=int(input("\n how many times you want to perform delete op:"))
for _ in range(d):
    dll.dab()
    dll.display()








