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
        """
        String representation of the list
        Note this has a effect on performance/space,since it consumes the
        iterator and instansiates the list
        """
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
        """
        Resets the object since reduce aggregates into a new object
        """
        final_result = reduce(f,self.curr_l)
        self.reset()
        return final_result

    def _reset(self):
        """
        Should be called when one is 'done' with the List. In this case its
        when reduce is called and collect
        """
        final_result = self.curr_l # Save the current list into a variable
        self.curr_l=self.init_l.copy() # set curr_l back to the inital list that the class was instansiated with
        return final_result

    def c(self):
        """
        Collect
        Collecting the final result into a list and reseting the object.
        """
        final_list = self._reset()
        return list(final_list)

    def copy(self):
        """
        The class is not very good for concurrent use, but can if each thread
        is given a copy. Nice to have method
        """
        return L(list(self.curr_l))

