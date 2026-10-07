
# 1. LISTA DE CANCIONES
# Cada canción es una tupla con:
# titulo, artista, genero y ambiente
# ============================================
canciones = [
    ("De Música Ligera", "Soda Stereo", "Rock alternativo", "Energico"),
    ("Persiana Americana", "Soda Stereo", "Rock alternativo", "Energico"),
    ("Cuando Pase el Temblor", "Soda Stereo", "Rock latino", "Energico"),
    ("Entre Dos Tierras", "Héroes del Silencio", "Rock alternativo", "Intenso"),
    ("Maldito Duende", "Héroes del Silencio", "Rock alternativo", "Intenso"),
    ("La Chispa Adecuada", "Héroes del Silencio", "Rock alternativo", "Tranquilo"),
    ("Lobo-Hombre en París", "La Unión", "Rock clasico", "Energico"),
    ("Afuera", "Caifanes", "Rock alternativo", "Intenso"),
    ("La Celula Que Explota", "Caifanes", "Rock latino", "Tranquilo"),
    ("Rayando el Sol", "Maná", "Rock latino", "Tranquilo"),
    ("En el Muelle de San Blas", "Maná", "Rock latino", "Tranquilo"),
    ("Lamento Boliviano", "Enanitos Verdes", "Rock latino", "Energico"),
    ("Mi Primer Día Sin Ti", "Enanitos Verdes", "Rock latino", "Tranquilo"),
    ("Trátame Suavemente", "Soda Stereo", "Rock alternativo", "Tranquilo"),
    ("Mil Horas", "Los Abuelos de la Nada", "Rock clasico", "Energico"),
    ("El Matador", "Los Fabulosos Cadillacs", "Rock latino", "Energico"),
    ("Siguiendo la Luna", "Los Fabulosos Cadillacs", "Rock latino", "Tranquilo"),
    ("Flaca", "Andrés Calamaro", "Rock clasico", "Tranquilo"),
    ("Sin Documentos", "Los Rodríguez", "Rock clasico", "Energico"),
    ("A Dios le Pido", "Juanes", "Rock latino", "Energico")
]


# ============================================
# 2. CREAR UN SET DE GÉNEROS
# El set evita que los géneros se repitan
# ============================================

generos = set()

# Recorrer todas las canciones
for cancion in canciones:

    # Agregar el género al set
    generos.add(cancion[2])


# ============================================
# 3. PRESENTACIÓN DEL PROGRAMA
# ============================================

print("============================================")
print("     DESCUBRE TU CANCION FAVORITA")
print("============================================")

# Mostrar la cantidad de canciones que tenemos en las duplas
print("\nTenemos", len(canciones), "canciones de rock en español.")

# Mostrar los géneros que tenemos en las duplas
print("\nLos estilos disponibles son:")

for genero in generos:
    print("-", genero)


# ============================================
# 4. PREGUNTAR EL GÉNERO FAVORITO
# ============================================

print("--------------------------------------------")
print("¿Que tipo de rock prefieres?")
print("--------------------------------------------")

print("1. Rock alternativo")
print("2. Rock clasico")
print("3. Rock latino")
print("4. Cualquier estilo")


# ============================================
# 5. VALIDAR LA OPCIÓN DEL GÉNERO
# No permite números diferentes de 1 a 4
# ============================================

while True:

    opcion = input("Selecciona una opcion (1-4): ")

    # Verificar que la opción sea 1, 2, 3 o 4
    if opcion in ["1", "2", "3", "4"]:
        break

    # Mensaje si el usuario escribe otra opción
    print("Opcion no valida. Por favor, elige un numero del 1 al 4.")


# ============================================
# 6. DETERMINAR EL GÉNERO ELEGIDO
# ============================================

if opcion == "1":
    genero_elegido = "Rock alternativo"

elif opcion == "2":
    genero_elegido = "Rock clasico"

elif opcion == "3":
    genero_elegido = "Rock latino"

else:
    genero_elegido = "Todos"


# ============================================
# 7. CREAR LISTA DE RECOMENDACIONES
# ============================================

recomendaciones = []


# ============================================
# 8. FILTRAR LAS CANCIONES POR GÉNERO
# ============================================

for cancion in canciones:

    # Si eligió cualquier género
    if genero_elegido == "Todos":

        # Agregar todas las canciones
        recomendaciones.append(cancion)

    # Si eligió un género específico
    elif cancion[2] == genero_elegido:

        # Agregar solamente las canciones
        # que coincidan con el género
        recomendaciones.append(cancion)


# ============================================
# 9. PREGUNTAR EL AMBIENTE FAVORITO
# ============================================

print("\n--------------------------------------------")
print("¿Que tipo de canciones prefieres?")
print("--------------------------------------------")

print("1. Energicas")
print("2. Tranquilas")
print("3. Intensas")
print("4. Cualquiera")


