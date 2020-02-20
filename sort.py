from read_file import read_file
from math import floor

def calculate_library_weight():
    meta_data = read_file("input/a_example.txt")
    weights = []
    for lib in meta_data[4].values():
        weight = 0
        NUM_DAYS = meta_data[2]
        time = (int(NUM_DAYS) - int(lib.timeUntilScan))
        sorted_books = sorted(lib.books, key=lambda book: book.score, reverse=True)
        i = 0
        while i <= (time * int(lib.booksPerDay) and i < len(sorted_books)):
            weight += sorted_books[i].score
            i += 1

        weights.append((lib.libraryID, weight))

    print(sorted(weights))


if __name__ == "__main__":
    calculate_library_weight()