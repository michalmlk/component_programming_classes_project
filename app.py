import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
from utils import BMR, BMI, export_to_txt

class NegativeValueException(Exception):
    pass

# root window
root = tk.Tk()
root.title('Calories calc')
root.geometry('540x360')
root.configure(padx=20, pady=10)
root.resizable(False, False)

frame = ttk.Frame(root)
frame.grid(column=0, row=0, sticky="nsew")

options = {'padx': 5, 'pady': 5}

# labels and inputs
sex_label = ttk.Label(frame, text='Płeć')
sex_label.grid(column=0, row=0, sticky='ew')

sex_input = tk.StringVar()
sex_input = ttk.OptionMenu(frame, sex_input, "female", "male")
sex_input.grid(column=0, row=1, **options)

weight_label = ttk.Label(frame, text='Waga (kg)')
weight_label.grid(column=0, row=2, sticky='W', **options)

weight_input = tk.DoubleVar()
weight_input = ttk.Entry(frame, textvariable=weight_input)
weight_input.grid(column=0, row=3, **options)

age_label = ttk.Label(frame, text='Wiek (lata)')
age_label.grid(column=0, row=4, sticky='W', **options)

age_input = tk.IntVar()
age_input = ttk.Entry(frame, textvariable=age_input)
age_input.grid(column=0, row=5, **options)

height_label = ttk.Label(frame, text='Wzrost (cm)')
height_label.grid(column=0, row=6, sticky='W', **options)

height_input = tk.IntVar()
height_input = ttk.Entry(frame, textvariable=height_input)
height_input.grid(column=0, row=7, **options)

def action_button_clicked():
    try:
        weight = float(weight_input.get())
        height = int(height_input.get())
        age = int(age_input.get())
        bmr = round(BMR(sex_input, weight, age, height), 2)
        bmi = round(BMI(weight, height), 2)

        if weight <= 0 or height <= 0 or age <= 0:
            raise NegativeValueException

    except ValueError:
        showerror(title='Error', message="Błędne dane")
    except NegativeValueException:
        showerror(title='Error', message="Wielkości fizyczne nie mogą być ujemne!")
    else:
        info_header.config(text="Oto Twoje dane:")

        bmr_val = f'BMR: {bmr} kcal'
        bmr_label.config(text=bmr_val)

        weight_info_label.config(text=f'Waga: {weight_input.get()} kg')
        age_info_label.config(text=f'Wiek: {age_input.get()} lat')
        height_info_label.config(text=f'Wzrost: {height_input.get()} cm')

        bmi_val = f'BMI: {bmi}'
        bmi_label.config(text=bmi_val)

        weight_input.delete(0, len(weight_input.get()))
        height_input.delete(0, len(height_input.get()))
        age_input.delete(0, len(age_input.get()))


action_button = ttk.Button(frame, text='Policz')
action_button.grid(column=0, row=9, sticky='ew', **options)
action_button.configure(command=action_button_clicked)

export_button = ttk.Button(frame, text='Export do .txt')
export_button.grid(column=1, row=9, sticky='ew', **options)
export_button.configure(command=lambda: export_to_txt(collected_data))


info_header = ttk.Label(frame)
info_header.grid(row=0, column=1, **options)

weight_info_label = ttk.Label(frame)
weight_info_label.grid(row=1, column=1, **options)
height_info_label = ttk.Label(frame)
height_info_label.grid(row=2, column=1, **options)
age_info_label = ttk.Label(frame)
age_info_label.grid(row=3, column=1, **options)

bmr_label = ttk.Label(frame)
bmr_label.grid(row=4, column=1, **options)
bmi_label = ttk.Label(frame)
bmi_label.grid(row=5, column=1, **options)

collected_data = [weight_info_label, age_info_label, height_info_label, bmr_label, bmi_label]

frame.grid(padx=10, pady=10)

root.mainloop()