# 10. VALIDAR LA OPCIÓN DEL AMBIENTE
# No permite números diferentes de 1 a 4

while True:

    ambiente = input("Selecciona una opcion (1-4): ")

    # Verificar que la opción sea válida
    if ambiente in ["1", "2", "3", "4"]:
        break

    # Mensaje si escribe una opción incorrecta
    print("Opcion no valida. Por favor, elige un numero del 1 al 4.")


# ============================================
# 11. DETERMINAR EL AMBIENTE ELEGIDO
# ============================================

if ambiente == "1":
    ambiente_elegido = "Energico"

elif ambiente == "2":
    ambiente_elegido = "Tranquilo"

elif ambiente == "3":
    ambiente_elegido = "Intenso"

else:
    ambiente_elegido = "Todos"


# ============================================
# 12. CREAR SEGUNDA LISTA
# Aquí guardaremos las recomendaciones finales
# ============================================

nuevas_recomendaciones = []


# ============================================
# 13. FILTRAR LAS CANCIONES POR AMBIENTE
# ============================================

for cancion in recomendaciones:

    # Si eligió cualquier ambiente
    if ambiente_elegido == "Todos":

        # Agregar la canción
        nuevas_recomendaciones.append(cancion)

    # Si eligió un ambiente específico
    elif cancion[3] == ambiente_elegido:

        # Agregar la canción que coincida
        nuevas_recomendaciones.append(cancion)


# ============================================
# 14. VERIFICAR SI HAY RECOMENDACIONES
# ============================================

if len(nuevas_recomendaciones) > 0:

    # Mostrar las canciones encontradas
    print("============================================")
    print("           TUS RECOMENDACIONES")
    print("============================================")

    # Recorrer las recomendaciones
    for i, cancion in enumerate(nuevas_recomendaciones):

        # Mostrar número, canción y artista
        print(
            i + 1,
            ".",
            cancion[0],
            "-",
            cancion[1]
        )

else:

    # Mostrar mensaje si no hubo coincidencias
    print("\nNo encontramos coincidencias exactas.")

    # Tomar las primeras cinco canciones
    # como recomendaciones generales
    nuevas_recomendaciones = canciones[:5]


# ============================================
# 15. MOSTRAR LAS CANCIONES PARA ELEGIR
# ============================================

print("\n--------------------------------------------")
print("De estas canciones, ¿cual quieres elegir?")
print("--------------------------------------------")


# Recorrer nuevamente las recomendaciones
for i, cancion in enumerate(nuevas_recomendaciones):

    # Mostrar las canciones numeradas
    print(
        i + 1,
        ".",
        cancion[0],
        "-",
        cancion[1]
    )


# ============================================
# 16. VALIDAR LA CANCIÓN FAVORITA
# No permite elegir una posición que no existe
# ============================================

while True:
##“El while True permite repetir la pregunta hasta obtener una respuesta válida. El try intenta convertir la respuesta en un número y el except
   # ValueError evita que el programa se cierre si el usuario escribe letras.”
    try:

        # Pedir al usuario el número
        eleccion = int(
            input(
                "\nEscribe el numero de tu favorita: "
            )
        )

        # Verificar que el número esté dentro
        # de las recomendaciones disponibles
        if 1 <= eleccion <= len(nuevas_recomendaciones):
            break
### el break lo que hace es que se salga del ciclo
        # Si el número no existe
        print(
            "Opcion no valida. Elige un numero entre 1 y",
            len(nuevas_recomendaciones)
        )

    except ValueError:

        # Si escribe letras en lugar de números
        print("Entrada no valida. Debes escribir un numero.")


# ============================================
# 17. GUARDAR LA CANCIÓN FAVORITA
# ============================================

# Python comienza las posiciones desde 0,
# por eso restamos 1 a la elección
cancion_favorita = nuevas_recomendaciones[eleccion - 1]


# ============================================
# 18. MOSTRAR EL RESULTADO FINAL
# ============================================

print("\n============================================")
print("          TU CANCION FAVORITA")
print("============================================")


# Mostrar el título de la canción
print("Cancion :", cancion_favorita[0])

# Mostrar el artista
print("Artista :", cancion_favorita[1])

# Mostrar el género
print("Genero  :", cancion_favorita[2])

# Mostrar el ambiente
print("Estilo  :", cancion_favorita[3])

# Mensaje final
print("\n¡Excelente eleccion!")


# ============================================
# 19. CREAR SET DE ARTISTAS
# ============================================

artistas = set()


# ============================================
# 20. AGREGAR ARTISTAS AL SET
# El set elimina los artistas repetidos
# ============================================

for cancion in canciones:

    # cancion[1] corresponde al artista
    artistas.add(cancion[1])


# ============================================
# 21. MOSTRAR CANTIDAD DE ARTISTAS
# ============================================

print("\n--------------------------------------------")
print("En nuestra biblioteca tenemos")
print(len(artistas), "artistas diferentes.")
print("--------------------------------------------")
