def promedio(notas,veces):
    prom = sum(notas) / veces
    
    return "Resultado: {0} y su promedio es: {1}".format(condicion(prom), 
    round(prom))


def condicion(promedio):
    if promedio >= 3 :
        return "APROBADO"
    elif promedio < 3 and promedio >= 2:
        return "REPROBADO CON OPORTUNIDAD DE HABILITAR"
    else:
        return "REPROBADO SIN OPORTUNIDAD DE HABILITAR"