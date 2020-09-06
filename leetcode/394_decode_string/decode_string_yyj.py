class Solution:
    def decodeString(self, s: str) -> str:
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        num_stack = []
        char_stack = []
        substring = ''
        subnum = ''
        answer = ''

        for char in s:
            if char in nums:
                subnum += char
            elif char == '[':
                if not num_stack:
                    answer += ''.join(char_stack) + substring
                    char_stack = []
                num_stack.append(subnum)
                subnum = ''
                substring = ''
            elif char == ']':
                num = num_stack.pop()
                if char_stack and substring == '':
                    substring = ''.join(char_stack) + substring
                substring = substring * int(num)
                char_stack.append(substring)
                substring = ''
                if not num_stack:
                    answer += ''.join(char_stack) + substring
                    char_stack = []
            else:
                substring += char
            print(substring, char_stack, '\t', subnum, num_stack, '\t', answer)

        if len(substring) > 0:
            char_stack.append(substring)

        return answer