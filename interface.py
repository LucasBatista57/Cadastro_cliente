from PySimpleGUI import PySimpleGUI as sg


layout = [

    [sg.Text('Nome: '), sg.Input(key='nome')],
    [sg.Text('CPF/CNPJ:'), sg.Input(key='doc')],
    [sg.Text('CEP: '), sg.Input(key='cep')],
    [sg.Text('Número: '), sg.Input(key='numero')],
    [sg.Button('Cadastrar')]
]

janela = sg.Window('FORMULARIO DE CADASTRO', layout)
