import time, winsound
import pyautogui as usa


class Entra_Aula:
    def __init__(self) -> None:
        winsound.PlaySound("Lets do it Its go time2.wav", winsound.SND_FILENAME)
        usa.alert('A aula já já vai começar')
        usa.hotkey('winleft','d')
        usa.click(x=523, y=1053)
        time.sleep(5)
        usa.hotkey('ctrlleft','t')
        usa.write('https://ava.pucpr.br/blackboardauth/')
        usa.press('enter')
        time.sleep(4)
        usa.press('enter')
        usa.press('enter')
        time.sleep(5)
        usa.click(x=1330, y=161)
        time.sleep(1)
class FM_Pratica:
    def __init__(self) -> None:
        usa.click(x=207, y=972) #entrar em FM
        time.sleep(2)
        usa.click(x=142, y=520) #entrar webconferencia
        time.sleep(2)
        usa.click(x=483, y=415) #blackboard ultra
        time.sleep(5)
        usa.moveTo(x=1913, y=269) #mover pra barra lateral
        time.sleep(1)
        usa.mouseDown()
        usa.moveTo(x=1913, y=542) #descer a barra lateral
        time.sleep(1)
        usa.mouseUp()
        time.sleep(1)
        usa.click(x=540, y=294) #grupo aula pratica
        time.sleep(1)
        usa.click(x=520, y=370) #aula pratica
        time.sleep(1)
        usa.click(x=1601, y=136)
        usa.alert('Vc está dentro da aula')
        time.sleep(70)
class FM_terca:
    def __init__(self) -> None:
        usa.click(x=207, y=972) #entrar em FM
        time.sleep(2)
        usa.click(x=142, y=520) #entrar webconferencia
        time.sleep(2)
        usa.click(x=483, y=415) #blackboard ultra
        time.sleep(5)
        usa.moveTo(x=1913, y=269) #mover pra barra lateral
        time.sleep(1)
        usa.mouseDown()
        usa.moveTo(x=1913, y=542) #descer a barra lateral
        time.sleep(1)
        usa.mouseUp()
        time.sleep(1)
        usa.click(x=619, y=444) # prox aula teorica acho
        usa.click(x=648, y=523) # aula de hoje acho
        time.sleep(1)
        usa.click(x=1592, y=133) #entrar
        usa.alert('Vc está dentro da aula')
        time.sleep(70)
class FM_sexta:
    def __init__(self) -> None:
        usa.click(x=207, y=972) #entrar em FM
        time.sleep(2)
        usa.click(x=142, y=520) #entrar webconferencia
        time.sleep(2)
        usa.click(x=483, y=415) #blackboard ultra
        time.sleep(5)
        usa.moveTo(x=1913, y=269) #mover pra barra lateral
        time.sleep(1)
        usa.mouseDown()
        usa.moveTo(x=1913, y=542) #descer a barra lateral
        time.sleep(1)
        usa.mouseUp()
        time.sleep(1)
        usa.click(x=551, y=369) # abrir aulas teoricas terça
        time.sleep(.5)
        usa.click(x=568, y=444)
        time.sleep(1)
        usa.click(x=1569, y=147)
        usa.alert('Vc está dentro da aula')
        time.sleep(70)
class EMB:
    def __init__(self) -> None:
        usa.click(x=234, y=938) # entrar em EMB
        time.sleep(2)
        usa.click(x=128, y=543) #entrar webconferencia
        time.sleep(2)
        usa.click(x=483, y=415) #blackboard ultra
        time.sleep(5)
        usa.click(x=488, y=614)
        time.sleep(1)
        usa.click(x=1522, y=468)
        usa.alert('Vc está dentro da aula')
        time.sleep(70)
class MS:
    def __init__(self) -> None:
        usa.click(x=239, y=1007) # entrar em MS
        time.sleep(2)
        usa.click(x=142, y=520) # entrar webconferencia
        time.sleep(2)
        usa.click(x=586, y=516) # entrar aula 1
        time.sleep(2)
        usa.click(x=436, y=470) # entrar 2o link
        time.sleep(6)
        usa.click(x=964, y=778) # para participar
        usa.alert('Vc está dentro da aula')
        time.sleep(70)
