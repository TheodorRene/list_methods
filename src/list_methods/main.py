from functools import reduce

class L:
    """
    Tired of not having map, filter and reduce as easily available like in
    Javascript, Java, Kotlin etc?  Fear not this is the class for you.
    """
    def __init__(self,l):
        self.init_l=l
        self.curr_l=l.copy()

    def __str__(self):
        self.curr_l=list(self.curr_l)
        return str(self.curr_l)

    def __repr__(self):
        return self.__str__()

    def map(self,f):
        self.curr_l=map(f,self.curr_l)
        return self

    def filter(self,f):
        self.curr_l=filter(f,self.curr_l)
        return self

    def reduce(self,f):
        final_result = reduce(f,self.curr_l)
        self.reset()
        return final_result

    def _reset(self):
        final_result = self.curr_l
        self.curr_l=self.init_l.copy()
        return final_result

    def c(self):
        final_list = self._reset()
        return list(final_list)

    def copy(self):
        return L(list(self.curr_l)

