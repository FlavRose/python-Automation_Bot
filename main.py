# Passo a passo do projeto - Automação de Tarefas com Python.

# Importando uma biblioteca que permite você controlar seu mouse, teclado e tela #
import pyautogui # Para instalar: pip install pyaltogui (utilizando o terminal) #

# pyautogui.click -> Clicar com o mouse
# pyautogui.click(clicks=2) -> Definir/dar um parâmetro de quantos clicks #
# pyautogui.write -> Escrever um texto
# pyautogui.press -> Precionar/apertar uma tecla
# pyautogui.hotkey -> Atalhos (combinações de teclas)

# Importando outra biblioteca que permite você controlar o tempo de espera para executar uma tarefa #
import time # não é preciso instalar nada para utilizar #

# Criando um tempo X de espera entre a execussão para cada comando do pyautogui #
pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa --> exemplo de sistema da empresa utlizado:
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Abrindo o Google Chrome #
pyautogui.press("win") # Para precionar a tecla Windows #
pyautogui.write("chrome")
pyautogui.press("enter")

# Criando um tempo de espera apenas para essa parte do código, assim esperando a página web carregar #
time.sleep(3)

# Entrando no sistema da empresa
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

time.sleep (3)

# Passo 2: Fazendo login
pyautogui.click(480, y=389)
pyautogui.write("email-email-email@gmail.com")
pyautogui.press("tab") # Passando para o campo de senha #
pyautogui.write("senha-senha-senha")
pyautogui.press("enter")
# OBS: As coordenadas do pointer muda dependendo da resolução de cada tela #
# OBS 2: As informações passadas nos campos acima são falsos/inexistentes, apenas para teste #

time.sleep(3)

# Importando biblioteca PANDAS para conseguir importar base de dados no código #
import pandas # Para instalar: pip install pandas numpy openpyxl (utilizando o terminal) #

# Passo 3: Importando a base de dados, por exemplo os produtos (de uma empresa) #
tabela = pandas.read_csv("produtos.csv")


for linha in tabela.index: # Para executar para todos os "produtos" #
    # Passo 4: Cadastrar os produtos
    pyautogui.click(x=520, y=271)

    # Preencher os campos #
    # !Note que estou utilizando a tabela do pandas para isso! #
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    # Enviando os cadastros #
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(20000) # Voltando ao topo da tela (scrollando) #

    # -> Importante não esquecer das indentações!! #

# Para parar a automação basta colocar seu ponteiro do mouse no extremo canto superior esquerdo
# de sua tela :D #
