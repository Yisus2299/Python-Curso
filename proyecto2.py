print("bienvenido al calculador de propinas")
total = float(input("cual es el total de la cuenta? "))
propina = float(input("cual es la propina? 10, 12 o 15? "))
personas = int(input("cuantas personas son? "))

propina_total = total * (propina / 100)
total_con_propina = total + propina_total
total_por_persona = total_con_propina / personas

print(f"el total de la cuenta es {total_con_propina}")
print(f"el total por persona es {total_por_persona}")