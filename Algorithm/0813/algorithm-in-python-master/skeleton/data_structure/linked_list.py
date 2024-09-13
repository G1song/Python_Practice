try:
    from node import Node 
except ModuleNotFoundError:
    from data_structure.node import Node
# res = []
# a = LinkedNode()
# a.node_id = node_id
class LinkedNode: # (= class Node)
    def __init__(self, node_id, datum, next = None):
        self.node_id = node_id 
        self.datum = datum #노드가 저장하는 데이터
        self.next = next #다음 노드 

#LinkedList라는 자료구조를 만들 함수들을 추가해야 함. 
#LinkedList는 LinkedNode를 여러 개 모아 연결된 리스트를 만들어주는클래스
#주요기능: 삽입, 출력, 삭제, 탐색 

class LinkedList:
    def __init__(self, elements):
        # print('elements in LinkedList.__init__()', elements, type(elements))
        if elements == []:    #elements 가 비어있다면
            self.head = None  #연결리스트의 첫 번째 노드를 가리킴
            self.tail = None  #연결리스트의 마지막 노드
            self.end = None 
            self.size = 0     #연결리스트의 노드 개수 저장 
        else: #비어있지 않다면 #elements는 리스트 혹은 튜플이다..
            elements = list(elements)
            if not isinstance(elements, LinkedNode): 
                idx = len(elements)
                for i in range(len(elements)):
                    elements[i] = LinkedNode(idx, elements[i])
                    idx -= 1

                for n in range(len(elements)):
                    if n == len(elements)-1:
                        break
                    # n += 1
                    elements[-n].next = elements[-n-1]
                # 질문:  32번 for n in range(1, len(elements)+1)이라고 하면 
                #n=1 부터 시작이니까 elements[-0] 의 오류를 방지할 수 있지 않을까?
                
                self.head = elements[-1]
                self.tail = LinkedList(elements[-2::-1])
                self.end = elements[0]
                self.size = len(elements)
                

            # for i, e in enumerate(elements):
            #     elements[i] = LinkedNode(i+1, e)    
            
 

    def __iter__(self):
        yield None 

  


    def __str__(self):
        res = ''

        return res 

class DoublyLinkedNode(Node):
    def __init__(self, node_id, datum, prev = None, next = None):
        self.node_id = node_id 
        self.datum = datum
        self.next = next 
        self.prev = prev 

class DoublyLinkedList:
    def __init__(self, elements):
        if elements == []:
            self.head = None 
            self.tail = None 
            self.end = None
            self.size = 0
        else:
            self.head = None 
            self.tail = None 
            self.end = None
            self.size = 0

    def __iter__(self):
        yield None 

    def __str__(self):
        res = ''

        return res 

if __name__ == '__main__':
    lst = LinkedList([1,2,3,4])
    print(lst.head.datum)
    print(lst.head.next.datum)
    print(lst.head.next.next.datum)
    print(lst.head.next.next.next.datum)
    print(lst.head.next.next.next.next is None)
    # assert lst.front() == 4
    # assert lst.head.datum == 4 
    # assert lst.head.next.datum == 3 
    # assert lst.head.next.next.datum == 2
    # assert lst.head.next.next.next.datum == 1
    # assert lst.head.next.next.next.next is None 

    # assert lst.end.datum == 1  