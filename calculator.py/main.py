import tkinter as tk
window = tk.Tk()
window.title("calcolatrice")
window.geometry("400x400")
window.resizable(True, True)
window.configure(background="pink")

    

def somma():
    numero1 = float(num1.get())
    numero2 = float(num2.get())
    operazione = numero1 + numero2
    risultato = tk.Label(window, text= "              ", fg="white", font=("Helvetica", 16))
    #risultato.grid (row = 7, column= 2, sticky = "w")
    risultato.place(x=200, y=300, anchor="center")
    risultato = tk.Label(window, text= operazione, fg="#FF0000", font=("Helvetica", 16))
    #risultato.grid (row = 7, column= 2, sticky = "w")
    risultato.place(x=200, y=300, anchor="center")

def sottrazione():
    numero1 = float(num1.get())
    numero2 = float(num2.get())
    operazione = numero1 - numero2
    risultato = tk.Label(window, text= "              ", fg="white", font=("Helvetica", 16))
    #risultato.grid (row = 7, column= 2, sticky = "w")
    risultato.place(x=200, y=300, anchor="center")
    risultato = tk.Label(window, text= operazione, fg="#FF0000", font=("Helvetica", 16))
    #risultato.grid (row = 7, column= 2, sticky = "w")
    risultato.place(x=200, y=300, anchor="center")

def moltiplicazione():
    numero1 = float(num1.get())
    numero2 = float(num2.get())
    operazione = numero1 * numero2
    risultato = tk.Label(window, text= "              ", fg="white", font=("Helvetica", 16))
    #risultato.grid (row = 7, column= 2, sticky = "w")
    risultato.place(x=200, y=300, anchor="center")
    risultato = tk.Label(window, text= operazione, fg="#FF0000", font=("Helvetica", 16))
    #risultato.grid (row = 7, column= 2, sticky = "w")
    risultato.place(x=200, y=300, anchor="center")

def divisione():
    numero1 = float(num1.get())
    numero2 = float(num2.get())
    if numero1 == 0:
        risultato = tk.Label(window, text= "              ", fg="white", font=("Helvetica", 16))
        #risultato.grid (row = 7, column= 2, sticky = "w")
        risultato.place(x=200, y=300, anchor="center")
        risultato = tk.Label(window, text= "infinito", fg="#FF0000", font=("Helvetica", 16))
        #risultato.grid (row = 7, column= 2, sticky = "w")
        risultato.place(x=200, y=300, anchor="center")
    elif numero2 == 0:
        risultato = tk.Label(window, text= "              ", fg="white", font=("Helvetica", 16))
        #risultato.grid (row = 7, column= 2, sticky = "w")
        risultato.place(x=200, y=300, anchor="center")
        risultato = tk.Label(window, text= "impossibile", fg="#FF0000", font=("Helvetica", 16))
        #risultato.grid (row = 7, column= 2, sticky = "w")
        risultato.place(x=200, y=300, anchor="center")
    else:
        operazione = numero1/numero2
        risultato = tk.Label(window, text= "              ", fg="white", font=("Helvetica", 16))
        #risultato.grid (row = 7, column= 2, sticky = "w")
        risultato.place(x=200, y=300, anchor="center")
        risultato = tk.Label(window, text= operazione, fg="#FF0000", font=("Helvetica", 16))
        #risultato.grid (row = 7, column= 2, sticky = "w")
        risultato.place(x=200, y=300, anchor="center")
        
     

num1 = tk.Entry(window) #input text num1
#num1.grid(row = 1, column = 2, sticky="w")
num1.place(x=200, y=50, anchor="center")

num2 = tk.Entry(window)
#num2.grid(row = 5, column = 2, sticky="w")
num2.place(x=200, y=200, anchor="center")

più = tk.Button(text="+", command= somma)
#più.grid(row = 3, column = 0, sticky = "w")
più.place(x = 50, y= 125, anchor="center")

meno = tk.Button(text="-", command= sottrazione)
#meno.grid(row = 3, column = 1, sticky = "w")
meno.place(x = 150, y= 125, anchor="center")

per = tk.Button(text="x", command= moltiplicazione)
#per.grid(row = 3, column = 3, sticky = "w")
per.place(x = 250, y= 125, anchor="center")

diviso = tk.Button(text="/", command= divisione)
#diviso.grid(row = 3, column = 4, sticky = "w")
diviso.place(x = 350, y= 125, anchor="center")

if __name__ == "__main__":
    window.mainloop()