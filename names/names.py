import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('./names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('./names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
duplicates = []
name_1_set = set(names_1)
name_2_set = set(names_2)
for name in name_1_set.intersection(name_2_set):
    duplicates.append(name)

end_time = time.time()
duration = end_time - start_time
time_provided = 15.133995771408081
multiple = round(time_provided/duration,1)
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {duration} seconds")
print(f'Optimized solution runs {multiple} times faster than the provided solution ')
print()