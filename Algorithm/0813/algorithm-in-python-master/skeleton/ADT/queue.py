import sys 
import os 
sys.path.append('../data_structure')
print(os.getcwd())
try:
    from linked_list_test import LinkedList, LinkedNode, DoublyLinkedNode, DoublyLinkedList
except ModuleNotFoundError:
    from data_structure.linked_list_test import LinkedList, LinkedNode, DoublyLinkedNode, DoublyLinkedList

class Queue:
    def __init__(self, *elements, backend = list):
        assert isinstance(elements, list) or isinstance(elements, tuple)
        # print('elements in Queue.__init__()', elements, type(elements))
        self.backend = backend
        if self.backend == list:
            self.list = list(elements)
        elif self.backend == LinkedList:
            self.linked_list = LinkedList(elements)
            print(self.linked_list.end.datum) # make right linked list 
            #LinkedList class 를 사용한다는 게 알아서 linkedlist 가 만들어진다는 건가? 
            #*elements 가 아니고 그냥 elements 임 *을 붙이면 elements 하나씩 풀어서 넣어버림. 
            
    def elements(self):
        if self.backend == list:
            return self.list
        elif self.backend == LinkedList: 
            result = []
            current_node = self.linked_list.head #(리스트가 아니니까 head지정필요)
            for i in range(self.linked_list.size):
                assert isinstance(current_node, LinkedNode), current_node
                #assert문법: 'assert 조건식, 조건이 거짓일 때의 메세지' 
                result.append(current_node.datum)
                current_node = current_node.next
            # return self.linked_list
            return result 
        
            #current_node = self.head
            # for i in range(self.linked_list.size):
            #     return self.linked_list
            

    def enqueue(self, elem): #Queue 의 끝에 추가하는 거
        if self.backend == list:
            self.list = self.list + [elem]
        elif self.backend == LinkedList:
            if not isinstance(elem, LinkedNode):
            # LinkedNode 각각의 순서인자 node_id, datum 을 정해줘야하는뎅.. 모르겟음 
                new_node = LinkedNode(node_id = self.linked_list.end.node_id + 1, datum = elem, next = None)
            #0821Q내 코드  (??질문// 내코드와 강사님 코드의 순서!! 이 순서가 왜 이순서인지)
            # self.linked_list.end.next = new_node 
            # self.linked_list.end = new_node
            # new_node.next = None
            # self.linked_list.size += 1 
            #강사님 코드 
            new_node.next = self.linked_list.head 
            self.linked_list.head = new_node
            self.linked_list.size += 1 

                  
    def dequeue(self): #dequeue 가장오래된 걸 빼! 
        if self.backend == list: 
            if not self.list: #리스트가 비어있다면
                raise IndexError("Queue is empty")
            return self.list.pop(0) 
        elif self.backend == LinkedList: #if isinstance 가 필요가없지 노드를 그냥 빼는거니까
            if self.linked_list.head is None:  # head가 None인지 확인
                raise IndexError("Queue is empty")
            else: #queue가 비어있지 않다면 
                old_end = self.linked_list.end
                self.linked_list.end = old_end.next 
                self.linked_list.size -= 1 
            return old_end.datum

 #head 는 연결리스트의 용어, front 는 queue의 용어 두 개는 다른 층위의 개념. 
    def front(self):
        if self.backend == list:
            return self.list[0] # 0821Q==list 일 경우에도 빈리스트일경우 raise IndexError 해야함? 
        elif self.backend == LinkedList:
            if self.linked_list.head is None:  # head가 None인지 확인
                raise IndexError("Queue is empty") 
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
        q1 = Queue(1,2,3,4, backend = backend)
        # print(q1)
        # print(str(q1))
        # print(Queue.__str__(q1))
        assert q1.elements() == [1,2,3,4]
    
        assert q1.size() == 4
        print(q1)
        q1.enqueue(5)
        print(q1)
        assert q1.elements() == [5,1,2,3,4], q1.elements()
        assert q1.size() == 5
        assert q1.dequeue() == 4
        assert q1.size() == 4
        assert q1.elements() == [5,1,2,3]
        assert q1.front() == 3 


        q2 = Queue(backend = backend)

        assert q2.elements() == []
        assert q2.size() == 0
        assert q2.is_empty()
        
        q2.enqueue(1)

        assert q2.elements() == [1]
        assert q2.size() == 1
        assert not q2.is_empty()
        
        if backend == LinkedList:
            print(q1.linked_list, q2.linked_list)
    
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


