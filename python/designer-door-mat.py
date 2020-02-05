# Size: 7 x 21
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------


class DoorMat:

    DASH = "-"
    DOT = "."
    PIPE = "|"
    WELCOME = "WELCOME"

    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.middle_line_number = (self.N - 1) // 2

    def __str__(self):
        return "\n".join([self.line(line_number) for line_number in range(0, N)])

    def line(self, line_number):
        if(line_number == self.middle_line_number):
            return self.welcome_line()
        return self.design_line(line_number)

    def welcome_line(self):
        return self.center_text(self.WELCOME)

    def design_line(self, line_number):
        return self.center_text(self.design_for_line(line_number))

    def design_for_line(self, line_number):
        return self.DOT + self.middle_design(line_number) + self.DOT

    def middle_design(self, line_number):
        if(line_number == 0):
            return self.PIPE

        pattern = self.PIPE + self.DOT + self.DOT
        return pattern * self.pattern_repeat_for_line(line_number) + self.PIPE

    def pattern_repeat_for_line(self, line_number):
        if line_number < self.middle_line_number:
            return line_number * 2
        return (self.N - 1 - line_number) * 2

    def center_text(self, text):
        return '{:{fill}^{line_length}}'.format(text, fill=self.DASH, line_length=self.M)


N, M = map(int, input().strip().split(" "))
doormat = DoorMat(N, M)
print(doormat)
