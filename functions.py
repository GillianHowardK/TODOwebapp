def get_todos(filepath="ToDos.txt"):
    """
    Reads a text file and returns the list of to-do items in a variable
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def alter_todos(todos_arg, filepath="/Users/Gillian/TODOwebapp/ToDos.txt"):
    """ Overwrites information in a text file using input stored in a variable """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)

