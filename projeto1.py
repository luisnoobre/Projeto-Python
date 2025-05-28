from tkinter import *

def calcular_imc():
    try:
        nome = entry_nome.get()
        idade = entry_idade.get()
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / (altura * altura)
        if imc < 18.5:
            classificacao, cor = "Abaixo do peso", "blue"
        elif imc < 24.9:
            classificacao, cor = "Peso normal", "green"
        elif imc < 29.9:
            classificacao, cor = "Sobrepeso", "orange"
        elif imc < 34.9:
            classificacao, cor = "Obesidade grau 1", "red"
        elif imc < 39.9:
            classificacao, cor = "Obesidade grau 2", "darkred"
        else:
            classificacao, cor = "Obesidade grau 3", "black"
        resultado.config(text="IMC: %.2f - %s" % (imc, classificacao), fg=cor)
        detalhes.config(text="%s, %s anos\nPeso: %.2f kg\nAltura: %.2f m" % (nome, idade, peso, altura), fg="black")
    except:
        resultado.config(text="Erro: verifique os dados.", fg="red")
        detalhes.config(text="", fg="black")

janela = Tk()
janela.title("Calculadora de IMC")
janela.geometry("300x400")
janela.config(bg="#f0f0f0")

frame_entrada = Frame(janela, bg="#f0f0f0")
frame_entrada.pack(pady=20)
Label(frame_entrada, text="Digite seu nome:", bg="#f0f0f0").pack()
entrada_nome_inicial = Entry(frame_entrada)
entrada_nome_inicial.pack()
Button(frame_entrada, text="Entrar", command=iniciar, bg="#4CAF50", fg="white").pack(pady=10)

msg_boas_vindas = Label(janela, text="", font=("Helvetica", 12, "bold"), bg="#f0f0f0")
msg_boas_vindas.pack()

frame_principal = Frame(janela, bg="#f0f0f0")
for texto, var in [("Nome:", "entry_nome"), ("Idade:", "entry_idade"), ("Peso (kg):", "entry_peso"), ("Altura (m):", "entry_altura")]:
    Label(frame_principal, text=texto, bg="#f0f0f0").pack()
    globals()[var] = Entry(frame_principal)
    globals()[var].pack()

Button(frame_principal, text="Calcular IMC", command=calcular_imc, bg="#4CAF50", fg="white").pack(pady=10)
resultado = Label(frame_principal, text="", font=("Helvetica", 12, "bold"), bg="#f0f0f0")
resultado.pack()
detalhes = Label(frame_principal, text="", bg="#f0f0f0")
detalhes.pack()
#Alterando
janela.mainloop()
