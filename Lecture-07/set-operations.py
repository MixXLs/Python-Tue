set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1 | set2
print("Union:", union_set)

intersection_set = set1 & set2
print("Intersection:", intersection_set)

difference_set = set1 - set2
print("Difference:", set1 - set2)

sym_diff_set = set1 ^ set2
print("Symmetric:", sym_diff_set)