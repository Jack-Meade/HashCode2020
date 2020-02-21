from read_file import read_file
from math import floor
# global final_list
# final_list = []

files = ["b_read_on.txt","c_incunabula.txt","d_tough_choices.txt","e_so_many_books.txt"]

def calculate_library_weight_main():
    final_list = []
    meta_data = read_file("input/d_tough_choices.txt")
    scanned_books = {}
    libraries = meta_data[4]
    num_days = meta_data[2]
    while libraries and num_days:
        libraries, num_days, final_list = calculate_scores(libraries, num_days, final_list)
        
    return final_list

def calculate_scores(libraries, num_days,final_list):
    weights = []

    for lib in libraries.values():
        used_books = []
        weight = 0
        time = (int(num_days) - int(lib.timeUntilScan))
        sorted_books = sorted(lib.books, key=lambda book: book.score, reverse=True)
        i = 0
        total_books = len(sorted_books)
        total_duration = (time * int(lib.booksPerDay))
        while i <= total_duration and i < total_books:
            weight += sorted_books[i].score
            used_books.append(sorted_books[i].bookID)
            i += 1

        weights.append((lib.libraryID, weight, used_books))

    sorted_weights = sorted(weights, key=lambda x: x[1], reverse=True)

    final_list.append(sorted_weights[0])
    
    del libraries[sorted_weights[0][0]]
    return libraries, time, final_list

def write_output(final_list):
    with open("output/d_submission.txt", "w") as outfile:
        outfile.write(str(len(final_list)))
        outfile.write("\n")
        for library in final_list:
            outfile.write("{} {}".format(library[0], len(library[2])))
            outfile.write("\n")
            booklist = " ".join(map(str,library[2]))
            outfile.write(booklist)
            outfile.write("\n")

if __name__ == "__main__":
    final_list = calculate_library_weight_main()
    write_output(final_list)