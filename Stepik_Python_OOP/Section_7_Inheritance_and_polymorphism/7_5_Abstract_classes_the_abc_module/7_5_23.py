from collections.abc import Sequence


class DNA(Sequence):
    def __init__(self, chain):
        self.chain = chain

    def __len__(self):
        return len(self.chain)

    def __getitem__(self, index):
        complement = {
            'A': 'T',
            'T': 'A',
            'G': 'C',
            'C': 'G'
        }

        if isinstance(index, slice):
            return self.__class__(self.chain[index])

        return self.chain[index], complement[self.chain[index]]

    def __str__(self):
        return self.chain

    def __contains__(self, item):
        return item in self.chain

    def __eq__(self, other):
        if not isinstance(other, DNA):
            return NotImplemented
        return self.chain == other.chain

    def __ne__(self, other):
        if not isinstance(other, DNA):
            return NotImplemented
        return self.chain != other.chain

    def __add__(self, other):
        if not isinstance(other, DNA):
            return NotImplemented
        return DNA(self.chain + other.chain)











dna = DNA('AGTC')

print(dna[0])
print(dna[1])
print(dna[2])
print(dna[3])
print(dna[-1])
print(dna[-2])



from collections.abc import Sequence


class DNA(Sequence):
    __BASE = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}

    def __init__(self, chain):
        self._chain = chain

    def __str__(self):
        return self._chain

    def __len__(self):
        return len(self._chain)

    def __getitem__(self, index):
        if isinstance(index, (int, slice)):
            return self._chain[index], type(self).__BASE[self._chain[index]]
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self._chain == other._chain
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, type(self)):
            return type(self)(self._chain + other._chain)
        return NotImplemented

    def __contains__(self, item):
        return item in self._chain





class DNA(str):
    def __add__(self, value):
        if isinstance(value, DNA):
            return DNA(str(self) + str(value))
        return NotImplemented

    def __getitem__(self, index):
        dct = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}
        char = str(self)[index]
        return (char, dct[char])

    def __iter__(self):
        for i in range(len(self)):
            yield self[i]