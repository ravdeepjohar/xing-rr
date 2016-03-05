from collections import namedtuple

class Impression(namedtuple("Impression", "user_id year week items")):
    __slots__ = ()

    def __repr__(self):
        return "Impression(user:{},year:{},week:{},items:{})".format(self.user_id, self.year, self.week, len(self.items))
        
    def __str__(self):
        return "Impression(user:{},year:{},week:{},items:{})".format(self.user_id, self.year, self.week, len(self.items))
        