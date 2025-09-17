# Datos iniciales - NO MODIFICAR
estudiantes = ["Rodriguez", "Gonzalez", "Martinez", "Lopez", "Silva", "Vargas", "Torres"]
notas_parcial = [14, 16, 12, 18, 15, 13, 17]
notas_final = [16, 15, 14, 17, 16, 12, 18]

print("=== REGISTRO DE NOTAS ACTUAL ===")
print("Estudiante\t\tParcial\tFinal")
for i in range(len(estudiantes)):
    print(f"{estudiantes[i]}\t\t{notas_parcial[i]}\t{notas_final[i]}")

## a) El docente decidió otorgar 1 punto adicional en el examen parcial a todos los estudiantes debido a un error en una pregunta.
notas_parcial = [nota + 1 for nota in notas_parcial]

## b) Calcula el promedio final de cada estudiante usando la fórmula: Promedio = (Parcial * 0.4) + (Final * 0.6)
promedios = []
print("\n=== PROMEDIOS FINALES ===")
print("Estudiante\t\tPromedio Final")
for i in range (len(estudiantes)):
    promedio = (notas_parcial[i] * 0.4) + (notas_final[i] * 0.6)
    promedios.append(promedio)
    print(f"{estudiantes[i]}\t\t{promedio:.2f}")


## c) Crea una lista con los apellidos de los estudiantes que obtuvieron un promedio mayor o igual a 14.
print("\n=== LISTA DE LOS ESTUDIANTES CON PROMEDIO MAYOR O IGUAL A 14 ===")
for i in range(len(estudiantes)):
    if promedios[i] >=14:
        print(f"{estudiantes[i]}: {promedios[i]:.2f} de promedio")

## d) Identifica al estudiante con el promedio más alto y al estudiante con el promedio más bajo. Muestra el apellido y el promedio de ambos.
max_promedio = max(promedios)
min_promedio = min(promedios)

estudiante_max = estudiantes[promedios.index(max_promedio)]
estudiante_min = estudiantes[promedios.index(min_promedio)]

print("\n=== ESTUDIANTES CON EL PROMEDIO MÁS ALTO Y EL MÁS BAJO ===")
print(f"Estudiante con el promedio más alto:{estudiante_max} - {max_promedio:.2f}")
print(f"Estudiantes con el promedio más bajo {estudiante_min} - {min_promedio:.2f}")
