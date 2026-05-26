import time

def speed_calc_decorator(function):  # El decorador recibe la función a "decorar"
    def wrapper():  # Esta función envuelve a la original
        start_time = time.time()      # 1. Hora antes de ejecutar
        function()                     # 2. Ejecutar la función original
        end_time = time.time()        # 3. Hora después de ejecutar
        duration = end_time - start_time  # 4. Calcular diferencia
        print(f"{function.__name__} ejecuta velocidad: {duration}s")
    return wrapper  # Devolver la función wrapper

@speed_calc_decorator  # Esto es lo mismo que: fast_function = speed_calc_decorator(fast_function)
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

# Para probar:
fast_function()
slow_function()
