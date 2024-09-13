import sys 
import os 
sys.path.append('../data_structure')
print(os.getcwd())
try:
    from linked_list_test import LinkedList, LinkedNode, DoublyLinkedNode, DoublyLinkedList
except ModuleNotFoundError:
    from data_structure.linked_list_test import LinkedList, LinkedNode, DoubcdlyLinkedNode, DoublyLinkedList

class Queue:
    def __init__(self, *elements, backend = list):
        assert isinstance(elements, list) or isinstance(elements, tuple)
        # self.elems = elements # 오류 발생?   
        self.backend = backend # Q1 )) self.elements 없어도 돼?
        if self.backend == list:
            self.list = list(elements)
        elif self.backend == LinkedList:
            self.linked_list = LinkedList(elements)
            
        


    def elements(self):
        if self.backend == list:
            return self.list
        elif self.backend == LinkedList:
            result = []
            current_node = self.linked_list.head
            # for _ in range(self.linked_list.size):
            while current_node is not None:
                assert isinstance(current_node, LinkedNode), current_node
                result.append(current_node.datum)
                current_node = current_node.next
            # print('End: ', self.linked_list.end.datum)
            return result
        

    def enqueue(self, elem): #Queue 의 끝에 추가하는 거
        print('before:', self.elements())
        if self.backend == list:
            self.list = self.list + [elem]
        elif self.backend == LinkedList:
            if not isinstance(elem, LinkedNode):
                new_node = LinkedNode(node_id=1, datum = elem, next = None)
            new_node.next = self.linked_list.head
            self.linked_list.head = new_node
            self.linked_list.size += 1
        print('after:', self.elements())
        

            #Q3 ))이거 왜 안나오는지? 나오게 하려면?? 
            
                  
    def dequeue(self): #dequeue 가장오래된 걸 빼! 
        if self.backend == list:
            if not self.list:
                raise IndexError("Queue is empty")
            # del_value = self.list[0]
            return self.list.pop() 

            #return del_value
            
        elif self.backend == LinkedList:
            prev = self.linked_list.head
            old_end = self.linked_list.end 
            while prev.next != self.linked_list.end:
                prev = prev.next
            prev.next = None 
            return 

    def front(self):
        if self.backend == list:
            if self.list == []:
                return None
            return self.list[0] # list 일 경우에도 빈리스트일경우 raise IndexError 해야함?
               
        elif self.backend == LinkedList:
            if self.linked_list.head is None:
                raise IndexError("Queue is empty")
            print("Front: ", self.linked_list.head.datum) #Q4 ))왜 안노오나요ㅠㅠㅠㅠ
            return self.linked_list.head.datum

    def size(self):
        if self.backend == list:
            return len(self.list)
        elif self.backend == LinkedList:
            return self.linked_list.size


    def is_empty(self): #비어있으면 True, 뭔가 있으면 False 
        if self.backend == list:
            return self.list == []
        elif self.backend == LinkedList:
            return self.linked_list.head is None
        else:
            raise ValueError


#현재 객체의 요소들을 반환하는 메서드 self.elementS()
    def __str__(self):
        res = ''
        res += '[front]'

        for elem in self.elements()[::-1]:
            res += '-' + str(elem)
        
        return res 
    

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.elements == other.elements 
        return False 

class PriorityQueue:
    def __init__(self, *elements_with_priority, backend = list):
        """Get list of 2-tuple containing (obj, number), which denotes object and its priority. Higher the number, the element have hight priority. 
        """
        
    def elements(self):
        if self.backend == list:
            return self.list 

    def enqueue(self, elem):
        if self.backend == list:
            self.list.append(elem)

    def dequeue(self):
        if self.backend == list:
            return self.list.pop()
                
    def front(self):
        if self.backend == list:
            return self.list[-1]

    def size(self):
        if self.backend == list:
            return len(self.list)
    
    def is_empty(self):
        if self.backend == list:
            return self.list == []

    def __str__(self):
        return str(self.elements())

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.elements == other.elements 
        return False 

if __name__ == '__main__':
    available_backends = [LinkedList] #, LinkedList] # , DoublyLinkedList]

    for backend in available_backends:
        # q1 = Queue(1,2,3,4, backend = backend)
        # # print(q1)
        # # print(str(q1))
        # # print(Queue.__str__(q1))
        # assert q1.elements() == [1,2,3,4]

        # # print('149: ', q1.enqueue(22))
        # # print('150: ', q1.elements())
        # # print(q1.front())

        # assert q1.size() == 4
        # print('161:' ,q1)
        # q1.enqueue(5)
        # print('163: ', q1)
        # assert q1.elements() == [5,1,2,3,4], q1.elements()
        # assert q1.size() == 5
        # assert q1.dequeue() == 4, print(q1.dequeue)
        # assert q1.size() == 4
        # assert q1.elements() == [5,1,2,3]
        # assert q1.front() == 3 
        
        q1=Queue(1,2,3,4)
        print(q1.dequeue())

        # q2 = Queue(backend = backend)

        # assert q2.elements() == []
        # assert q2.size() == 0
        # assert q2.is_empty()
        
        # q2.enqueue(1)

        # assert q2.elements() == [1]
        # assert q2.size() == 1
        # assert not q2.is_empty()
        
        # if backend == LinkedList:
        #     print(q1.linked_list, q2.linked_list)
    
        # q2 = PriorityQueue(('c',1), ('d',4), ('e',2), ('b',3), backend = backend)

        # assert q2.elements() == [('c',1), ('e',2), ('b',3), ('d',4)]
        # assert q2.size() == 4 
        # assert q2.front() == ('d', 4) 
        # assert not q2.is_empty()
        # q2.dequeue()

        # assert q2.elements() == [('c',1), ('e',2), ('b',3)]
        # assert q2.size() == 3 
        # assert q2.front() == ('b', 3) 
        # assert not q2.is_empty()

        # q2.dequeue()
        # q2.dequeue()
        # q2.dequeue()
        # q2.dequeue()

        # assert q2.is_empty()


