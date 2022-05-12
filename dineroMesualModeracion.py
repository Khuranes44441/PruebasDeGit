def dineroModeracion(mes):
    dias_4_horas =  6
    paga_dias_4_horas = 1540
    paga1 = dias_4_horas*paga_dias_4_horas

    dias_4_horas_y_media = 4
    paga_dias_4_horas_y_media = 1730
    paga2 = dias_4_horas_y_media*paga_dias_4_horas_y_media

    dias_8_horas = 1
    paga_dias_8_horas = 3270
    paga3 = dias_8_horas*paga_dias_8_horas

    print(f"el mes de {mes} gano un total de {paga1+paga2+paga3}")

    

dineroModeracion("junio")


