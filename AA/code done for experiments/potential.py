import re
import random

def analyze_python_code(file_path):
    append_pattern = re.compile(r'\.append\s*\(')
    count_pattern = re.compile(r'\.count\s*\(')

    append_count = 0
    count_count = 0

    push_count = 0
    pop_count = 0

    potential = 0

    with open(file_path, 'r') as file:
        for line in file:
            append_count += len(append_pattern.findall(line))
            count_count += len(count_pattern.findall(line))

            push_count += line.count('push(')
            pop_count += line.count('pop(')

            potential += 2 * line.count('push(') - line.count('pop(')

    if append_count + count_count > push_count + pop_count:
        data_structure = 'Array'
    else:
        data_structure = 'Stack'

    print("Input file is python")
    print(f'Data Structure Used: {data_structure}')
    print(f'Array Operations (append, count): ({append_count}, {count_count})')
    print(f'Stack Operations (push, pop): ({push_count}, {pop_count})')

    print("Potential Cost:", potential)

    return append_count, count_count, push_count, pop_count

def analyze_c_code(file_path):
    array_declaration_pattern = re.compile(r'\b(?:int|float|char)\s+[a-zA-Z_][a-zA-Z0-9_]*\s*\[\s*\d*\s*\]\s*;')
    push_count = 0
    pop_count = 0

    potential = 0

    with open(file_path, 'r') as file:
        array_declaration_count = 0
        for line in file:
            push_count += line.count('push(')
            pop_count += line.count('pop(')
            array_declaration_count += len(array_declaration_pattern.findall(line))

            potential += 2 * line.count('push(') - line.count('pop(')

    print("Input file is C")
    print(f'Data Structure Used: Array')
    print(f'Array Declaration Count: {array_declaration_count}')
    print(f'Stack Operations (push, pop): ({push_count}, {pop_count})')

    print("Potential Cost:", potential)

    return array_declaration_count, push_count, pop_count

def get_file_extension(file_path):
    return file_path.split('.')[-1].lower()

def main():
    file_path = input("Enter the path to the code file: ")
    file_extension = get_file_extension(file_path)

    if file_extension == 'py':
        analyze_python_code(file_path)
    elif file_extension == 'c':
        analyze_c_code(file_path)
    else:
        print("Unsupported file type. Please provide a Python (.py) or C (.c) file.")

if __name__ == "__main__":
    main()