class CAE_Modulada:
    def __init__(self) -> None:
        usa.click(x=331, y=865) # entrar em CAE modulada
        time.sleep(1)
        usa.click(x=151, y=539) # entrar webconferencia
        time.sleep(3)
        usa.click(x=499, y=418) # entrar blackboard
        time.sleep(4)
        usa.click(x=575, y=612) # prof claudia
        time.sleep(2)
        usa.click(x=554, y=682) # proxima aula, espero
        usa.click(x=1553, y=462) # entrar de fato
        usa.alert('Vc está dentro da aula')
        time.sleep(70)
class CR:
    def __init__(self) -> None:
        usa.click(x=245, y=902) # entrar em CR
        time.sleep(1)
        usa.click(x=142, y=520) # entrar webconferencia
        time.sleep(3)
        usa.click(x=499, y=418) # entrar blackboard
        time.sleep(4)
        usa.click(x=513, y=473) # entrar aula
        time.sleep(3)
        usa.click(x=1521, y=467) # entrar dnv
        usa.alert('Vc está dentro da aula')
        time.sleep(70)
class CAE_Completa:
    def __init__(self) -> None:
        usa.click(x=331, y=865) # entrar em CAE completa
        time.sleep(1)
        usa.click(x=151, y=539) # entrar webconferencia
        time.sleep(2)
        usa.click(x=499, y=418) # entrar blackboard
        time.sleep(4)
        usa.click(x=502, y=679) # abrir lista completa
        time.sleep(3)
        usa.click(x=541, y=762) # entrar proxima aula espero
        time.sleep(1)
        usa.click(x=1538, y=475) # entrar ultima 
        usa.alert('Vc está dentro da aula')
        time.sleep(70)
aula = {'hora1': '07','minute1': '47', 'hora2' : '09', 'minute2' : '37', 'hora3' : '11', 'minute3' : '07'}
while True:
    if time.strftime('%A') == 'Monday':
        if time.strftime('%H') == aula['hora2'] and time.strftime('%M') == aula['minute2']:
            Entra_Aula()
            aula_agora = EMB()
        if time.strftime('%H') == aula['hora3'] and time.strftime('%M') == aula['minute3']:
            Entra_Aula()
            aula_agora = FM_Pratica() # acho que terminei (?)
            break
    if time.strftime('%A') == 'Tuesday':
        if time.strftime('%H') == aula['hora1'] and time.strftime('%M') == aula['minute1']:
            Entra_Aula()
            aula_agora = FM_terca() # acho que terminei (?)
        if time.strftime('%H') == aula['hora2'] and time.strftime('%M') == aula['minute2']:
            Entra_Aula()
            aula_agora = MS()
            break
    if time.strftime('%A') == 'Wednesday':
        if time.strftime('%H') == aula['hora2'] and time.strftime('%M') == aula['minute2']:
            Entra_Aula()
            aula_agora = MS()
        if time.strftime('%H') == aula['hora3'] and time.strftime('%M') == aula['minute3']:
            Entra_Aula()
            aula_agora = CAE_Modulada() # acho que terminei (?)
            break
    if time.strftime('%A') == 'Thursday':
        if time.strftime('%H') == aula['hora2'] and time.strftime('%M') == aula['minute2']:
            Entra_Aula()
            aula_agora = CR()
        if time.strftime('%H') == aula['hora3'] and time.strftime('%M') == aula['minute3']:
            Entra_Aula()
            aula_agora = EMB()
            break
    if time.strftime('%A') == 'Friday':
        if time.strftime('%H') == aula['hora1'] and time.strftime('%M') == aula['minute1']:
            Entra_Aula()
            aula_agora = FM_sexta() # acho que terminei (?)
        if time.strftime('%H') == aula['hora2'] and time.strftime('%M') == aula['minute2']:
            Entra_Aula()
            aula_agora = MS()
        if time.strftime('%H') == aula['hora3'] and time.strftime('%M') == aula['minute3']:
            Entra_Aula()
            aula_agora = CAE_Completa() # acho que terminei (?)
            break