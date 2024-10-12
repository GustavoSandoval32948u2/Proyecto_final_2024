import tkinter as tk
from tkinter import messagebox

# Función para crear la ventana principal
def ventana_principal():
    ventana = tk.Tk()
    ventana.title("Aplicación de Álgebra Lineal")
    ventana.geometry("1200x600")  # Aumentar el tamaño de la ventana
    ventana.configure(bg="#e0f7fa")

    bienvenida_label = tk.Label(ventana, text="Bienvenido a la Aplicación de Álgebra Lineal", font=("Arial", 20), bg="#e0f7fa")
    bienvenida_label.pack(pady=20)

    multiplicar_button = tk.Button(ventana, text="Multiplicar Matrices", command=lambda: ventana_multiplicar(ventana), bg="#4db6ac", fg="white", font=("Arial", 16))
    multiplicar_button.pack(pady=10)

    ventana.mainloop()

# Ventana para la opción de multiplicar matrices
def ventana_multiplicar(ventana):
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("Multiplicar Matrices")
    nueva_ventana.geometry("1200x600")  # Aumentar el tamaño de la ventana
    nueva_ventana.configure(bg="#e0f7fa")

    # Frame para las instrucciones y entradas
    left_frame = tk.Frame(nueva_ventana, bg="#e0f7fa")
    left_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)

    instrucciones_label = tk.Label(left_frame, text="Ingresa las dimensiones de las matrices para multiplicarlas:", font=("Arial", 14), bg="#e0f7fa")
    instrucciones_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

    filas1_label = tk.Label(left_frame, text="Filas de la primera matriz:", bg="#e0f7fa", font=("Arial", 12))
    filas1_label.grid(row=1, column=0, padx=10, sticky='w')
    filas1_entry = tk.Entry(left_frame, font=("Arial", 12))
    filas1_entry.grid(row=1, column=1)

    columnas1_label = tk.Label(left_frame, text="Columnas de la primera matriz:", bg="#e0f7fa", font=("Arial", 12))
    columnas1_label.grid(row=2, column=0, padx=10, sticky='w')
    columnas1_entry = tk.Entry(left_frame, font=("Arial", 12))
    columnas1_entry.grid(row=2, column=1)

    filas2_label = tk.Label(left_frame, text="Filas de la segunda matriz:", bg="#e0f7fa", font=("Arial", 12))
    filas2_label.grid(row=3, column=0, padx=10, sticky='w')
    filas2_entry = tk.Entry(left_frame, font=("Arial", 12))
    filas2_entry.grid(row=3, column=1)

    columnas2_label = tk.Label(left_frame, text="Columnas de la segunda matriz:", bg="#e0f7fa", font=("Arial", 12))
    columnas2_label.grid(row=4, column=0, padx=10, sticky='w')
    columnas2_entry = tk.Entry(left_frame, font=("Arial", 12))
    columnas2_entry.grid(row=4, column=1)

    # Título y contexto en la parte derecha
    right_frame = tk.Frame(nueva_ventana, bg="#e0f7fa")
    right_frame.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y)

    contexto_label = tk.Label(right_frame, text="Contexto sobre la Multiplicación de Matrices", font=("Arial", 16, 'bold'), bg="#e0f7fa")
    contexto_label.pack(anchor='ne', pady=(0, 5))

    contexto_text = (
        "La multiplicación de matrices es una operación que combina dos matrices para producir una tercera matriz. "
        "Esta operación es fundamental en diversas áreas como la ingeniería, la computación y la física. "
        "Para multiplicar dos matrices, el número de columnas de la primera matriz debe ser igual al número de filas "
        "de la segunda matriz. El elemento de la fila i y columna j de la matriz resultante se calcula como la "
        "suma del producto de los elementos de la fila i de la primera matriz por los elementos de la columna j de "
        "la segunda matriz."
    )

    contexto_label_d = tk.Label(right_frame, text=contexto_text, font=("Arial", 12), bg="#e0f7fa", justify="left", wraplength=400)
    contexto_label_d.pack(anchor='ne', padx=10, pady=10)

    resultado_label = tk.Label(left_frame, text="Resultado de la multiplicación:", font=("Arial", 12), bg="#e0f7fa")
    resultado_label.grid(row=5, column=0, columnspan=2, pady=10)

    resultado_frame = tk.Frame(left_frame)
    resultado_frame.grid(row=7, column=0, columnspan=2, pady=10)

    matriz_frame = tk.Frame(left_frame)
    matriz_frame.grid(row=8, column=0, columnspan=2, pady=10)

    def crear_entradas_matrices():
        try:
            filas1 = int(filas1_entry.get())
            columnas1 = int(columnas1_entry.get())
            filas2 = int(filas2_entry.get())
            columnas2 = int(columnas2_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa números válidos.")
            return

        if columnas1 != filas2:
            messagebox.showerror("Error", "El número de columnas de la primera matriz debe coincidir con el número de filas de la segunda matriz.")
            return

        # Limpiar los marcos de la matriz y del resultado antes de generar nuevas entradas
        for widget in matriz_frame.winfo_children():
            widget.destroy()
        for widget in resultado_frame.winfo_children():
            widget.destroy()

        # Generar celdas para la primera matriz
        matriz1_entries = []
        for i in range(filas1):
            fila_entries = []
            for j in range(columnas1):
                entrada = tk.Entry(matriz_frame, width=5, font=("Arial", 12))
                entrada.grid(row=i, column=j)
                fila_entries.append(entrada)
            matriz1_entries.append(fila_entries)

        # Generar celdas para la segunda matriz
        matriz2_entries = []
        for i in range(filas2):
            fila_entries = []
            for j in range(columnas2):
                entrada = tk.Entry(matriz_frame, width=5, font=("Arial", 12))
                entrada.grid(row=i, column=j + columnas1 + 2)  # Separar la segunda matriz
                fila_entries.append(entrada)
            matriz2_entries.append(fila_entries)

        # Calcular y mostrar el resultado de la multiplicación
        def multiplicar_matrices():
            try:
                matriz1 = [[int(matriz1_entries[i][j].get()) for j in range(columnas1)] for i in range(filas1)]
                matriz2 = [[int(matriz2_entries[i][j].get()) for j in range(columnas2)] for i in range(filas2)]
                resultado = [[0] * columnas2 for _ in range(filas1)]

                for i in range(filas1):
                    for j in range(columnas2):
                        for k in range(columnas1):  # o filas2, ya que columnas1 == filas2
                            resultado[i][j] += matriz1[i][k] * matriz2[k][j]

                for i in range(filas1):
                    for j in range(columnas2):
                        entrada_resultado = tk.Label(resultado_frame, text=resultado[i][j], font=("Arial", 12))
                        entrada_resultado.grid(row=i, column=j)

            except ValueError:
                messagebox.showerror("Error", "Por favor, ingresa solo números en las matrices.")
                return

        # Botón para multiplicar las matrices
        multiplicar_button = tk.Button(left_frame, text="Multiplicar Matrices", command=multiplicar_matrices, bg="#4db6ac", fg="white", font=("Arial", 12))
        multiplicar_button.grid(row=6, column=0, columnspan=2, pady=20)

    generar_button = tk.Button(left_frame, text="Generar Entradas de Matrices", command=crear_entradas_matrices, bg="#4db6ac", fg="white", font=("Arial", 12))
    generar_button.grid(row=5, column=0, columnspan=2, pady=20)

# Ejecutar la ventana principal
ventana_principal()
