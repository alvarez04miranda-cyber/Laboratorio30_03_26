import tkinter as tk
from tkinter import messagebox

class CalculadoraBasica:

    def __init__(self):

        self.ventana = tk.Tk()
        self.ventana.title("Calculator")
        self.ventana.geometry("300x500")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg='#1C1C1C')

        self.numero1 = ""
        self.numero2 = ""
        self.operador = None

        self.crear_display()
        self.crear_botones()

    def crear_display(self):

        frame_display = tk.Frame(self.ventana, bg='#1C1C1C')
        frame_display.pack(pady=20, padx=10, fill='both')

        self.display = tk.Entry(
            frame_display,
            font=("Arial", 30, "bold"),
            justify="right",
            bg='#F5F5F5',
            fg='black',
            relief=tk.FLAT,
            bd=10
        )

        self.display.pack(fill='both', ipady=15)

        self.actualizar_display("0")

    def actualizar_display(self, valor):
        self.display.delete(0, tk.END)
        self.display.insert(0, valor)

    def agregar_numero(self, numero):
        actual = self.display.get()

        if actual == "0":
            self.actualizar_display(str(numero))
        else:
            self.actualizar_display(actual + str(numero))

    def agregar_punto(self):
        actual = self.display.get()

        if '.' not in actual:
            self.actualizar_display(actual + ".")

    def seleccionar_operador(self, op):
        try:
            self.numero1 = float(self.display.get())
            self.operador = op
            self.actualizar_display("0")
        except:
            messagebox.showerror("Error", "Número inválido")

    def calcular(self):
        try:
            self.numero2 = float(self.display.get())

            if self.operador == '+':
                resultado = self.numero1 + self.numero2
            elif self.operador == '-':
                resultado = self.numero1 - self.numero2
            elif self.operador == '*':
                resultado = self.numero1 * self.numero2
            elif self.operador == '/':
                if self.numero2 == 0:
                    raise ZeroDivisionError
                resultado = self.numero1 / self.numero2
            else:
                return

            self.mostrar_resultado(resultado)

        except ZeroDivisionError:
            messagebox.showerror("Error", "❌ No se puede dividir entre cero")
            self.limpiar()
        except:
            messagebox.showerror("Error", "❌ Error de cálculo")
            self.limpiar()

    def mostrar_resultado(self, resultado):
        if resultado == int(resultado):
            self.actualizar_display(str(int(resultado)))
        else:
            self.actualizar_display(str(round(resultado, 8)))

    def limpiar(self):
        self.numero1 = ""
        self.numero2 = ""
        self.operador = None
        self.actualizar_display("0")

    def limpiar_entrada(self):
        self.actualizar_display("0")

    def porcentaje(self):
        try:
            valor = float(self.display.get())
            self.mostrar_resultado(valor / 100)
        except:
            messagebox.showerror("Error", "Número inválido")

    def cambiar_signo(self):
        try:
            valor = float(self.display.get())
            self.mostrar_resultado(valor * -1)
        except:
            messagebox.showerror("Error", "Número inválido")

    def raiz_cuadrada(self):
        try:
            valor = float(self.display.get())

            if valor < 0:
                messagebox.showerror("Error", "❌ No se puede calcular √ de negativo\nSugerencia: usa número positivo")
                return

            self.mostrar_resultado(valor ** 0.5)

        except:
            messagebox.showerror("Error", "Número inválido")

    def cuadrado(self):
        try:
            valor = float(self.display.get())
            self.mostrar_resultado(valor ** 2)
        except:
            messagebox.showerror("Error", "Número inválido")

    def inverso(self):
        try:
            valor = float(self.display.get())

            if valor == 0:
                messagebox.showerror("Error", "❌ No se puede dividir entre cero")
                return

            self.mostrar_resultado(1 / valor)

        except:
            messagebox.showerror("Error", "Número inválido")

    def borrar_ultimo(self):
        actual = self.display.get()

        if actual == "" or actual == "0":
            return  # ✔ no hace nada si está vacío

        nuevo = actual[:-1]

        if nuevo == "":
            nuevo = "0"

        self.actualizar_display(nuevo)

    def crear_botones(self):

        colores = {
            'bg': '#1C1C1C',
            'btn_gris': '#505050',
            'btn_naranja': '#FF9500',
            'btn_gris_claro': '#D4D4D2'
        }

        frame_botones = tk.Frame(self.ventana, bg=colores['bg'])
        frame_botones.pack(pady=10, padx=10, fill='both', expand=True)

        for i in range(6):
            frame_botones.grid_rowconfigure(i, weight=1)

        for i in range(4):
            frame_botones.grid_columnconfigure(i, weight=1)

        botones = [

            ['AC',0,0,colores['btn_gris_claro'],self.limpiar],
            ['+/-',0,1,colores['btn_gris_claro'],self.cambiar_signo],
            ['%',0,2,colores['btn_gris_claro'],self.porcentaje],
            ['/',0,3,colores['btn_naranja'],lambda:self.seleccionar_operador('/')],

            ['7',1,0,colores['btn_gris'],lambda:self.agregar_numero('7')],
            ['8',1,1,colores['btn_gris'],lambda:self.agregar_numero('8')],
            ['9',1,2,colores['btn_gris'],lambda:self.agregar_numero('9')],
            ['*',1,3,colores['btn_naranja'],lambda:self.seleccionar_operador('*')],

            ['4',2,0,colores['btn_gris'],lambda:self.agregar_numero('4')],
            ['5',2,1,colores['btn_gris'],lambda:self.agregar_numero('5')],
            ['6',2,2,colores['btn_gris'],lambda:self.agregar_numero('6')],
            ['-',2,3,colores['btn_naranja'],lambda:self.seleccionar_operador('-')],

            ['1',3,0,colores['btn_gris'],lambda:self.agregar_numero('1')],
            ['2',3,1,colores['btn_gris'],lambda:self.agregar_numero('2')],
            ['3',3,2,colores['btn_gris'],lambda:self.agregar_numero('3')],
            ['+',3,3,colores['btn_naranja'],lambda:self.seleccionar_operador('+')],

            ['C',4,0,colores['btn_gris_claro'],self.limpiar_entrada],
            ['0',4,1,colores['btn_gris'],lambda:self.agregar_numero('0')],
            ['.',4,2,colores['btn_gris'],self.agregar_punto],
            ['=',4,3,colores['btn_naranja'],self.calcular],

            ['√',5,0,colores['btn_gris_claro'],self.raiz_cuadrada],
            ['x²',5,1,colores['btn_gris_claro'],self.cuadrado],
            ['1/x',5,2,colores['btn_gris_claro'],self.inverso],
            ['←',5,3,colores['btn_gris_claro'],self.borrar_ultimo],
        ]

        for texto, fila, columna, color, comando in botones:

            btn = tk.Button(
                frame_botones,
                text=texto,
                font=("Arial", 16, "bold"),
                bg=color,
                fg='white' if color != colores['btn_gris_claro'] else 'black',
                relief=tk.FLAT,
                command=comando
            )

            btn.grid(row=fila, column=columna, sticky='nsew', padx=2, pady=2)

    def ejecutar(self):
        self.ventana.mainloop()


if __name__ == "__main__":
    app = CalculadoraBasica()
    app.ejecutar()