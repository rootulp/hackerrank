class BalancedBrackets(object):
    
    BRACKETS = {
        "{": "}",
        "[": "]",
        "(": ")"
    }
    
    @classmethod
    def is_balanced(cls, expression):
        stack = []
        for char in expression:
            if char in cls.BRACKETS:
                stack.append(char)
            elif not stack or cls.BRACKETS.get(stack.pop()) != char:
                return False
        return not stack


NUM_CASES = int(input().strip())
for _ in range(NUM_CASES):
    expression = input().strip()
    if BalancedBrackets.is_balanced(expression):
        print("YES")
    else:
        print("NO")
