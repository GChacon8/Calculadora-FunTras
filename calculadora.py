import tkinter as tk
import funciones as f
from tkinter import messagebox

tolerancia= 1e-8
iteraciones= 2500

class IDE(object):
    def __init__(self, master):
        self.master = master
        self.master.title("Calc FunTras")
        self.master.geometry("600x530")
        self.master.resizable(False, False)
        self.master.configure(bg='gray')
        self.create_widgets()

    def create_widgets(self):

        # Crea un área de texto para editar el código.
        self.nombre = tk.Label(self.master)
        self.nombre = tk.Label(root, text= "Calculadora FunTras", font= ('Segoe UI', '25', 'bold'), bg= '#1E1E1E', fg='light gray')
        self.nombre.place(x= 145, y=10)

        self.inputX = tk.Text(self.master)
        self.inputX = tk.Text(root, height=1, width=30, bg= "#1E1E1E", fg='light gray')
        self.inputX.place(x= 100, y=100)

        self.inputY = tk.Text(self.master)
        self.inputY = tk.Text(root, height=1, width=30, bg= "#1E1E1E", fg='light gray')
        self.inputY.place(x= 100, y=130)

        self.output_area = tk.Text(self.master)
        self.output_area = tk.Text(root, height=1, width=30, bg= "#1E1E1E", fg='light gray', state='disabled')
        self.output_area.place(x= 100, y=190)

        self.inputX_l = tk.Label(self.master)
        self.inputX_l = tk.Label(root, text= "Input X =", font= ('Segoe UI', '10', 'bold'), bg= '#1E1E1E', fg='light gray')
        self.inputX_l.place(x= 10, y=100)

        self.inputY_l = tk.Label(self.master)
        self.inputY_l = tk.Label(root, text= "Input Y =", font= ('Segoe UI', '10', 'bold'), bg= '#1E1E1E', fg='light gray')
        self.inputY_l.place(x= 10, y=130)

        self.output_l = tk.Label(self.master)
        self.output_l = tk.Label(root, text= "Output =", font= ('Segoe UI', '10', 'bold'), bg= '#1E1E1E', fg='light gray')  
        self.output_l.place(x= 10, y=190)

        self.clear = tk.Button(self.master)
        self.clear = tk.Button(root, text="Clear Inputs", width=15, height=2,font= ('Segoe UI', '10', 'bold'), bg= '#1E1E1E', fg='light gray',command=self.clearAll)
        self.clear.place(x= 400, y=105)

        self.senh_b = tk.Button(self.master)
        self.senh_b = tk.Button(root, text="senh(x)", width=23, height=1, bg='#1E1E1E', fg='light gray', font= ('Segoe UI', '10', 'bold'), command= lambda: self.WriteResults(f.sinh_t(float(self.inputX.get("1.0", "end-1c")), iteraciones, tolerancia)))
        self.senh_b.place(x=10, y=300)
        
        self.cosh_b = tk.Button(self.master)
        self.cosh_b = tk.Button(root, text="cosh(x)",width=23, height=1, bg='#1E1E1E', fg='light gray', font= ('Segoe UI', '10', 'bold'), command= lambda: self.WriteResults(f.cosh_t(float(self.inputX.get("1.0", "end-1c")), iteraciones, tolerancia)))
        self.cosh_b.place(x=205, y=300)

        self.tanh_b = tk.Button(self.master)
        self.tanh_b = tk.Button(root, text="tanh(x)", width=23, height=1, bg='#1E1E1E', fg='light gray', font= ('Segoe UI', '10', 'bold'), command= lambda: self.WriteResults(f.tanh_t(float(self.inputX.get("1.0", "end-1c")), iteraciones, tolerancia)))
        self.tanh_b.place(x=400, y=300)

        self.asen_b = tk.Button(self.master)
        self.asen_b = tk.Button(root, text="asen(x)", width=23, height=1, bg='#1E1E1E', fg='light gray', font= ('Segoe UI', '10', 'bold'), command= lambda: self.WriteResults(f.asin_t(float(self.inputX.get("1.0", "end-1c")), iteraciones, tolerancia)))
        self.asen_b.place(x=10, y=330)

        self.acos_b = tk.Button(self.master)
        self.acos_b = tk.Button(root, text="acos(x)", width=23, height=1, bg='#1E1E1E', fg='light gray', font= ('Segoe UI', '10', 'bold'), command= lambda: self.WriteResults(f.acos_t(float(self.inputX.get("1.0", "end-1c")), iteraciones, tolerancia)))
        self.acos_b.place(x=205, y=330)

        self.atan_b = tk.Button(self.master)
        self.atan_b = tk.Button(root, text="atan(x)", width=23, height=1, bg='#1E1E1E', fg='light gray', font= ('Segoe UI', '10', 'bold'), command= lambda: self.WriteResults(f.atan_t(float(self.inputX.get("1.0", "end-1c")), iteraciones, tolerancia)))
        self.atan_b.place(x=400, y=330)

        self.sec_b = tk.Button(self.master)
        self.sec_b = tk.Button(root, text="sec(x)", width=23, height=1, bg='#1E1E1E', fg='light gray', font= ('Segoe UI', '10', 'bold'), command= lambda: self.WriteResults(f.sec_t(float(self.inputX.get("1.0", "end-1c")), iteraciones, tolerancia)))
        self.sec_b.place(x=10, y=360)


        self.csc_b = tk.Button(self.master)
        self.csc_b = tk.Button(root, text="csc(x)", width=23, height=1, bg='#1E1E1E', fg='light gray', font= ('Segoe UI', '10', 'bold'), command= lambda: self.WriteResults(f.csc_t(float(self.inputX.get("1.0", "end-1c")), iteraciones, tolerancia)))
        self.csc_b.place(x=205, y=360)

        self.cot_b = tk.Button(self.master)
        self.cot_b = tk.Button(root, text="cot(x)", width=23, height=1, bg='#1E1E1E', fg='light gray', font= ('Segoe UI', '10', 'bold'), command= lambda: self.WriteResults(f.cot_t(float(self.inputX.get("1.0", "end-1c")), iteraciones, tolerancia)))
        self.cot_b.place(x=400, y=360)

        self.sen_b = tk.Button(self.master)
        self.sen_b = tk.Button(root, text="sen(x)", width=23, height=1, bg='#1E1E1E', fg='light gray', font= ('Segoe UI', '10', 'bold'), command= lambda: self.WriteResults(f.sin_t(float(self.inputX.get("1.0", "end-1c")), iteraciones, tolerancia)))
        self.sen_b.place(x=10, y=390)

        self.cos_b = tk.Button(self.master)
        self.cos_b = tk.Button(root, text="cos(x)", width=23, height=1, bg='#1E1E1E', fg='light gray', font= ('Segoe UI', '10', 'bold'), command= lambda: self.WriteResults(f.cos_t(float(self.inputX.get("1.0", "end-1c")), iteraciones, tolerancia)))
        self.cos_b.place(x=205, y=390)

        self.tan_b = tk.Button(self.master)
        self.tan_b = tk.Button(root, text="tan(x)", width=23, height=1, bg='#1E1E1E', fg='light gray', font= ('Segoe UI', '10', 'bold'), command= lambda: self.WriteResults(f.tan_t(float(self.inputX.get("1.0", "end-1c")), iteraciones, tolerancia)))
        self.tan_b.place(x=400, y=390)

        self.ln_b = tk.Button(self.master)
        self.ln_b = tk.Button(root, text="ln(x)", width=23, height=1, bg='#1E1E1E', fg='light gray', font= ('Segoe UI', '10', 'bold'), command= lambda: self.WriteResults(f.in_t(float(self.inputX.get("1.0", "end-1c")), iteraciones, tolerancia)))
        self.ln_b.place(x=10, y=420)

        self.log10_b = tk.Button(self.master)
        self.log10_b = tk.Button(root, text="log10(x)", width=23, height=1, bg='#1E1E1E', fg='light gray', font= ('Segoe UI', '10', 'bold'), command= lambda: self.WriteResults(f.log_t(float(self.inputX.get("1.0", "end-1c")), 10, iteraciones, tolerancia)))
        self.log10_b.place(x=205, y=420)

        self.log2_b = tk.Button(self.master)
        self.log2_b = tk.Button(root, text="log2(x)", width=23, height=1, bg='#1E1E1E', fg='light gray', font= ('Segoe UI', '10', 'bold'), command= lambda: self.WriteResults(f.log_t(float(self.inputX.get("1.0", "end-1c")), 2, iteraciones, tolerancia)))
        self.log2_b.place(x=400, y=420)

        self.div1x_b = tk.Button(self.master)
        self.div1x_b = tk.Button(root, text="1/x", width=23, height=1, bg='#1E1E1E', fg='light gray', font= ('Segoe UI', '10', 'bold'), command= lambda: self.WriteResults(f.div_t(float(self.inputX.get("1.0", "end-1c")), iteraciones, tolerancia)))
        self.div1x_b.place(x=10, y=450)

        self.sqrt_b = tk.Button(self.master)
        self.sqrt_b = tk.Button(root, text="sqrt(x)", width=23, height=1, bg='#1E1E1E', fg='light gray', font= ('Segoe UI', '10', 'bold'), command= lambda: self.WriteResults(f.sqrt_t(float(self.inputX.get("1.0", "end-1c")), iteraciones, tolerancia)))
        self.sqrt_b.place(x=205, y=450)

        self.YrtX_b = tk.Button(self.master)
        self.YrtX_b = tk.Button(root, text="Yrt(x)", width=23, height=1, bg='#1E1E1E', fg='light gray', font= ('Segoe UI', '10', 'bold'), command= lambda: self.WriteResults(f.root_t(float(self.inputX.get("1.0", "end-1c")), float(self.inputY.get("1.0", "end-1c")), iteraciones, tolerancia)))
        self.YrtX_b.place(x=400, y=450)

        self.exp_b = tk.Button(self.master)
        self.exp_b = tk.Button(root, text="exp(x)", width=23, height=1, bg='#1E1E1E', fg='light gray', font= ('Segoe UI', '10', 'bold'), command= lambda: self.WriteResults(f.exp_t(float(self.inputX.get("1.0", "end-1c")), iteraciones, tolerancia)))
        self.exp_b.place(x=10, y=480)

        self.xpwry_b = tk.Button(self.master)
        self.xpwry_b = tk.Button(root, text="x^y", width=23, height=1, bg='#1E1E1E', fg='light gray', font= ('Segoe UI', '10', 'bold'), command= lambda: self.WriteResults(f.power_t(float(self.inputX.get("1.0", "end-1c")), float(self.inputY.get("1.0", "end-1c")))))
        self.xpwry_b.place(x=205, y=480)

        self.factx_b = tk.Button(self.master)
        self.factx_b = tk.Button(root, text="x!", width=23, height=1, bg='#1E1E1E', fg='light gray', font= ('Segoe UI', '10', 'bold'), command= lambda: self.WriteResults(f.fac(float(self.inputX.get("1.0", "end-1c")))))
        self.factx_b.place(x=400, y=480)


    def clearAll(self, event=None):
        self.inputX.delete("1.0", tk.END)
        self.inputY.delete("1.0", tk.END)
        self.output_area.config(state='normal') 
        self.output_area.delete("1.0", tk.END)
        self.output_area.config(state='disabled')  


    def WriteResults(self, result):
        if isinstance(result, tuple):
            result= result[0]
        self.output_area.config(state='normal')
        self.output_area.delete("1.0", tk.END) 
        self.output_area.insert("1.0", result)
        self.output_area.config(state='disabled')  

root = tk.Tk()
app = IDE(root)
root.mainloop()
