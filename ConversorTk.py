import tkinter as tk
erro = ValueError


def converterMetros():
    try:
        
        cm = float(va_cm.get())
        
        
        metros = cm / 100
        
        
        texto_resultado.config(text=f"{cm} centímetros é igual a {metros} metros.")
    except erro:
        
        texto_resultado.config(text="Por favor, insira um valor válido.")


janela = tk.Tk()
janela.title("Conversor do Tigrinho")

texto_cm = tk.Label(janela, text="Centímetros:")
texto_cm.grid(row=0, column=0, padx=10, pady=5)

va_cm = tk.Entry(janela)
va_cm.grid(row=0, column=1, padx=10, pady=5)

botao_converter = tk.Button(janela, text="Converter", command=converterMetros)
botao_converter.grid(row=1, columnspan=2, padx=10, pady=5)

texto_resultado = tk.Label(janela, text="")
texto_resultado.grid(row=2, columnspan=2, padx=10, pady=5)


janela.mainloop()
