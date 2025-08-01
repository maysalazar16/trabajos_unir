# Ingreso de datos manualmente (sin bucles)
materias = []
calificaciones = []

materia1 = input("Ingrese el nombre de la primera materia: ")
nota1 = float(input("Ingrese la calificación (0 a 10): "))

materia2 = input("Ingrese el nombre de la segunda materia: ")
nota2 = float(input("Ingrese la calificación (0 a 10): "))

materia3 = input("Ingrese el nombre de la tercera materia: ")
nota3 = float(input("Ingrese la calificación (0 a 10): "))

# Guardar en listas
materias = [materia1, materia2, materia3]
calificaciones = [nota1, nota2, nota3]

# Calcular promedio
promedio = (nota1 + nota2 + nota3) / 3

# Determinar materias aprobadas y reprobadas
aprobadas = []
reprobadas = []

if nota1 >= 5.0:
    aprobadas.append(materia1)
else:
    reprobadas.append(materia1)

if nota2 >= 5.0:
    aprobadas.append(materia2)
else:
    reprobadas.append(materia2)

if nota3 >= 5.0:
    aprobadas.append(materia3)
else:
    reprobadas.append(materia3)

# Calificación más alta y más baja
mayor = max(calificaciones)
menor = min(calificaciones)

indice_mayor = calificaciones.index(mayor)
indice_menor = calificaciones.index(menor)

# Mostrar resultados
print("\n===== RESUMEN FINAL =====")
print("Materias ingresadas:", materias)
print("Calificaciones:", calificaciones)
print("Promedio general:", round(promedio, 2))

print("Materias aprobadas:", aprobadas)
print("Materias reprobadas:", reprobadas)

print("Materia con mayor nota:", materias[indice_mayor], "-", mayor)
print("Materia con menor nota:", materias[indice_menor], "-", menor)
