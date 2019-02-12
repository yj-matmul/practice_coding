class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        try:

            dummy = cur = ListNode(0)
            # dp설정
            dp = head.val #제일 처음 값(빈칸이 안만들어져서 1번부터 시작)
            nextnode = ListNode(0) #다음 노드가 될 값을 담을 곳
            nextnode.next = ListNode(dp) #(dp와 같은 이유로 1번부터 셋팅)
            duplication = 0 #이전 노드가 중복인지 여부
            head = head.next #2번 노드부터 시작

            while head:

                if head.val == dp: #중복값인가?
                    nextnode = ListNode(0)
                    duplication = 1

                if duplication == 0 and nextnode.next: #이전 노드가 중복값이 아닌경우 저장해 둔 노드 연결
                    cur.next = nextnode.next
                    cur = cur.next

                if head.val != dp: #새로운 노드가 중복값이 아닌경우 노드 저장
                    nextnode.next = ListNode(head.val)
                    duplication = 0

                dp = head.val
                head = head.next

            #마지막 노드 연결 여부 판별
            if duplication == 0 and nextnode.next:
                cur.next = nextnode.next
                cur = cur.next

            return dummy.next

        except:
            return head