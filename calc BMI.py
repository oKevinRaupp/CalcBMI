from PySimpleGUI import PySimpleGUI as sg

sg.theme('Reddit')
layout = [
	[sg.Text("--------------------------------------------------")],
    [sg.Text("Let calculate your BMI.")],
    [sg.Text("Put your WEIGHT and HEIGHT.")],
    [sg.Text("--------------------------------------------------")],
    [sg.InputText(key="Weight")],
    [sg.InputText(key="Height")],
    [sg.Button('Calculate'), sg.Button('Cancel')],
    [sg.Text("",key="msg1")],
]

window = sg.Window("Calculate ", layout)

while True:
    event, values = window.read()
    
    if event == "Calculate":

        weight = values["Weight"]
        height = values["Height"]

        weight = float(weight)
        height = float(height)

        bmi =  height/(weight**2)

        if bmi < 16:
            window["msg1"].update(f"Severe Thinness")
        elif bmi < 17:
            window["msg1"].update(f"Moderate Thinness")
        elif bmi < 18.5:
            window["msg1"].update(f"Mild Thinness")
        elif bmi < 25:
            window["msg1"].update(f"Normal")
        elif bmi < 30:
            window["msg1"].update(f"Overweight")
        elif bmi < 35:
            window["msg1"].update(f"Obese Class I")
        elif bmi < 40:
            window["msg1"].update(f"Obese Class II") 
        else:
            window["msg1"].update(f"Obese Class III")
    
    if event == "Cancel":
        break

    if event == sg.WIN_CLOSED:
         break
window.close()