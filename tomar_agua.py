import time, pyautogui, winsound

while True:
    if time.strftime('%M') == '00' or time.strftime('%M') == '30':
        winsound.PlaySound("Teste Agua1.wav", winsound.SND_FILENAME)
        pyautogui.alert('Toma água!!')
        time.sleep(60)