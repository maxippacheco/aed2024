# SelectionSort. Escribir una función selectionsort(L), que ordena los elementos de L de menor a
# mayor. Para ello debe tomarse el menor elemento de L e intercambiarlo (swap) con el primer elemento
# de la lista. Luego intercambiar el menor elemento de la lista restante, con el segundo elemento, y así
# sucesivamente. Esta función debe ser in-place.

# todo revisar
def selection_sort(L):
    n = len(L)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if L[j] < L[min_index]:
                min_index = j
        if min_index != i:
            L[i], L[min_index] = L[min_index], L[i]


# Ejemplo de uso
L = [64, 25, 12, 22, 11]
selection_sort(L)
print(L)  # Output: [11, 12, 22, 25, 64]