import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class RectaApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Gráficas de Recta")
        self.root.geometry("800x500")
        self.root.configure(bg="#ccf1e1")

        self.valores_frame = ttk.Frame(root, padding=20)
        self.valores_frame.pack(side="left", fill="y")

        self.titulo_label = ttk.Label(self.valores_frame, text="Parámetros de la recta", font=("Arial", 14, "bold"))
        self.titulo_label.pack(pady=(0, 20))

        self.pendiente_label = ttk.Label(self.valores_frame, text="Pendiente (m):")
        self.pendiente_label.pack(anchor="w")
        self.pendiente_entry = ttk.Entry(self.valores_frame, width=20)
        self.pendiente_entry.pack(pady=(0, 10))

        self.independiente_label = ttk.Label(self.valores_frame, text="Término independiente (b):")
        self.independiente_label.pack(anchor="w")
        self.independiente_entry = ttk.Entry(self.valores_frame, width=20)
        self.independiente_entry.pack(pady=(0, 20))

        self.graficar_btn = ttk.Button(self.valores_frame, text="Graficar", command=self.graficar)
        self.graficar_btn.pack(pady=(10, 0))

        self.grafica_frame = ttk.Frame(root, padding=10)
        self.grafica_frame.pack(side="right", fill="both", expand=True)

        self.mostrar_plano_vacio()

    def mostrar_plano_vacio(self):
        x = np.linspace(-10, 10, 400)
        y = np.zeros_like(x)

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot([], [])
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid(True)
        ax.set_title("Plano cartesiano")

        canvas = FigureCanvasTkAgg(fig, master=self.grafica_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def graficar(self):
        try:
            m = float(self.pendiente_entry.get())
            b = float(self.independiente_entry.get())

            x = np.linspace(-10, 10, 400)
            y = m * x + b

            fig, ax = plt.subplots(figsize=(6, 4))
            ax.plot(x, y, label=f'y = {m}x + {b}', color='blue')
            ax.axhline(0, color='black', linewidth=0.5)
            ax.axvline(0, color='black', linewidth=0.5)
            ax.set_xlim(-10, 10)
            ax.set_ylim(-10, 10)
            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.grid(True)
            ax.legend()
            plt.tight_layout()

            for widget in self.grafica_frame.winfo_children():
                widget.destroy()

            canvas = FigureCanvasTkAgg(fig, master=self.grafica_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill="both", expand=True)

        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa valores numéricos válidos.")

if _name_ == "_main_":
    root = tk.Tk()
    app = RectaApp(root)
    root.mainloop()