from pathlib import Path

class Lib:
    def __init__(self, self_id, book_ids, signup, ship_per_day):
        self.id = self_id
        self.books_num = len(book_ids)
        self.book_ids = book_ids
        self.signup = signup
        self.ship_per_day = ship_per_day


def parse_line(line : str):
    return list(map(int, line.split(' ')))


def parse_file(path : Path):
    with path.open() as file:
        books_num, libs_num, days = parse_line(file.readline())

        books_str = parse_line(file.readline())
        books = [(index, val) for index, val in enumerate(books_str)]

        libs = []
        for lib_id in range(libs_num):
            books_per_lib, signup, ship_per_day = parse_line(file.readline())
            books_in_lib = parse_line(file.readline())

            libs.append(Lib(lib_id, books_in_lib, signup, ship_per_day))

    return books, libs, days

