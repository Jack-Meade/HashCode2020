class Book(object):
    def __init__(self, bookID, score):
        self.bookID = bookID
        self.score = score


    def get_score(self):
        return int(self.score)
        
    def __str__(self):
        return "BookID:%s BookScore:%s"%(self.bookID, self.score)

    def __repr__(self):
        return "BookID:%s BookScore:%s"%(self.bookID, self.score)