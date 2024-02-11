import tkinter as tk
from tkinter import ttk


def on_frequency_change(event=None):
    # Mise à jour depuis le curseur ou le champ de saisie
    try:
        frequency = float(freq_var.get())
    except ValueError:
        frequency = freq_slider.get()
    update_display(frequency)


def on_entry_change(event=None):
    # Mise à jour depuis le champ de saisie
    try:
        frequency = float(freq_var.get())
        freq_slider.set(frequency)
        update_display(frequency)
    except ValueError:
        result_var.set("Please enter a valid numeric value.")


def update_display(frequency):
    if frequency > 0:
        freq_display_var.set(f"Frequency: {frequency:.2f} MHz")
        calculate_wavelength(frequency)
    else:
        result_var.set("Frequency must be greater than 0")


def calculate_wavelength(frequency):
    wavelength = 300 / frequency
    result_var.set(f"Wave length: {wavelength:.2f} meters")


root = tk.Tk()
root.title("Wavelength Calculator")

# Ajustement pour éviter le redimensionnement non désiré
root.resizable(False, False)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

frame = ttk.Frame(root, padding="10")
frame.grid(sticky=(tk.W, tk.E, tk.N, tk.S))

freq_display_var = tk.StringVar()
result_var = tk.StringVar()
freq_var = tk.StringVar(
    value="145.800"
)  # Variable pour le champ de saisie et le curseur

freq_label = ttk.Label(frame, textvariable=freq_display_var)
freq_label.grid(column=0, row=0, sticky=tk.W, pady=2)

freq_entry = ttk.Entry(frame, textvariable=freq_var)
freq_entry.grid(column=1, row=1, sticky=(tk.W, tk.E), pady=2)
freq_entry.bind("<Return>", on_entry_change)  # Mise à jour lors de l'appui sur Entrée

freq_slider = ttk.Scale(
    frame,
    from_=1.0,
    to=1000.0,
    orient=tk.HORIZONTAL,
    variable=freq_var,
    command=on_frequency_change,
)
freq_slider.grid(column=1, row=0, sticky=(tk.W, tk.E), pady=2)

result_label = ttk.Label(frame, textvariable=result_var)
result_label.grid(column=0, row=3, columnspan=2, sticky=(tk.W, tk.E), pady=2)

# Initialisation
on_frequency_change()  # Mise à jour initiale de l'affichage

root.mainloop()
