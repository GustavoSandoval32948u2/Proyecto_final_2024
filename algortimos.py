import numpy as np
from sympy import Matrix
from tkinter import Tk, Entry, Button, Text, Frame, Label, messagebox
import tkinter as tk

class MatrixCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Multifuncional de Matrices")
        self.root.geometry("1200x800")
        self.root.configure(bg='#98FF98')

        # Marco principal para la parte izquierda (entrada y botones)
        calc_frame = Frame(root, bg='#98FF98')
        calc_frame.pack(side="left", padx=10, pady=0, anchor='n')

        # Botón de contexto
        Button(calc_frame, text="¿Qué hace cada operación?", command=self.show_context, width=20, height=2, font=("Arial", 14, "bold"), bg='orange', fg='black').pack(pady=10)

        # Etiqueta de instrucciones
        self.instruction_label = Label(calc_frame, text="Ingrese las dimensiones de la matriz:", bg='#98FF98', font=("Arial", 16, "bold"))
        self.instruction_label.pack(pady=10)

        # Campos de entrada para dimensiones
        self.rows_input = Entry(calc_frame, width=15, font=("Arial", 18))
        self.rows_input.pack(pady=5)
        self.rows_input.insert(0, "Filas (1-5)")

        self.cols_input = Entry(calc_frame, width=15, font=("Arial", 18))
        self.cols_input.pack(pady=5)
        self.cols_input.insert(0, "Columnas (1-5)")

        # Campo de entrada de la matriz
        self.matrix_input = Entry(calc_frame, width=30, font=("Arial", 18))
        self.matrix_input.pack(pady=5)

        # Botones de operación
        Button(calc_frame, text="Gauss-Jordan", command=self.gauss_jordan, width=20, height=2, font=("Arial", 14, "bold"), bg='blue', fg='white').pack(pady=12)
        Button(calc_frame, text="Regla de Cramer", command=self.cramer, width=20, height=2, font=("Arial", 14, "bold"), bg='blue', fg='white').pack(pady=12)
        Button(calc_frame, text="Multiplicación de Matrices", command=self.multiplicar, width=20, height=2, font=("Arial", 14, "bold"), bg='blue', fg='white').pack(pady=12)
        Button(calc_frame, text="Matriz Inversa", command=self.inversa, width=20, height=2, font=("Arial", 14, "bold"), bg='blue', fg='white').pack(pady=12)

        # Marco para el área de resultados
        result_frame = Frame(root, bg='#98FF98')
        result_frame.pack(side="left", padx=10, pady=0, anchor='n')

        # Etiqueta de resultados
        result_label = Label(result_frame, text="Resultado", bg='#98FF98', font=("Arial", 16, "bold"), fg='black')
        result_label.pack(pady=3)

        # Área de texto para mostrar resultados
        self.result_text = Text(result_frame, wrap="word", width=40, height=20, font=("Courier", 20, "bold"), bg='#f0f0f0', fg='black', relief="flat")
        self.result_text.pack(pady=5, fill="both", expand=True)

    def show_context(self):
        context_message = (
            "1. Método de Gauss-Jordan: Implementa la eliminación Gaussiana para hallar soluciones de sistemas de ecuaciones lineales.\n"
            "2. Regla de Cramer: Resuelve sistemas de ecuaciones lineales utilizando determinantes.\n"
            "3. Multiplicación de matrices: Implementa la multiplicación entre dos matrices de tamaño n x n.\n"
            "4. Cálculo de la matriz inversa: Proporciona la opción de calcular la matriz inversa de una matriz cuadrada, si esta existe."
        )
        messagebox.showinfo("Contexto de Operaciones", context_message)

    def get_matrix(self):
        try:
            # Obtener la matriz de la entrada del usuario
            rows = int(self.rows_input.get())
            cols = int(self.cols_input.get())
            if rows < 1 or rows > 5 or cols < 1 or cols > 5:
                raise ValueError("Las dimensiones deben estar entre 1 y 5.")
            
            matrix_input = self.matrix_input.get()
            if '|' in matrix_input:
                matrices = matrix_input.split('|')
                if len(matrices) != 2:
                    raise ValueError("Ingrese dos matrices separadas por '|' para la multiplicación.")
                matrices = [m.split(';') for m in matrices]
                matrix_a = np.array([list(map(float, row.split(','))) for row in matrices[0]])
                matrix_b = np.array([list(map(float, row.split(','))) for row in matrices[1]])
                return matrix_a, matrix_b
            else:
                rows_data = matrix_input.split(';')
                if len(rows_data) != rows or any(len(row.split(',')) != cols for row in rows_data):
                    raise ValueError(f"Ingrese exactamente {rows} filas y {cols} columnas.")
                matrix = np.array([list(map(float, row.split(','))) for row in rows_data])
                return matrix
        except ValueError as e:
            self.result_text.delete(1.0, "end")
            self.result_text.insert("end", f"Error: {e}")
            return None
        except Exception as e:
            self.result_text.delete(1.0, "end")
            self.result_text.insert("end", f"Error en los datos de entrada: {e}")
            return None

    def format_matrix(self, matrix):
        """Convierte los valores flotantes cercanos a enteros en enteros para eliminar los .0000"""
        formatted_matrix = []
        for row in matrix:
            formatted_row = []
            for el in row:
                if abs(el - round(el)) < 1e-9:
                    formatted_row.append(int(round(el)))
                else:
                    formatted_row.append(round(el, 2))
            formatted_matrix.append(formatted_row)
        return formatted_matrix

    def gauss_jordan(self):
        matrix = self.get_matrix()
        if matrix is not None:
            try:
                self.result_text.delete(1.0, "end")
                self.result_text.insert("end", f"Paso 1: Matriz original:\n{self.format_matrix(matrix.tolist())}\n\n")
                
                m = Matrix(matrix)
                result, pivot_indices = m.rref()  # Calcular la matriz reducida por filas y los pivotes
                
                self.result_text.insert("end", "Paso 2: Aplicamos operaciones elementales para reducir la matriz:\n")
                for idx, pivot in enumerate(pivot_indices):
                    self.result_text.insert("end", f"Operación {idx + 1}: Se hace pivot en la columna {pivot + 1}\n")
                
                self.result_text.insert("end", f"Resultado final (forma escalonada):\n{self.format_matrix(result.tolist())}\n")
            except Exception as e:
                self.result_text.delete(1.0, "end")
                self.result_text.insert("end", f"Error al calcular Gauss-Jordan: {e}")

    def cramer(self):
        matrix = self.get_matrix()
        if matrix is not None:
            try:
                self.result_text.delete(1.0, "end")
                
                # Verificamos que sea un sistema cuadrado
                if matrix.shape[0] != matrix.shape[1] - 1:
                    self.result_text.insert("end", "La matriz no tiene la forma adecuada para aplicar la regla de Cramer (debe ser una matriz cuadrada aumentada).\n")
                    return
                
                m = Matrix(matrix[:, :-1])  # Coeficientes (sin términos independientes)
                det = m.det()  # Determinante de la matriz de coeficientes
                self.result_text.insert("end", f"Paso 1: Calculamos el determinante de la matriz de coeficientes:\nDeterminante = {det}\n\n")

                if det == 0:
                    self.result_text.insert("end", "El sistema no tiene solución única porque el determinante es 0.\n")
                else:
                    b = Matrix(matrix[:, -1])  # Términos independientes
                    solution = []
                    for i in range(m.shape[1]):
                        mi = m.copy()
                        mi[:, i] = b  # Reemplazamos la columna i por los términos independientes
                        det_mi = mi.det()  # Determinante de la nueva matriz
                        self.result_text.insert("end", f"Paso 2.{i+1}: Reemplazamos la columna {i+1} por los términos independientes y calculamos el nuevo determinante:\nDeterminante = {det_mi}\n\n")
                        solution.append(det_mi / det)
                    
                    self.result_text.insert("end", f"Solución final del sistema:\n{self.format_matrix([solution])}\n")
            except Exception as e:
                self.result_text.delete(1.0, "end")
                self.result_text.insert("end", f"Error al calcular la regla de Cramer: {e}")

    def multiplicar(self):
        matrices = self.get_matrix()
        if matrices is not None and isinstance(matrices, tuple):
            try:
                result = np.dot(matrices[0], matrices[1])
                self.result_text.delete(1.0, "end")
                self.result_text.insert("end", f"Resultado de la multiplicación:\n{self.format_matrix(result.tolist())}\n")
            except ValueError as e:
                self.result_text.delete(1.0, "end")
                self.result_text.insert("end", f"Error en la multiplicación: {e}")

    def inversa(self):
        matrix = self.get_matrix()
        if matrix is not None:
            try:
                m = Matrix(matrix)
                inv = m.inv()  # Calcular la inversa
                self.result_text.delete(1.0, "end")
                self.result_text.insert("end", f"Matriz inversa:\n{self.format_matrix(inv.tolist())}\n")
            except Exception as e:
                self.result_text.delete(1.0, "end")
                self.result_text.insert("end", f"Error al calcular la matriz inversa: {e}")

if __name__ == "__main__":
    root = Tk()
    app = MatrixCalculator(root)
    root.mainloop()
