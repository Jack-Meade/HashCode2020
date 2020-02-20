from Book import Book
from Library import Library

def read_file(filename):
    NUM_BOOKS       = 0
    NUM_LIBRARIES   = 0
    NUM_DAYS        = 0
    BOOK_SCORES     = []
    libraries       = {}

    with open(filename, "r") as file:
        lines           = file.readlines()
        line            = lines[0].split()
        NUM_BOOKS       = line[0]
        NUM_LIBRARIES   = line[1]
        NUM_DAYS        = line[2]
        BOOK_SCORES     = lines[1].split()

        lib_num = 0
        for i in range(2, len(lines), 2):
            line                = lines[i].split()
            numbooks            = line[0]
            stime               = line[1]
            bpd                 = line[2]
            books               = lines[i+1].split()
            
            libraries[lib_num]  = Library(lib_num, stime, bpd, books)

    return NUM_BOOKS, NUM_LIBRARIES, NUM_DAYS, BOOK_SCORES, libraries

if __name__ == '__main__':
    NUM_BOOKS, NUM_LIBRARIES, NUM_DAYS, BOOK_SCORES, libraries = read_file("input/a_example.txt")
    print("NUM_BOOKS:    ", NUM_BOOKS)
    print("NUM_LIBRARIES:", NUM_LIBRARIES)
    print("NUM_DAYS:     ", NUM_DAYS)
    print("BOOK_SCORES:  ", BOOK_SCORES)
    print("libraries:    ", libraries)
