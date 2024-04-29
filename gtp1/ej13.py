# Merge. Escribir una función merge(L1, L2, L) la cual recibe dos listas ordenadas (que pueden ser de
# distinto tamaño) de forma ascendente L1 y L2 y retorna una lista L, pasada como parámetro, con los
# elementos de ambas ordenados también en forma ascendente. Por ejemplo si L1=[1, 3, 6, 11] y L2=[2,
# 4, 6, 10], la lista L debe quedar como L=[1, 2, 3, 4, 6, 6, 10, 11].

def merge(list1, list2, merged_list):
	# Check if the lists have the same number of elements
	if len(list1) == len(list2):
    # Iterate through both lists simultaneously
		for i in range(len(list1)):
      # Compare corresponding elements and append to merged_list in ascending order
			if list1[i] < list2[i]:
				merged_list = merged_list + [list1[i]] + [list2[i]]
			else:
				merged_list = merged_list + [list2[i]] + [list1[i]]
  # Handle lists with unequal lengths (assuming list1 is longer)	
	elif len(list1) > len(list2):
    # Iterate through list2 and merge elements
		for i in range(len(list2)):
			if list1[i] < list2[i]:
				merged_list = merged_list + [list1[i]] + [list2[i]]
			else:
				merged_list = merged_list + [list2[i]] + [list1[i]]
    # Append remaining elements from the longer list (list1)		
		merged_list += list2[len(list1):]
	return merged_list


L = []
L1=[1, 3, 6, 11]
L2=[2, 4, 6, 10]

print(merge(L1, L2, L))