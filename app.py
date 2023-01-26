import tkinter as tk
from tkinter import ttk, filedialog
from tkinter.messagebox import showerror

class NegativeValueException(Exception):
    pass

def BMR(s, w, a, h):
    if s == 'K':
        return 655.1 + (9.567 * w) + (1.85 * h) + (-4.68 * a)
    elif s == 'M':
        return 66.47 + (13.7 * w) + (5 * h) + (-6.76 * a)
    else:
        return


def BMI(w, h):
    return w / (h / 100) ** 2


def export_to_txt(data, button):
    file = filedialog.asksaveasfile(defaultextension=".txt",
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("All files", ".*"),
                                    ])
    for i in data:
        line = i.cget("text")
        file.write(line + "\n")
    file.close()
    button["state"] = "disabled"

class BodyParams(object):
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("540x360")
        self.root.title("Body params calculator")
        self.root.resizable(False, False)
        self.root.configure(padx=20, pady=10)
        self.options = {'padx': 5, 'pady': 5}
        self.build_gui()
        self.root.mainloop()

    def build_gui(self):
        self.frame = ttk.Frame(self.root)
        self.frame.grid(column=0, row=0, sticky="nsew")
        self.gender_label = ttk.Label(self.frame, text='Płeć')
        self.gender_label.grid(column=0, row=0, sticky='ew')

        option_list = ("K", "M")
        self.gender_selected = tk.StringVar()
        self.gender_selected.set("Wybierz płeć")
        self.gender_input = tk.OptionMenu(self.frame, self.gender_selected, *option_list)
        self.gender_input.grid(column=0, row=1, **self.options)

        self.weight_label = ttk.Label(self.frame, text='Waga (kg)')
        self.weight_label.grid(column=0, row=2, sticky='W', **self.options)

        self.weight_input = tk.DoubleVar()
        self.weight_input = ttk.Entry(self.frame, textvariable=self.weight_input)
        self.weight_input.grid(column=0, row=3, **self.options)

        self.age_label = ttk.Label(self.frame, text='Wiek (lata)')
        self.age_label.grid(column=0, row=4, sticky='W', **self.options)

        self.age_input = tk.IntVar()
        self.age_input = ttk.Entry(self.frame, textvariable=self.age_input)
        self.age_input.grid(column=0, row=5, **self.options)

        self.height_label = ttk.Label(self.frame, text='Wzrost (cm)')
        self.height_label.grid(column=0, row=6, sticky='W', **self.options)

        self.height_input = tk.IntVar()
        self.height_input = ttk.Entry(self.frame, textvariable=self.height_input)
        self.height_input.grid(column=0, row=7, **self.options)

        self.action_button = ttk.Button(self.frame, text='Policz')
        self.action_button.grid(column=0, row=9, sticky='ew', **self.options)
        self.action_button.configure(command=self.action_button_clicked)

        self.export_button = ttk.Button(self.frame, text='Exportuj do .txt')
        self.export_button.grid(column=1, row=9, sticky='ew', **self.options)
        self.export_button.configure(command=lambda: export_to_txt(self.collected_data, self.export_button))
        self.export_button['state']='disabled'

        self.info_header = ttk.Label(self.frame)
        self.info_header.grid(row=0, column=1, **self.options)

        self.weight_info_label = ttk.Label(self.frame)
        self.weight_info_label.grid(row=1, column=1, **self.options)
        self.height_info_label = ttk.Label(self.frame)
        self.height_info_label.grid(row=2, column=1, **self.options)
        self.age_info_label = ttk.Label(self.frame)
        self.age_info_label.grid(row=3, column=1, **self.options)

        self.bmr_label = ttk.Label(self.frame)
        self.bmr_label.grid(row=4, column=1, **self.options)
        self.bmi_label = ttk.Label(self.frame)
        self.bmi_label.grid(row=5, column=1, **self.options)

        self.collected_data = [self.weight_info_label, self.age_info_label, self.height_info_label, self.bmr_label,
                               self.bmi_label]

        self.frame.grid(padx=10, pady=10)

    def action_button_clicked(self):
        try:
            weight = float(self.weight_input.get())
            height = int(self.height_input.get())
            age = int(self.age_input.get())

            if weight <= 0 or height <= 0 or age <= 0:
                raise NegativeValueException
            if self.gender_selected.get() == 'Wybierz płeć':
                raise ValueError
        except ValueError:
            showerror(title='Błąd', message="Błędne lub niepełne dane")
            self.export_button['state'] = 'disabled'
        except NegativeValueException:
            showerror(title='Błąd', message="Wielkości fizyczne muszą być nieujemne!")
            self.export_button['state'] = 'disabled'
        else:
            bmr = round(BMR(self.gender_selected.get(), weight, age, height), 2)
            bmi = round(BMI(weight, height), 2)
            self.info_header.config(text="Oto Twoje dane:")
            self.bmr_val = f'BMR: {bmr} kcal'
            self.bmr_label.config(text=self.bmr_val)
            self.weight_info_label.config(text=f'Waga: {self.weight_input.get()} kg')
            self.age_info_label.config(text=f'Wiek: {self.age_input.get()} lat')
            self.height_info_label.config(text=f'Wzrost: {self.height_input.get()} cm')

            self.bmi_val = f'BMI: {bmi}'
            self.bmi_label.config(text=self.bmi_val)
            self.export_button['state'] = 'enable'

            self.weight_input.delete(0, len(self.weight_input.get()))
            self.height_input.delete(0, len(self.height_input.get()))
            self.age_input.delete(0, len(self.age_input.get()))

bk = BodyParams()
