import math
def safe_apply(func, data):
    results = []
    errors = []
    
    for item in data:
        try:
            # Применение функ
            result = func(item)
            results.append(result)
        except Exception as e:
            errors.append((item, type(e).__name__))
      return results, errors

# Демонстрация
data = ['4', '16', 'text', '-25', '9.0']
sqrt_func = lambda x: math.sqrt(float(x))

results, errors = safe_apply(sqrt_func, data)

print("Успешные результаты:", results)
print("Ошибки:", errors)
