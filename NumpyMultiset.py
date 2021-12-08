import numpy as np

class NumpyMultiset():

    __slots__ = ['multiset']

    def __init__(self, support_type : str):

        multiset_dtype = {'names':('supports', 'multiplicities'), 'formats':(support_type, 'i4')}

        self.multiset = np.array([], dtype = multiset_dtype)

    def append(self, value, times : int = 1):

        if(times > 0):
            Multiset = self.multiset
        
            if(value in Multiset['supports']):
                Multiset['multiplicities'][np.where(Multiset['supports'] == value)] += times
            else:
                Multiset = np.append(Multiset, np.array((value,times) , dtype = Multiset.dtype))
            self.multiset = Multiset
        else:
            raise ValueError("Non positive multiplicity")

    def remove(self, value, times : int = 1):

        if(times > 0):    
            Multiset = self.multiset

            if(value in Multiset['supports']):
                pos = np.where(Multiset['supports'] == value)
                Multiset['multiplicities'][pos] -= times
                if(Multiset['multiplicities'][pos] <= 0):
                    Multiset = np.delete(Multiset, pos)
            else:
                raise ValueError("value does not exist in set")
            self.multiset = Multiset
        else:
            raise ValueError("Non positive multiplicity")

    def __len__(self):
        return np.sum(self.multiset['multiplicities'])

    def __str__(self):
        return f"{self.multiset}"

    def supportSet(self):
        return self.multiset['supports']

    def multiplicities(self):
        return self.multiset['multiplicities']

    def typecheck(self, Multiset):
        return type(Multiset.supportSet()[0])

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __le__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __add__(self, other):
        pass

    def __radd__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __rsub__(self, other):
        pass

    def __or__(self, other):
        pass

    def __ror__(self, other):
        pass

    def __and__(self, other):
        pass

    def __rand__(self, other):
        pass

    def __iadd__(self, other):
        pass

    def __isub__(self, other):
        pass

    def __iand__(self, other):
        pass

    def __ior__(self, other):
        pass
