import tkinter as tk

# XOR-Funktion mit variabler Anzahl von Eingängen
def xor(*args):
    return sum(args) % 2

# Funktion zum Aktualisieren des Lampenstatus
def update_lamp():
    lampenstatus = xor(*[schalter[i].get() for i in range(len(schalter))])
    if lampenstatus:
        lampe.config(bg='yellow')
    else:
        lampe.config(bg='black')


# Erstellen des Hauptfensters
root = tk.Tk()
root.title("Treppenhausschaltung")

# Erstellen der Schalter
schalter = []
for i in range(20):
    schalter.append(tk.BooleanVar())
    schalter[i].set(False)
    tk.Checkbutton(root, text=f"Schalter {i}", variable=schalter[i], command=update_lamp, font=("Helvetica", 16)).grid(row=i, column=0, padx=10, pady=10)

# Erstellen der Lampe
lampe = tk.Label(root, text="Lampe", bg='black', width=10, height=5, font=("Helvetica", 16))
lampe.grid(row=0, column=1, rowspan=2, padx=10, pady=10)

# Start der GUI
root.mainloop()
