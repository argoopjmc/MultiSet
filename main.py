from NumpyMultiset import NumpyMultiset

multiset_f = NumpyMultiset('f8')
print(multiset_f)
multiset_f.append(1,2)
print(multiset_f)
multiset_f.append(1,3)
print(multiset_f)
multiset_f.append(4,3)
print(multiset_f)
multiset_f.remove(1,4)
print(len(multiset_f))
print(multiset_f)
print(len(multiset_f))
# multiset_f.remove(1,-3)
print(multiset_f.typecheck(multiset_f))