import tkinter as tk
from tkinter import messagebox

class Matematica:
    def mcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

def calcular_mcd():
    try:
        num1 = int(entry_num1.get())
        num2 = int(entry_num2.get())
        if num1 > 0 and num2 > 0:
            matematica = Matematica()
            resultado = matematica.mcd(num1, num2)
            label_resultado.config(text=f"El MCD de {num1} y {num2} es {resultado}")
        else:
            messagebox.showerror("Error", "Por favor, ingresa números mayores a cero.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa números válidos.")


ventana = tk.Tk()
ventana.title("Cálculo del MCD")
ventana.geometry("300x250")

label_num1 = tk.Label(ventana, text="Ingresa el primer número:")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(ventana)
entry_num1.pack()

label_num2 = tk.Label(ventana, text="Ingresa el segundo número:")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(ventana)
entry_num2.pack()

btn_calcular = tk.Button(ventana, text="Calcular MCD", command=calcular_mcd)
btn_calcular.pack(pady=10)

label_resultado = tk.Label(ventana, text="")
label_resultado.pack(pady=10)

ventana.mainloop()