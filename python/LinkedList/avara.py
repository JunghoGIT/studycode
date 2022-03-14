class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(name,num):
    """
    문자열 형태의 이름과 계산할 정수를 인자로 받아서 정수의 각 자리별 역순으로 ListNode 생성

    :param name: 노드 인스턴스의 이름 접두사
    :param num: 저장될 정수
    :return: head node
    """
    n = [int(number) for number in str(num)]  # 숫자를 문자열로 변경 후 각 요소를 리스트에 저장
    globals()[f'{name}_{len(n)}'] = ListNode(n[0])  # 가장 큰 자리수를 tail 노드에 저장
    for i in range(1, len(n)):
        globals()[f'{name}_{len(n)-i}'] = ListNode(n[i], globals()[f'{name}_{len(n)-i+1}'])  # head 까지 노드 인스턴스 생성

    return globals()[f'{name}_1'] # head 노드 반환


class Solution(object):

    def get_number_from_linked_list(node):
        """
        연결된 노드의 데이터를 head 부터 tail 까지 병합 하고 reverse 함으로서 연결리스트화 하기 전 정수 구하기
        :param node: head node
        :return: 계산할 정수
        """
        int_list = []
        while True:
            int_list.append(str(node.val))  # insert 사용시 시간복잡도 증가, 대신 reverse 함수 사용
            node = node.next
            if not node.next: # tail node 체크
                int_list.append(str(node.val))  # join 을 사용하기 위해서 문자열 형태로 변환
                break
        int_list.reverse()  # 계산을 위해 역순이었던 노드 데이터를 리버스
        number = int("".join(int_list))  # 문자열 형태로 저장되어 있던 리스트 요소를 하나의 문자열로 합친 후 정수형으로 변환

        return number

    @staticmethod
    def addTwoNumbers(l1, l2):

        l1_num = Solution.get_number_from_linked_list(l1) # 연결리스트의 정수
        l2_num = Solution.get_number_from_linked_list(l2)
        result_num = l1_num + l2_num # 두 연결 리스트의 정수를 덧셈
        result_head = create_linked_list('result', result_num) # 덧셈 결과 값을 연결리스트로 자리별 역순으로 저장 후 head 노드 반환

        return result_head


def check_answer(node):
    answer = []
    while True:
        answer.append(node.val)
        node = node.next
        if not node.next:
            answer.append(node.val)
            break
    print(answer)

# 예제 1
# l1 = create_linked_list('node_l1', 9999999)
# l2 = create_linked_list('node_l2', 9999)


l1_head = create_linked_list('node_l1', 9999999)
l2_head = create_linked_list('node_l2', 9999)
result = Solution.addTwoNumbers(l1_head, l2_head)

check_answer(l1_head)
check_answer(l2_head)
check_answer(result)

"""
문제 풀이
    
    addTwoNumbers 의 인자 타입과 반환 타입이 ListNode 형태임으로 연결리스트 클래스를 구현하여 푸는 문제가 아닌, 노드 클래스만을 이용하여
    푸는 문제라 추측 했습니다.
    그렇기에 첫 번째로 각 노드를 생성하고 연결할 함수가 필요하다고 생각했고,
    두 번째로 함수의 인자 형을 맞추기 위해서 head 노드 만을 사용하여 푸는 것이 올바른 과정이라고 판단 했습니다.
    
    추가로 연결 리스트의 각 데이터가 역순으로 저장된다는 점은 각 노드를 head 부터 계산 할 시 일반적인 덧셈 순서대로 되도록 유도 하신 것 같습니다.
    하지만 그것보단 정수의 자릿수대로 흩어져있는 데이터를 모아서 하나의 정수로 만든 후 계산 하는 것이 시간 복잡도에서도 그닥 차이가 없으며,
    직관적인 방법이라고 판단 했습니다.
    
문제 후기 및 감사 인사
    
    문제를 풀면서 자료구조나 python 문법을 공부할 수 있는 좋은 시간이었습니다.
    변수나 함수명은 아마 카멜케이스를 선호하시는 듯 하여 저도 사용해볼까 하다가 어색하여 평소 쓰던 방식대로 했습니다.
    양해 부탁드립니다.
    답은 출력되지만 완벽히 좋은 코드라고 생각 되지 않습니다.
    더 좋은 코드에 대한 피드백이 있으시다면 메일로 답장 부탁 드리겠습니다.
    감사합니다 !
"""