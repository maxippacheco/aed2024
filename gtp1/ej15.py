# Other way to do merge sort

def merge_sort(arr):
	if len(arr) > 1:
		left_arr = arr[:len(arr)//2]
		right_arr = arr[len(arr)//2:]


		# recursion
		merge_sort(left_arr)
		merge_sort(right_arr)

		# merge
		i, j = 0, 0 # right & left idx
		k = 0 # merge arr idx
		while i < len(left_arr) and j < len(right_arr):
			if left_arr[i] < right_arr[j]:
				arr[k] = left_arr[i]
				i += 1
			else:
				arr[k] = right_arr[j]
				j += 1
			k += 1

		while i < len(left_arr):
			arr[k] = left_arr[i]
			i += 1
			k += 1
		
		while j < len(right_arr):
			arr[k] = right_arr[j]
			j += 1
			k += 1

	return arr

test = [1, 20, 3, 18, 22, 44, 32, 8]
arr_sorted = merge_sort(test)
print(arr_sorted)