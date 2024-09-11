import tkinter as tk
from tkinter import messagebox

class Matematica:
    def fibonacci(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fibonacci(n - 1) + self.fibonacci(n - 2)

    def suma_fibonacci(self, n):
        suma = 0
        for i in range(n + 1):
            suma += self.fibonacci(i)
        return suma

def calcular_fibonacci():
    try:
        num = int(entry_num.get())
        if num >= 0:
            matematica = Matematica()
            suma = matematica.suma_fibonacci(num)
            label_resultado.config(text=f"La suma de Fibonacci hasta {num} es {suma}")
        else:
            messagebox.showerror("Error", "Por favor, ingresa un número mayor o igual a cero.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido.")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Suma de Fibonacci")

# Etiqueta para la entrada
label_num = tk.Label(root, text="Ingresa un número:")
label_num.pack()

# Caja de texto para ingresar el número
entry_num = tk.Entry(root)
entry_num.pack()

# Botón para calcular Fibonacci
btn_calcular = tk.Button(root, text="Calcular Suma de Fibonacci", command=calcular_fibonacci)
btn_calcular.pack()

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(root, text="")
label_resultado.pack()

# Iniciar el bucle de la aplicación
root.mainloop()
