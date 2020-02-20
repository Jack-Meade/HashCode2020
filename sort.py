from read_file import read_file

def calculate_library_weight():
    meta_data = read_file("input/a_example.txt")

    for lib in meta_data[4].values():
        print(lib)

if __name__ == "__main__":
    calculate_library_weight()