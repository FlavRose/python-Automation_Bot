# Código para auxiliar com o código main #

import pyautogui
import time

# Criando um tempo para modo de espera antes de tirar o print do meu ponteiro do mouse #
time.sleep(5)

# Tirando print do ponteiro do mouse para mostrar as coordenadas dele em um momento específico #
print(pyautogui.position())


# Assim fica mais fácil de passar para o nosso código onde que a automação de trabalho deve clicar :) #