def read_file(filename):
    MAX = 0
    num_indices = 0
    indices = []
    with open(filename, "r") as file:
        for line in file:
            line = line.split()
            if len(line) == 2:
                MAX         = line[0]
                num_indices = line[1]
            else:
                indices = [i for i in line]

    return MAX, num_indices, indices
