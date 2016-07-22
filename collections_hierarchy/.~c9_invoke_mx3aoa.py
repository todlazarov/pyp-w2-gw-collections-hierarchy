class ComparableMixin(object):
    
    def __eq__(self, other):
        if type(self) != type(other):
            return False
        
        self_ = getattr(self,self.DATA_ATTR_NAME)
        other_ = getattr(other,other.DATA_ATTR_NAME)
        
        return self_ == other_
        
    def __ne__(self, other):
        return not (self == other)


class SequenceMixin(object):
    def __iter__(self):
        self.idx = -1
        return self

    def __next__(self):
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        elements = self.get_elements()
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")
        if not hasattr(self, 'idx'):
            self.idx = 0
        else:
            self.idx += 1
        if self.idx >= len(elements):
            raise StopIteration
        
        return elements[self.idx][]
    
    next = __next__

    def __len__(self):
        count = 0
        for element in self:
            count += 1
        return count

    def __getitem__(self, key):
        return getattr(self, self.DATA_ATTR_NAME)[key]

    def __setitem__(self, key, value):
        getattr(self, self.DATA_ATTR_NAME)[key] = value


    def __delitem__(self, key):
        del getattr(self,self.DATA_ATTR_NAME)[key]

    def __contains__(self, item):
        
        for element in self:
            try:
                if element == item or item in element:
                    return True
            except:
                pass
        return False
    
    def count(self):
        return len(self)


class RepresentableMixin(object):
    def __repr__(self):
        # Will rely on the iterator or __str__
        pass

    def __str__(self):
        return str([elem for elem in self])


class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)

class OperableMixin(object):
    def __add__(self, other):
        self_ = getattr(self,self.DATA_ATTR_NAME)
        other_ = getattr(other,other.DATA_ATTR_NAME)
        return self.__class__(self_ + other_)
        
    def __iadd__(self, other):
        self
        return self

class AppendableMixin(object):
    def append(self, elem):
        getattr(self,self.DATA_ATTR_NAME).append(elem)


class HashableMixin(object):
    def keys(self):
        return [key for key, value in self]

    def values(self):
        return [value for key, value in self]

    def items(self):
        return [(key, value) for key, value in self]


class IndexableMixin(object):
    def index(self, x):
        for idx, element in enumerate(self):
            if element == x:
                return idx
        raise ValueError
            
