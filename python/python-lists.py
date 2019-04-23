def parse(unparsed_command):
    command, *args = unparsed_command.split(" ")
    args = map(int, args)
    return (command, args)

def execute_command(current_list, parsed_command):
    command, args = parsed_command
    if command == "insert":
        current_list.insert(*args)
    elif command == "print":
        print(current_list)
    elif command == "remove":
        current_list.remove(*args)
    elif command == "append":
        current_list.append(*args)
    elif command == "sort":
        current_list.sort()
    elif command == "pop":
        current_list.pop()
    elif command == "reverse":
        current_list.reverse()

if __name__ == '__main__':
    current_list = []
    num_commands = int(input())
    for _command_index in range(num_commands):
        unparsed_command = input()
        parsed_command = parse(unparsed_command)
        execute_command(current_list, parsed_command)
