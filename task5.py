list_ = input('Type some numbers(don\'t forget spaces):\n').split()
for i in range(len(list_)):
    list_[i] = int(list_[i])
set1 = set(range(1, len(list_) + 2))
set2 = set(list_)

x = min(set1 - set2)
print(f'Minimal positive integer that isn\'t in list: {x}')
