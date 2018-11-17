import os
import argparse


def print_file_names(path: str) -> None:
    """
    Printing file names func
    """
    dirs = []
    for name in os.listdir(path):
        new_path = f'{path}/{name}'
        if os.path.isfile(new_path):
            print(f'{path} ===> {name}')
        else:
            dirs.append(new_path)
    for d in dirs:
        print_file_names(d)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', type=str, help='Path analyzed dir')
    args = parser.parse_args()
    print_file_names(args.path)
