import streamlit as sl
from utilitarios import validar_dados

# Pensar em um nome para o aplicativo
sl.title("Nome do aplicativo")

sl.header("Preencha suas informações")

nome = sl.text_input("Nome Completo")
email = sl.text_input("Email")
linkedin = sl.text_input("Link do Linkedin")
formacao = sl.text_input("Formação(ões)")
idioma = sl.text_input("Idioma(s)")
requisito = sl.text_area("Requisitos da vaga")
github = sl.text_input("Github (Opcional)")
experiencia = sl.text_input("Experiência Profissional (Opcional)")
certificacao = sl.text_input("Certificação(ões) (Opcional)")

botao_enviado = False # Validação do botão sem estar pressionado

if sl.button("Enviar Dados"):
    valido, mensagem = validar_dados(nome, email, linkedin, formacao, idioma, requisito)
    if valido:
        botao_enviado = True  # Dados válidos
        sl.success("Dados enviados com sucesso!")
    else:
        sl.error(mensagem)

# Botão para baixar o currículo em PDF apenas estará visível quando as variáveis forem verificadas
if botao_enviado:
    if sl.button("Baixar Currículo em PDF"):
        sl.write("Função em desenvolvimento...")