def validar_nome(nome):
    if not nome or any(char.isdigit() for char in nome):
        return False, "Nome inválido. Não deve conter números ou estar vazio."
    return True, ""

def validar_email(email):
    if not email:
        return False, "Email é obrigatório."
    return True, ""

def validar_linkedin(linkedin):
    if not linkedin:
        return False, "O Link do Linkedin é obrigatório."
    return True, ""

def validar_formacao(formacao):
    if not formacao:
        return False, "Formação é obrigatória."
    return True, ""

def validar_idioma(idioma):
    if not idioma:
        return False, "Idioma é obrigatório."
    return True, ""

def validar_requisito(requisito):
    if not requisito:
        return False, "Requisitos da vaga são obrigatórios."
    return True, ""

def validar_dados(nome, email, linkedin, formacao, idioma, requisito):
    validacoes = [
        validar_nome(nome),
        validar_email(email),
        validar_linkedin(linkedin),
        validar_formacao(formacao),
        validar_idioma(idioma),
        validar_requisito(requisito)
    ]
    for valido, mensagem in validacoes:
        if not valido:
            return False, mensagem
    return True, "Dados válidos."