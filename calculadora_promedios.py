def ingresar_calificaciones():
    """
    Permite al usuario ingresar materias y calificaciones.
    Retorna dos listas: nombres de materias y calificaciones correspondientes.
    """
    materias = []
    calificaciones = []
    
    print("=== INGRESO DE CALIFICACIONES ===")
    print("Ingresa las materias y sus calificaciones (0-10)")
    print("-" * 40)
    
    while True:
        # Solicitar nombre de la materia
        materia = input("\nIngresa el nombre de la materia: ").strip()
        
        if not materia:
            print("Error: El nombre de la materia no puede estar vacío.")
            continue
        
        # Solicitar y validar calificación
        while True:
            try:
                calificacion = float(input(f"Ingresa la calificación para {materia} (0-10): "))
                
                if 0 <= calificacion <= 10:
                    break
                else:
                    print("Error: La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Error: Por favor ingresa un número válido.")
        
        # Almacenar datos
        materias.append(materia)
        calificaciones.append(calificacion)
        
        print(f"✓ {materia}: {calificacion}")
        
        # Preguntar si desea continuar
        while True:
            continuar = input("\n¿Deseas ingresar otra materia? (s/n): ").lower().strip()
            if continuar in ['s', 'si', 'sí', 'y', 'yes']:
                break
            elif continuar in ['n', 'no']:
                return materias, calificaciones
            else:
                print("Por favor responde 's' para sí o 'n' para no.")


def calcular_promedio(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones.
    
    Args:
        calificaciones (list): Lista de calificaciones numéricas
    
    Returns:
        float: Promedio de las calificaciones
    """
    if not calificaciones:
        return 0
    
    return sum(calificaciones) / len(calificaciones)


def determinar_estado(calificaciones, umbral=5.0):
    """
    Determina qué materias están aprobadas y cuáles reprobadas.
    
    Args:
        calificaciones (list): Lista de calificaciones
        umbral (float): Calificación mínima para aprobar (por defecto 5.0)
    
    Returns:
        tuple: (índices_aprobadas, índices_reprobadas)
    """
    aprobadas = []
    reprobadas = []
    
    for i, calificacion in enumerate(calificaciones):
        if calificacion >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)
    
    return aprobadas, reprobadas


def encontrar_extremos(calificaciones):
    """
    Encuentra los índices de la calificación más alta y más baja.
    
    Args:
        calificaciones (list): Lista de calificaciones
    
    Returns:
        tuple: (índice_máximo, índice_mínimo)
    """
    if not calificaciones:
        return None, None
    
    indice_max = 0
    indice_min = 0
    
    for i in range(1, len(calificaciones)):
        if calificaciones[i] > calificaciones[indice_max]:
            indice_max = i
        if calificaciones[i] < calificaciones[indice_min]:
            indice_min = i
    
    return indice_max, indice_min


def mostrar_resumen(materias, calificaciones):
    """
    Muestra un resumen completo de las calificaciones y estadísticas.
    """
    if not materias or not calificaciones:
        print("\n No se ingresaron materias para procesar.")
        return
    
    print("\n" + "=" * 50)
    print("           RESUMEN DE CALIFICACIONES")
    print("=" * 50)
    
    # Mostrar todas las materias con sus calificaciones
    print("\n MATERIAS Y CALIFICACIONES:")
    print("-" * 30)
    for i, (materia, calificacion) in enumerate(zip(materias, calificaciones), 1):
        print(f"{i:2d}. {materia:<20} {calificacion:>5.1f}")
    
    # Calcular promedio
    promedio = calcular_promedio(calificaciones)
    print(f"\n PROMEDIO GENERAL: {promedio:.2f}")
    
    # Determinar estado de materias
    aprobadas, reprobadas = determinar_estado(calificaciones)
    
    print(f"\n MATERIAS APROBADAS ({len(aprobadas)}):")
    if aprobadas:
        for i in aprobadas:
            print(f"   • {materias[i]}: {calificaciones[i]:.1f}")
    else:
        print("   Ninguna materia aprobada")
    
    print(f"\n MATERIAS REPROBADAS ({len(reprobadas)}):")
    if reprobadas:
        for i in reprobadas:
            print(f"   • {materias[i]}: {calificaciones[i]:.1f}")
    else:
        print("   Ninguna materia reprobada")
    
    # Encontrar extremos
    indice_max, indice_min = encontrar_extremos(calificaciones)
    
    if indice_max is not None and indice_min is not None:
        print(f"\n MEJOR CALIFICACIÓN:")
        print(f"   {materias[indice_max]}: {calificaciones[indice_max]:.1f}")
        
        print(f"\n PEOR CALIFICACIÓN:")
        print(f"   {materias[indice_min]}: {calificaciones[indice_min]:.1f}")
    
    # Estadísticas adicionales
    print(f"\n ESTADÍSTICAS:")
    print(f"   Total de materias: {len(materias)}")
    print(f"   Porcentaje de aprobación: {(len(aprobadas)/len(materias)*100):.1f}%")
    
    # Determinar estado general
    if promedio >= 5.0:
        estado = "APROBADO "
    else:
        estado = "REPROBADO "
    
    print(f"\n ESTADO GENERAL: {estado}")


def main():
    """
    Función principal del programa.
    """
    print(" CALCULADORA DE PROMEDIOS ACADÉMICOS")
    print("=" * 40)
    
    try:
        # Ingresar calificaciones
        materias, calificaciones = ingresar_calificaciones()
        
        # Mostrar resumen completo
        mostrar_resumen(materias, calificaciones)
        
    except KeyboardInterrupt:
        print("\n\n  Programa interrumpido por el usuario.")
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
    
    # Mensaje de despedida
    print("\n" + "=" * 50)
    print("¡Gracias por usar la Calculadora de Promedios!")
    print("¡Que tengas un excelente día! 🌟")
    print("=" * 50)


if __name__ == "__main__":
    main()