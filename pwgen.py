import PySimpleGUI as sg
import random
import string
import pyperclip

sg.theme('Topanga')

layout = [
    [sg.Text('Password Length: '), sg.Spin(values=[i for i in range(4, 101)], initial_value=16, size=(5, 1))],
    [sg.Text('Character Sets: ')],
    [sg.Checkbox('Uppercase', default=True), sg.Checkbox('Lowercase', default=True), sg.Checkbox('Digits', default=True), sg.Checkbox('Punctuation', default=True)],
    [sg.Button('Generate Password'), sg.Button('Copy to Clipboard')],
    [sg.Text('Generated Password:'), sg.InputText(size=(30,1), key='-PASSWORD-')],
]

window = sg.Window('Password Generator', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'Generate Password':
        length = values[0]
        upper = values[1]
        lower = values[2]
        digits = values[3]
        punctuation = values[4]

        chars = ''
        if upper:
            chars += string.ascii_uppercase
        if lower:
            chars += string.ascii_lowercase
        if digits:
            chars += string.digits
        if punctuation:
            chars += string.punctuation

        password = ''.join(random.choice(chars) for _ in range(length))

        window['-PASSWORD-'].update(password)

    if event == 'Copy to Clipboard':
        password = values['-PASSWORD-']
        pyperclip.copy(password)

window.close()
