FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return
    lis of to-do items"""
    with open(filepath, 'r') as local_file:
        local_todo = local_file.readlines()
    return local_todo


def write_todos(todos_arg,filepath=FILEPATH):
    """write items of a list in text file """
    with open(filepath, 'w') as file_arg:
        file_arg.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello You!")