class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(":")", "[":"]", "{":"}"}
        stack = []

        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if len(stack) > 0:
                    x = stack.pop()
                else:
                    return False
                if dic[x] != i:
                    return False

        if len(stack) == 0:
            return True
        return False
