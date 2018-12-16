class TextEditor:

    def __init__(self):
        self.text = []

    def append(self, string_to_append):
        self.text.append(self.peek() + string_to_append)

    def delete(self, num_chars_to_delete):
        self.text.append(self.peek()[:-num_chars_to_delete])

    def char_at_position(self, k):
        return self.peek()[k - 1]

    def undo(self):
        self.text.pop()

    def peek(self):
        if self.text:
            return self.text[-1]
        else:
            return ''


n = int(input().strip())
text_editor = TextEditor()
for _ in range(n):
    command = input().strip().split(' ')
    if command[0] == '1':
        text_editor.append(command[1])
    elif command[0] == '2':
        text_editor.delete(int(command[1]))
    elif command[0] == '3':
        print(text_editor.char_at_position(int(command[1])))
    elif command[0] == '4':
        text_editor.undo()
