1class Solution(object):
2    def isValid(self, s):
3        """
4        :type s: str
5        :rtype: bool
6        """
7        stack = []
8
9        close_to_open = {
10            ")" : "(",
11            "}" : "{",
12            "]" : "["
13        }
14
15        for char in s:
16            #if its a CLOSING bracket
17            if char in close_to_open:
18                if not stack:
19                    return False
20                
21                top_char = stack.pop()
22
23                expected_opener = close_to_open[char]
24
25                if top_char != expected_opener:
26                    return False
27            
28            # if its an OPENING bracket
29            else:
30                stack.append(char)
31            
32        return len(stack) == 0
33        