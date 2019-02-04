def compare_file_contents(first, second):
    first_content = _readfile(first)
    second_content = _readfile(second)

    return first_content == second_content


def _readfile(filename):
    content = ''
    with open(filename, 'r') as f:
        content = f.read()

    return content
