import operator
import re
from typing import List, Dict
import os
import shutil
import pprint
from pathlib import PurePath
import tempfile

#current_directory = PurePath()
current_directory = list()
folder_structure = {}

CD_RE = "\$ cd (.+)"
CD_RE_COMP = re.compile(CD_RE)
DIR_RE = "dir (.*)"
DIR_RE_COMP = re.compile(DIR_RE)

TMP_DIR = "/tmp/test"
pp = pprint.PrettyPrinter(indent=4)
directories = {}
dir_sizes = {}

total_system_memory = 70000000

def get_directory_size(directory, current_dir=''):
    global dir_sizes
    total = 0
    for key, value in directory.items():
        if type(value) is int:
            total += value
        if type(value) is dict:
            total += get_directory_size(value, os.path.join(current_dir, key))
            #p = os.path.join(current_dir, key)

    dir_sizes[current_dir] = total

    return total

def set_value(d: Dict, keys: List[str], value):
    parent = d
    n = d
    for key in keys[:-1]:
        n = n[key]
    if keys[-1] not in n:
        n[keys[-1]] = value
    else:
        n[keys[-1]].update(value)

def key_exists(d: Dict, keys: List[str]) -> bool:
    n = d
    for key in keys:
        if key in n:
            n = n[key]
        else:
            return False

    return True


def calc_dir_size(directory):
    total = 0
    for key, size in dir_sizes.items():
        if size <= 100000:
            total += size

    return total

def find_total_dir_size(dir_sizes):
    total = 0
    for dir_name, dir_size in dir_sizes.items():
        if dir_size <= 100000:
            total += dir_size

    print(f"Final: {total}")



def process_command(command: str, command_output: List[str]):
    global current_directory
    global folder_structure
    global directories
    print(f"Base Directory: {TMP_DIR}")
    if command.startswith("$ cd"):
        m = re.search(CD_RE_COMP, command)
        print(m.group(1))
        if m is not None:
            if m.group(1) == '..':
                # Go up a directory
                current_directory.pop()
            elif m.group(1)[0] == '/':
                # Go to the root directory
                current_directory = [TMP_DIR]
                set_value(directories, [TMP_DIR], {})
            else:
                # Go into a directory
                current_directory.append(m.group(1))
                #try:
                #    os.makedirs('/'.join(current_directory))
                #except FileExistsError:
                #    print(f"Folder: {'/'.join(current_directory)} exists")
                if not key_exists(directories, current_directory):
                    set_value(directories, current_directory, {})

            print(f"Current Directory: {current_directory}")
    elif command == "$ ls":
        for line in command_output:
            # new command, exit
            if line.startswith('$'):
                break
            elif line.startswith("dir"):
                # We have a new directory
                line_parts = line.split()
                folder = line_parts[1]
                #new_directory = '/'.join(current_directory + [folder])
                #try:
                #    os.makedirs(new_directory)
                #    print(f"Found directory: {new_directory}")
                if not key_exists(directories, current_directory + [folder]):
                    set_value(directories, current_directory, {folder: {}})
                #except FileExistsError:
                #    print(f"Folder {new_directory} exists.")
            elif line[0].isdigit():
                # We have a file
                file_parts = line.split(' ')
                #print(f"Found file of size {file_parts[0]} and name of {file_parts[1]}")
                #new_file = '/'.join(current_directory + [file_parts[1]])
                #with open(new_file, 'w') as fp:
                #    fp.write(file_parts[0])
                set_value(directories, current_directory, {file_parts[1]: int(file_parts[0])})

    else:
        print(f"Command not supported: {command}")

    print(folder_structure)

def main():
    data = '''
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
    '''
    with open("day7_input.txt", "r") as fp:
        data = fp.read()

    if os.path.exists(TMP_DIR):
        shutil.rmtree(TMP_DIR)

    os.makedirs(TMP_DIR)

    data_lines = data.split('\n')
    for idx, data in enumerate(data_lines):
        if data == '':
            continue
        if data[0] == '$':
            process_command(data, data_lines[idx+1:])

    pp.pprint(directories)
    total_size = get_directory_size(directories['/tmp/test'], '/tmp/test')
    #print(f"Total size: {total_size}")
    pp.pprint(dir_sizes)
    #dir_sizes = calc_dir_size(TMP_DIR)
    #find_total_dir_size(dir_sizes)
    size = calc_dir_size(dir_sizes)
    print(f"Total size: {size}")
    unused_space = total_system_memory - total_size
    print(f"Disk space Used: {total_size}/{total_system_memory} space left = {unused_space}")
    space_needed = 30000000 - unused_space
    print(f"Additional space needed for update: {space_needed}")

    directories_big_enough = dict()
    for dir_name, dir_size in dir_sizes.items():
        if dir_size >= space_needed:
            directories_big_enough[dir_name] = dir_size

    pp.pprint(directories_big_enough)
    sorted(directories_big_enough, key=lambda item: item[1], reverse=False)
    print(directories_big_enough)
if __name__ == "__main__":
    main()