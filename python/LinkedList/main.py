class SLinkedList:

    class Node:
        def __init__(self, v, n = None):
            self.value = v
            self.next = n

    def __init__(self):
        self.head = None

    def printNode(self):
        if self.head is None:
            print("저장된 데이터가 없음")
            return
        else:
            print("<현재 리스트 구조>", end='\t')
            link = self.head

            while link :
                print(link.value, '->' , end = ' ')
                link = link.next
            print()

    def insertNode(self, v):
        if self.head is None:
            self.head = self.Node(v)
        else:

            self.head = self.Node(v, self.head)

    def deleteNode(self):
        if self.head is None:
            print("삭제할 노드가 없습니다.")
            return
        else:
            self.head = self.head.next

    def searchNode(self,v):
        if self.head is None:
            print("저장된 데이터가 없음")
            return
        else:
            link = self.head
            index  = 0
            while link:
                if v == link.value:
                    return index
                else:
                    link = link.next
                    index += 1

if __name__=="__main__":
    sl = SLinkedList()
    sl.insertNode('1st')
    sl.insertNode('2nd')
    sl.insertNode('3rd')

    print("<위치 탐색>")
    result = sl.searchNode('1st')
    print("1st의 위치 : {}".format(result))

    result = sl.searchNode('555')
    print("555의 위치 : {}".format(result))
