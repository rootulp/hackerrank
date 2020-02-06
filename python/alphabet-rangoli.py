import string

class Rangoli:

    DASH = "-"
    ALPHABET = string.ascii_lowercase
    def __init__(self, size):
        self.size = size
        self.num_lines = self.size * 2 - 1
        self.line_length = self.num_lines * 2 - 1
        self.middle_line_num = (self.num_lines - 1) // 2

    def __str__(self):
        return "\n".join([self.line(line_number) for line_number in range(0, self.num_lines)])

    def line(self, line_number):
        return self.center_text(self.pattern(line_number))

    def pattern(self, line_number):
        num_lines_away_from_middle = abs(self.middle_line_num - line_number)
        pattern = ""
        for i in range(self.middle_line_num, num_lines_away_from_middle, -1):
            pattern += self.ALPHABET[i] + self.DASH

        pattern += self.ALPHABET[num_lines_away_from_middle]

        for i in range(num_lines_away_from_middle + 1, self.middle_line_num + 1):
            pattern += self.DASH + self.ALPHABET[i]

        return pattern


    def center_text(self, text):
        return '{:{fill}^{line_length}}'.format(text, fill=self.DASH, line_length=self.line_length)


def print_rangoli(size):
    rangoli = Rangoli(size)
    print(rangoli)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
