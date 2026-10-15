# Programa que me indica un presupuesto de compra

producto = input("Nombre del producto: ")

precio = float(input("Precio por unidad: "))

unidades = int(input("¿Cuántas unidades quiere comprar?: "))

presupuesto = float(input("¿Cuál es el presupuesto?: "))

total = precio * unidades


print(f"Total: {total:,.0f}")

if total <= presupuesto:
    print(f"Te alcanza para comprar {producto}")
else:
    print(f"No te alcanza, te faltan {total - presupuesto:,.0f} pesos")