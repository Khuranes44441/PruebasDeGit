

def finanzasPersonales():
    patrimonio_total = []
    

    # DINERO MODERACION

    def dineroModeracion(mes, cantidad_dias_4_horas, cantidad_dias_4_horas_y_media, cantidad_dias_8_horas):

        dias_4_horas = cantidad_dias_4_horas
        paga_dias_4_horas = 1540
        paga1 = dias_4_horas*paga_dias_4_horas

        dias_4_horas_y_media = cantidad_dias_4_horas_y_media
        paga_dias_4_horas_y_media = 1730
        paga2 = dias_4_horas_y_media*paga_dias_4_horas_y_media

        dias_8_horas = cantidad_dias_8_horas
        paga_dias_8_horas = 3270
        paga3 = dias_8_horas*paga_dias_8_horas

        paga_moderacion_mensual = paga1 + paga2 + paga3

        print(f"moderacion {mes}:  {paga_moderacion_mensual}")
        patrimonio_total.append(paga_moderacion_mensual)


    # print(f"{patrimonio_total}")

# INGRESOS EXTRA

    def ingresosExtra(mes, progresar, ife):
        progresar = progresar
        ife = ife
        ingresos_extra_total = progresar + ife
        print(f"ingresos extra {mes}: {ingresos_extra_total}")
        patrimonio_total.append(ingresos_extra_total)

# EJECUCION DEL CODIGO

    

    dineroModeracion("mayo", 6, 4, 1)
    ingresosExtra("mayo", 12840, 9000)

    dineroModeracion("junio", 10, 0, 0)
    ingresosExtra("junio", 6400, 9000)
    
    ingresosExtra("julio", 6400, 0)
        

    def calculo_patrimonio_total ():
        
        print(f"el patrimonio neto total para el mes de julio es de {sum(patrimonio_total)}")

    calculo_patrimonio_total()




finanzasPersonales()
