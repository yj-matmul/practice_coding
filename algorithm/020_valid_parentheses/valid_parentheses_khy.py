class Solution:
    def isValid(self, s: 'str') -> 'bool':
        dp2 = []
        lstr = list(s)
        for i in lstr:
            print(i)
            if i in ["{", "(", "["]:
                dp2.append(i)
            elif i in ["]", ")", "}"] and len(dp2) != 0:

                if i == ")" and dp2[-1] == "(":
                    dp2.pop()

                elif i == "]" and dp2[-1] == "[":
                    dp2.pop()

                elif i == "}" and dp2[-1] == "{":
                    dp2.pop()

                else:
                    return False
            else:
                return False

        if len(dp2) == 0:
            return True

        else:
            return False