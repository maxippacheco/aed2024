import json
import random

class Eval:
    @staticmethod
    def generate_test_cases(func, num_cases=50):
        test_cases = []
        for _ in range(num_cases):
            L = [random.randint(-100, 100) for _ in range(random.randint(1, 20))]
            test_cases.append({"input": L, "output": func(L)})
        with open("test_cases.json", "w") as f:
            json.dump(test_cases, f, indent=4)
        print(f"{num_cases} casos de prueba generados y almacenados en 'test_cases.json'.")

    @staticmethod
    def validate_test_cases(func):
        passed = 0
        failed = 0
        with open("test_cases.json", "r") as f:
            test_cases = json.load(f)
        for idx, test_case in enumerate(test_cases, start=1):
            L = test_case["input"]
            expected_output = test_case["output"]
            output = func(L)
            if output == expected_output:
                passed += 1
                print(f"Test {idx}: PASSED")
            else:
                failed += 1
                print(f"Test {idx}: FAILED - Entrada: {L}, Salida esperada: {expected_output}, Salida obtenida: {output}")
        print(f"\nTotal de pruebas: {len(test_cases)}")
        print(f"Pruebas pasadas: {passed}")
        print(f"Pruebas falladas: {failed}")