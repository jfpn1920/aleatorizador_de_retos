import random
ids = []
titulos = []
categorias = []
niveles = []
descripciones = []
tiempos = []
observaciones = []
#-------------------------------------------#
#--|menu_principal_aleatorizador_de_retos|--#
#-------------------------------------------#
while True:
    print("menu principal aleatorizador de retos")
    print("1) crear reto")
    print("2) editar reto")
    print("3) eliminar reto")
    print("4) buscar reto")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #----------------#
    #--|crear_reto|--#
    #----------------#
    if opcion == "1":
        if len(ids) == 0:
            id_reto = 1
        else:
            id_reto = ids[-1] + 1
        titulo = input("título del reto: ")
        categoria = input("categoría: ")
        nivel = input("nivel de dificultad: ")
        descripcion = input("descripción del reto: ")
        tiempo = input("tiempo límite: ")
        observacion = input("observación: ")
        ids.append(id_reto)
        titulos.append(titulo)
        categorias.append(categoria)
        niveles.append(nivel)
        descripciones.append(descripcion)
        tiempos.append(tiempo)
        observaciones.append(observacion)
        print("reto registrado correctamente.")
        print("id:", id_reto)
    #-----------------#
    #--|editar_reto|--#
    #-----------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar reto")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {categorias[i]} | {niveles[i]} | {descripciones[i]} | {tiempos[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {titulos[posicion]} | {categorias[posicion]} | {niveles[posicion]} | {descripciones[posicion]} | {tiempos[posicion]} | {observaciones[posicion]}")
                titulos[posicion] = input("nuevo título: ")
                categorias[posicion] = input("nueva categoría: ")
                niveles[posicion] = input("nuevo nivel de dificultad: ")
                descripciones[posicion] = input("nueva descripción: ")
                tiempos[posicion] = input("nuevo tiempo límite: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #-------------------#
    #--|eliminar_reto|--#
    #-------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar reto")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {categorias[i]} | {niveles[i]} | {descripciones[i]} | {tiempos[i]} | {observaciones[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {titulos[posicion]} | {categorias[posicion]} | {niveles[posicion]} | {descripciones[posicion]} | {tiempos[posicion]} | {observaciones[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    titulos.pop(posicion)
                    categorias.pop(posicion)
                    niveles.pop(posicion)
                    descripciones.pop(posicion)
                    tiempos.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|buscar_reto|--#
    #-----------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar reto")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {titulos[posicion]} | {categorias[posicion]} | {niveles[posicion]} | {descripciones[posicion]} | {tiempos[posicion]} | {observaciones[posicion]}")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            faciles = 0
            medios = 0
            dificiles = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {categorias[i]} | {niveles[i]} | {descripciones[i]} | {tiempos[i]} | {observaciones[i]}")
                if niveles[i].lower() == "fácil" or niveles[i].lower() == "facil":
                    faciles += 1
                elif niveles[i].lower() == "media":
                    medios += 1
                elif niveles[i].lower() == "difícil" or niveles[i].lower() == "dificil":
                    dificiles += 1
            print("estadísticas aleatorizador de retos")
            print("cantidad de retos:", len(ids))
            print("retos fáciles:", faciles)
            print("retos medios:", medios)
            print("retos difíciles:", dificiles)
            posicion = random.randint(0, len(ids) - 1)
            print("reto seleccionado aleatoriamente")
            print(f"{ids[posicion]} | {titulos[posicion]} | {categorias[posicion]} | {niveles[posicion]} | {descripciones[posicion]} | {tiempos[posicion]} | {observaciones[posicion]}")
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el aleatorizador de retos.")
        break
    else:
        print("opción no válida.")