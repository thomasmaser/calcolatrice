import tkinter as tk
window = tk.Tk()
window.title("buongiorno tenebrodo")
window.geometry("600x600")
window.resizable(False, False)
window.configure(background="pink")


# etichetta = tk.Label(window, text = "leshgo", fg = "#FF0000", font = ("Helvetica", 16))
# etichetta.grid(row = 0, column = 0, sticky = "w", padx = 10, pady =10)

# def stampa_etichetta():
#     text = "Etichetta di prova da funzione"
#     text_output = tk.Label(window, text=text, fg="#ff0000", font = ("Helvetica", 16))
#     text_output.grid(row = 1, column = 1, sticky = "w")



# first_button = tk.Button(text = "Clicca!", command = stampa_etichetta)
# first_button.grid(row = 1, column = 0, sticky="w")

# input_text = tk.Entry(window)
# input_text.grid(row = 2, column = 0, sticky = "w")

def stampa_etichetta_input():
    testo = input_text.get()
    text_output1= tk.Label(window, text= testo, fg="#FF0000", font=("Helvetica", 16))
    text_output1.grid (row = 4, column= 1, sticky = "w")

input_text = tk.Entry(window)
input_text.grid(row = 2, column = 2, sticky="w")

second_button = tk.Button(window, text= "clicca", command = stampa_etichetta_input)
second_button.grid( row = 3, column = 3, sticky="w")



if __name__ == "__main__":
    window.mainloop() #con questo comando gli sto dicendo di non farmi sparire la finestra ma di mantenerla a schermo