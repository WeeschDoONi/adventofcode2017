def read_line(file_name):
    with open(file_name, 'r') as data:
        return data.read().strip()
    
def read_lines(file_name):
    with open(file_name, 'r') as data:
        return data.readlines()