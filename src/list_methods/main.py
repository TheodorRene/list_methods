from functools import reduce
from warnings import warn

class L:
    """
    Tired of not having map, filter and reduce as easily available like in
    Javascript, Java, Kotlin etc?  Fear not this is the class for you.
    """
    def __init__(self,l,mutable=False):
        """
        :init_l: inital list, useful when completing an operation and resetting the state
        :curr_l: current list
        :mutable: determines if a copy is needed, this removes the opportunity
        to reset the state of the object, but reduces memory overhead of using
        .copy()
        """
        self.init_l=l
        self.curr_l=l.copy() if not mutable else l
        self.mutable=mutable

    def __str__(self):
        """
        String representation of the list
        Note this has a effect on performance/space,since it consumes the
        iterator and instantiates the list
        """
        self.curr_l=list(self.curr_l)
        return f"L({str(self.curr_l)}"

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
        self._reset()
        return final_result

    def _reset(self):
        """
        Should be called when one is 'done' with the List. In this case its
        when reduce is called and collect
        """
        final_result = self.curr_l # Save the current list into a variable
        self.curr_l=self.init_l.copy() # set curr_l back to the inital list that the class was instantiated with
        return final_result

    def c(self):
        """
        Collect
        Collecting the final result into a list and reseting the object.
        """
        if self.mutable:
            warn("This List is mutable and therefore does not need to be instantiated into a list",SyntaxWarning)
            return self.curr_l
        final_list = self._reset()
        return list(final_list)

    def copy(self):
        """
        The class is not very good for concurrent use, but can if each thread
        is given a copy. Nice to have method
        """
        return L(list(self.curr_l))

