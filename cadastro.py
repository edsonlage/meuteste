from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
Layout = [
    [sg. Text('usuario'),sg.Input(key='usuario',size=(20,1))],
    [sg.Text('Senha'),sg.Input(key='senha',password_char='*',size=(20,1))],
    [sg.Checkbox('salvar o login?')],
    [sg.Button('ENTRAR')]
]
# Janela 
janela = sg.Window('Edson', Layout)
# Ler eventos
while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED:
        break
    if evento == 'ENTRAR':
        if valores ['usuario'] == 'meuteste' and valores ['senha'] == '123456':
            print ('Bem vindo à minha primeira tela com Python =D')