class Library(object):
    def __init__(self, libraryID, timeUntilScan, booksPerDay, books):
        self.libraryID = libraryID
        self.timeUntilScan = timeUntilScan
        self.booksPerDay = booksPerDay
        self.books = books

    def __str__(self):
        return "ID:%s Setup:%s BookRate:%s books:%s"%(self.libraryID, self.timeUntilScan, self.booksPerDay, self.books)

    def __repr__(self):
        return "ID:%s Setup:%s BookRate:%s books:%s"%(self.libraryID, self.timeUntilScan, self.booksPerDay, self.books)