import numpy as np

class MultiSet():

    __slots__ = ['multiset']

    def __init__(self, support_type : str):

        multiset_dtype = {'names':('supports', 'multiplicities'), 'formats':(support_type, 'i4')}

        self.multiset = np.array([], dtype = multiset_dtype)

    def appendMultiset(self, value, times : int = 1):

        if(times > 0):
            Multiset = self.multiset
        
            if(value in Multiset['supports']):
                Multiset['multiplicities'][np.where(Multiset['supports'] == value)] += times
            else:
                Multiset = np.append(Multiset, np.array((value,times) , dtype = Multiset.dtype))
            self.multiset = Multiset
        else:
            raise ValueError("Non positive multiplicity")

    def removeMultiset(self, value, times : int = 1):

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

    def __str__(self):
        return f"{self.multiset}"

multiset_f = MultiSet('f8')
print(multiset_f)
multiset_f.appendMultiset(1,2)
print(multiset_f)
multiset_f.appendMultiset(1,3)
print(multiset_f)
multiset_f.appendMultiset(4,3)
print(multiset_f)
multiset_f.removeMultiset(1,4)
print(multiset_f)
multiset_f.removeMultiset(1,-3)
print(multiset_f)