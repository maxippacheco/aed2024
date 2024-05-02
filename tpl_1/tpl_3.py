# Escribir una función void extract_prime(list<int> &L, queue<int> &Q); que, dada una lista de enteros L, extrae todos los numeros primos,
# en una cola Q, de mayor a menor. De modo tal que al invocar front por primera vez, se obtenga el mayor.

from queue_implementation import Queue

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def extract_prime(L: list):
  queue = Queue()
  prime_numbers = []

	# push the prime numbers in an aux array
  for num in L:
    if is_prime(num):
      prime_numbers.append(num)
  final_list = sorted(prime_numbers, reverse=True)
  
  for num in final_list:
      queue.push(num)
  return queue 


L = [12, 7, 5, 23, 15, 13, 20]
new_queue = extract_prime(L)

# Example usage
# while not new_queue.is_empty():
print(new_queue.top())  # Prints the largest prime number first
