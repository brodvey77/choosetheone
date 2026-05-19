
class ReversedSequence:
    def __init__(self, sequence):
        self.sequence = sequence

    def __getitem__(self, index):
        return self.sequence[::-1][int(index)]

    def __len__(self):
        return len(self.sequence)




numbers = [1, 2, 3, 4, 5]
reversed_numbers = ReversedSequence(numbers)
print(len(reversed_numbers))

numbers.append(6)
numbers.append(7)
print(len(reversed_numbers))

#
#
# class ReversedSequence:
#     def __init__(self, sequence):
#         self.sequence = sequence
#
#     def __len__(self):
#         return len(self.sequence)
#
#     def __getitem__(self, key):
#         return self.sequence[len(self) - key - 1]
#
#     def __iter__(self):
#         yield from reversed(self.sequence)
#
#
# class ReversedSequence:
#     def __init__(self, sequence):
#         self.sequence = sequence
#
#     def __len__(self):
#         return len(self.sequence)
#
#     def __getitem__(self, key):
#         return self.sequence[~key]