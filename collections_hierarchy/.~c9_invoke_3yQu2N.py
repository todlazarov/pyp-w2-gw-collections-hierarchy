class ComparableMixin(object):
    
    def __eq__(self, other):
        if type(self) == type(other):
            return self.data == other.data
        else:
            return False
            
    def __ne__(self, other):
        return not (self == other)


class SequenceMixin(object):
    def __iter__(self):
        self.idx = 0
        return self

    def __next__(self):
        """This method will rely on the get_elements() method of the
        concrete class.
        """
        
        elements = self.get_elements()
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")
        # Keep writing your code here
        if self.idx >= len(elements):
            raise StopIteration
        else:
            self.idx += 1

        return elements[self.idx - 1]
    
    next = __next__

    def __len__(self):
        # Will rely on the iterator, can't do len(self.data)
        count = 0
        for element in self:
            count += 1
        return count

    def __getitem__(self, key):
        self[key] = value # a = list[1]

    def __setitem__(self, key, value):
        getattr(self, self.DATA_ATTR_NAME)[key] = value
        
    def __delitem__(self, key):
        pass

    def __contains__(self, item):
        for element in self:
            print(element)
            if element == item:
                return True
        return False


class RepresentableMixin(object):
    def __repr__(self):
        # Will rely on the iterator or __str__
        pass

    def __str__(self):
        # Will rely on the iterator
        pass


class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)

class OperableMixin(object):
    def __add__(self, other):
        pass

    def __iadd__(self, other):
        pass


class AppendableMixin(object):
    def append(self, elem):
        # Relies on DATA_ATTR_NAME = 'data'
        pass


class HashableMixin(object):
    def keys(self):
        pass

    def values(self):
        pass

    def items(self):
        pass


class IndexableMixin(object):
    def index(self, x):
        pass
