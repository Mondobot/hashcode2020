from pathlib import Path
from lib import Lib

"""
class Lib:
    def __init__(self, self_id, book_ids, signup, ship_per_day):
        self.id = self_id
        self.book_ids = book_ids
        self.signup = signup
        self.ship_per_day = ship_per_day
"""

def parse_line(line : str):
    return list(map(int, line.split(' ')))


def parse_file(path : Path):
    with path.open() as file:
        books_num, libs_num, days = parse_line(file.readline())

        books_str = parse_line(file.readline())
        books = {index: val for index, val in enumerate(books_str)}

        libs = []
        for lib_id in range(libs_num):
            books_per_lib, signup, ship_per_day = parse_line(file.readline())
            books_in_lib = parse_line(file.readline())

            libs.append(Lib(lib_id, books_in_lib, signup, ship_per_day))

    return books, libs, days

def save_solution(libs, input_name):
    filename = Path('solution_' + input_name.split('/')[-1])
    with filename.open('w') as file:
        file.write(str(len(libs)))

        for lib in libs:
            file.write('{} {}'.format(lib.id, len(lib.book_ids)))
            file.write(' '.join(map(str, lib.book_ids)))
