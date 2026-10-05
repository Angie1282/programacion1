# Calculo de promedio de tres notas

print("\nPromedio Notas\n")

grades = []
for n in range(1, 4):
    grade = float(input(f"Ingrese la nota {n} : "))
    grades.append(grade)

average = round(sum(grades) / len(grades), 1)

print("\nEl promedio es: ", average)

if average >= 3: 
    print("Aprobaste")
else:
    print("Reprobaste, a seguir estudiando")