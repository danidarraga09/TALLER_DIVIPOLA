class Node:
    def __init__(self,id,name):
        self.id=id
        self.name=name
        self.next=None
        self.prev=None
        self.sub_list= None #apunta a otra linked list

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def add_child(self,parent=None,child=None):
        if parent.sub_list is None:
            sublist=LinkedList()
            self.head=child
            self.head=child
            parent.sub_list=sublist
        else:
            current=parent.sub_list.tail
            current.next=child
            child.prev=current
            parent.sub_list.tail=child
        return parent.sub_list
    
    def search_att(self,attr,value):
        current=self.head
        while current:
            if getattr(current,attr)== value:
                return current
            current=current.next
        return None

    def update(self,search_value,**attrs):
        node = self.search.id(search_value)
        if node:
            for k,v in attrs.items():
                setattr(node,k,v)
            return True
        return False 
    
    def delete_id(self,search_value):
        current=self.head
        while current:
            if current==search_value:
                if current.prev: #Si hay uno nodo antes
                    current.prev.next=current.next
                else:
                    self.head=current.next
                if current.next: #si hay un nodo despues
                    current.next.prev=current.prev #para conectar en der a izq
                else:
                    self.tail=current.prev #si no hay el anterior del actual va a ser la cola
                return True 
            current=current.next
        return False 
    
    def printmulti_list(self,level=0):
        if self.head is None:
            print("Empty list"); return
        current = self.head
        while current:
            print(\"  \" * level + str(current))
            if current.sub_list:
                current.sub_list.print_multilinked_list(level + 1)
            current = current.next


