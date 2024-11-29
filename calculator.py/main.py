import tkinter as tk
window = tk.Tk()
window.title("calcolatrice")
window.geometry("600x800")
window.resizable(True, True)
window.configure(background="pink")

def somma():
    operazione= ""
    numero1 = int(num1.get())
    numero2 = int(num2.get())
    operazione = numero1 + numero2
    risultato = tk.Label(window, text= operazione, fg="#FF0000", font=("Helvetica", 16))
    risultato.grid (row = 4, column= 0, sticky = "w")

def sottrazione():
    operazione= ""
    numero1 = int(num1.get())
    numero2 = int(num2.get())
    operazione = numero1 - numero2
    risultato = tk.Label(window, text= operazione, fg="#FF0000", font=("Helvetica", 16))
    risultato.grid (row = 4, column= 0, sticky = "w")

def moltiplicazione():
    operazione= ""
    numero1 = int(num1.get())
    numero2 = int(num2.get())
    operazione = numero1 * numero2
    risultato = tk.Label(window, text= operazione, fg="#FF0000", font=("Helvetica", 16))
    risultato.grid (row = 4, column= 0, sticky = "w")

def divisione():
    operazione= ""
    numero1 = int(num1.get())
    numero2 = int(num2.get())
    if numero1 == 0:
        risultato = tk.Label(window, text= "infinito", fg="#FF0000", font=("Helvetica", 16))
        risultato.grid (row = 4, column= 0, sticky = "w")
    elif numero2 == 0:
        risultato = tk.Label(window, text= "impossibile", fg="#FF0000", font=("Helvetica", 16))
        risultato.grid (row = 4, column= 0, sticky = "w")
    else:
        operazione = numero1/numero2
        risultato = tk.Label(window, text= operazione, fg="#FF0000", font=("Helvetica", 16))
        risultato.grid (row = 4, column= 0, sticky = "w")


num1 = tk.Entry(window) #input text num1
num1.grid(row = 1, column = 0, sticky="w")

num2 = tk.Entry(window)
num2.grid(row = 3, column = 0, sticky="w")

più = tk.Button(text="+", command= somma)
più.grid(row = 2, column = 0, sticky = "w")

meno = tk.Button(text="-", command= sottrazione)
meno.grid(row = 2, column = 1, sticky = "w")

per = tk.Button(text="x", command= moltiplicazione)
per.grid(row = 2, column = 2, sticky = "w")

diviso = tk.Button(text="/", command= divisione)
diviso.grid(row = 2, column = 3, sticky = "w")

if __name__ == "__main__":
    window.mainloop()