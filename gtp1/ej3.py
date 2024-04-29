# Concatena. Escriba procedimientos para concatenar:

# a) dos listas L1 y L2 usando insert;
def concatena_a(L1: list, L2: list) -> list:
    for item in L2:
      L1.insert(len(L1), item)
    return L1

L1 = [1,2,3]
L2 = [4,5,6]
L3 = concatena_a(L1, L2)
print(L3)

# b) una lista LL de n sublistas usando insert
def concatena_b(LL: list) -> list:
  result = []
  for sublist in LL:
    for item in sublist:
      result.insert(len(result), item)
  return result

LL = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
result_b = concatena_b(LL)
print(result_b)

# c) una lista LL de n sublistas usando splice. Cada procedimiento debe retornar el resultado en una lista nuevao.
def concatena_c(LL: list) -> list:
  result = []
  for sublist in LL:
    result[len(result):] = sublist
  return result

LL = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
result_c = concatena_c(LL)
print(result_c)