'''
Crea una función que reciba días, horas, minutos y segundos (como enteros)
y retorne su resultado en milisegundos.'''
 

'''
1 segundo = 1000
1 minuto = 60
1 hora = 60
1 dia = 24

'''
MILISEGUNDO = 1000
SEGUNDO = 60
MINUTO = 60
HORA = 60
DIA = 24

segundos = 60

milisegundos_por_segundos = segundos * MILISEGUNDO

# print(f'>> {segundos} segundos tienen: {milisegundos_por_segundos} milisegundos')

def conversor_tiempo(dias:int, horas:int, minutos:int, segundos:int):
    # dia = dias
    # hora = horas
    # minuto = minutos
    # segundo = segundos
    
    MILISEGUNDO = 1000
    SEGUNDO = 1
    MINUTO = 60
    HORA = 60
    DIA = 24
    
    milisegundos_por_segundos = segundos * MILISEGUNDO
    segundos_por_minutos = minutos * SEGUNDO
    total_minutos_por_hora = horas * HORA
    total_hora_por_dia = dias * DIA
    
    total_milisegundos = total_hora_por_dia * total_minutos_por_hora * segundos_por_minutos * milisegundos_por_segundos
    
    return f'''
    En {dias} días, {horas} horas, {minutos} minutos y {segundos} segundos hay: 
    {total_milisegundos}  milisegundos
'''

tiempo = conversor_tiempo(2,0,0,0)
print(tiempo)

