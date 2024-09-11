import tkinter as tk
from tkinter import messagebox

class Matematica:
    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)


def calcular_factorial():
    try:
        num = int(entry_num.get())
        if num >= 0:
            matematica = Matematica()
            resultado = matematica.factorial(num)
            label_resultado.config(text=f"El factorial de {num} es {resultado}")
        else:
            messagebox.showerror("Error", "Por favor, ingresa un número mayor o igual a cero.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")

ventana = tk.Tk()
ventana.title("Cálculo del Factorial")
ventana.geometry("300x200")

label_num = tk.Label(ventana, text="Ingresa un número:")
label_num.pack(pady=10)
entry_num = tk.Entry(ventana)
entry_num.pack()

btn_calcular = tk.Button(ventana, text="Calcular Factorial", command=calcular_factorial)
btn_calcular.pack(pady=10)

label_resultado = tk.Label(ventana, text="")
label_resultado.pack(pady=10)

ventana.mainloop()