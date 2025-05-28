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

def iniciar():
    nome = entrada_nome_inicial.get()
    if nome.strip() != "":
        msg_boas_vindas.config(text=f"Olá, {nome}!")
        frame_principal.pack(pady=10)
        entry_nome.insert(0, nome)  # Pré-preenche o campo "nome" com o nome digitado
        frame_entrada.pack_forget()
    else:
        msg_boas_vindas.config(text="Digite um nome válido.")

janela = Tk()
janela.title("Calculadora de IMC")
janela.geometry("300x450")
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

Label(frame_principal, text="Nome:", bg="#f0f0f0").pack()
entry_nome = Entry(frame_principal)
entry_nome.pack()

Label(frame_principal, text="Idade:", bg="#f0f0f0").pack()
entry_idade = Entry(frame_principal)
entry_idade.pack()

Label(frame_principal, text="Peso (kg):", bg="#f0f0f0").pack()
entry_peso = Entry(frame_principal)
entry_peso.pack()

Label(frame_principal, text="Altura (m):", bg="#f0f0f0").pack()
entry_altura = Entry(frame_principal)
entry_altura.pack()

Button(frame_principal, text="Calcular IMC", command=calcular_imc, bg="#4CAF50", fg="white").pack(pady=10)
resultado = Label(frame_principal, text="", font=("Helvetica", 12, "bold"), bg="#f0f0f0")
resultado.pack()
detalhes = Label(frame_principal, text="", bg="#f0f0f0")
detalhes.pack()

janela.mainloop()
