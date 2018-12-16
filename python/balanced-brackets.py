class BracketChecker:

    def __init__(self, string_of_brackets):
        self.string_of_brackets = string_of_brackets

    def balanced_brackets(self):
        self.stack = []
        for bracket in string_of_brackets:
            if self.stack and self.matching_brackets(self.stack[-1], bracket):
                self.stack.pop()
            else:
                self.stack.append(bracket)
        return not self.stack

    @classmethod
    def matching_brackets(cls, bracket_1, bracket_2):
        return ((bracket_1 == '(' and bracket_2 == ')') or
                (bracket_1 == '[' and bracket_2 == ']') or
                (bracket_1 == '{' and bracket_2 == '}'))


n = int(input().strip())
for _ in range(n):
    string_of_brackets = input().strip()
    if (BracketChecker(string_of_brackets).balanced_brackets()):
        print('YES')
    else:
        print('NO')
