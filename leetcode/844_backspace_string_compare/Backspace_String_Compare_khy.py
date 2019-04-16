class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        #함수정의
        def stack_str(string):
            stack = []
            for s in string:
                try:
                    if s == "#":
                        stack.pop()

                    else:
                        stack.append(s)

                except:
                    pass

            return stack
        #실행
        stack_S = stack_str(S)
        stack_T = stack_str(T)

        #비교
        if stack_S == stack_T:
            result = True

        else:
            result = False

        return result
