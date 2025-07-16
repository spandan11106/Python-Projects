def read_file(filename = "task.txt"):
    """ Reads the text file and returns the list of to-do items."""
    try:
        with open(filename, 'r') as txt:
            return txt.readlines()
    except FileNotFoundError:
        return []

def write_file(updated, filename = "task.txt"):
    """ Writes the updated to-do items in the text file. """
    with open(filename, 'w') as file:
        file.writelines(updated)

