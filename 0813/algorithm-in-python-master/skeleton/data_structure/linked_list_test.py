try:
    from node import Node 
except ModuleNotFoundError:
    from data_structure.node import Node

class LinkedNode:
    def __init__(self, node_id, datum, next = None):
        self.node_id = node_id 
        self.datum = datum
        self.next = next 

class LinkedList:
    def __init__(self, elements):
        if elements == []:
            self.head = None 
            self.tail = None 
            self.end = None
            self.size = 0
        else: 
            #노드만들기
            if not isinstance(elements, list):
                elements = list(elements)
            for i in range(len(elements)):
                if not isinstance(elements[i], LinkedNode):
                    elements[i] = LinkedNode(i+1, elements[i])  #얘도 그럼node_id 에 아무거나 가능?
                    
            self.head = elements[0]
            self.tail = LinkedList(elements[1:])
            self.end = elements[-1]
            self.size = len(elements)
            #next 구하기
            for j in range(len(elements)-1):
                elements[j].next = elements[j+1]
            # for j in range(len(elements)):
            #     if j == len(elements)-1:
            #         break 
            #     elements[j].next = elements[j+1]
            elements[-1].next = None
            
            # 23번 i = 1있어야함? 없어도 될 거 같은데 
            #Q? self.next 가 안되는이유?? self는 Linkedlist 잡채잖아. next는 node가 필요

  
        
                   
         
            

    
    def __iter__(self):
        yield None

    def __str__(self): # 링크드리스트 안에 뭐가 있는지 
        return 'hello world'


class DoublyLinkedNode(Node):
    def __init__(self, node_id, datum, prev = None, next = None):
        self.node_id = node_id 
        self.datum = datum
        self.next = next 
        self.prev = prev 

class DoublyLinkedList:
    def __init__(self, elements):
        if elements is None:
            elements = []
        elements = list(elements)

        if not elements:
            self.head = None
            self.tail = None
            self.size = 0
       
        else:
            for idx, elem in enumerate(elements):
                if not isinstance(elem, DoublyLinkedNode):
                   elements[idx] = DoublyLinkedNode(idx, elem)
                    
            self.head = elements[0]
            self.end = elements[-1]

            for idx, elem in enumerate(elements):
                if idx == len(elements)-1:
                    elem.next = None
                else:  
                    elem.next = elements[idx+1]

            for idx, elem in enumerate(elements):
                if idx == 0:
                    elem.prev = None
                else:  
                    elem.prev = elements[idx-1]
                
            self.tail = DoublyLinkedList(elements[1:])
            self.size = len(elements)  

    def add_to_head(self, elem):
        new_node = DoublyLinkedNode(0, elem)
        
        if self.head is None:
            self.head = new_node
            self.end = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            
        self.size += 1

    def delete_from_back(self):
        if self.size == 0:
            return None

        deleted_node = self.end

        if self.size == 1:
            self.head = None
            self.end = None
        else:
            self.end = self.end.prev
            self.end.next = None

        self.size -= 1
        return deleted_node.datum
        
    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.datum
            current = current.next

    def __str__(self):
        res = []
        current = self.head
        while current is not None:
            res.append(str(current.datum))
            current = current.next
        return ' -> '.join(res) 

if __name__ == '__main__':
    lst = LinkedList([1,2,3,4])

    print(lst) 
    print(LinkedList.__str__(lst))
    str(lst)
    LinkedList.__str__(lst)

    print(lst.head.datum)
    print(lst.head.next.next.next.datum)
    print(lst.head.next.next.next.next is None)
    # assert lst.front() == 4
    assert lst.head.datum == 1 
    assert lst.head.next.datum == 2 
    assert lst.head.next.next.datum == 3
    assert lst.head.next.next.next.datum == 4
    assert lst.head.next.next.next.next is None 
    