import os
import openai
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Acessa a chave da API da OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def gerar_prompt(nome, email, Linkedin, Github, formacoes, idiomas, requisitos, experiencias=None, certificacoes=None):
    """
    Gera o prompt que será enviado ao ChatGPT para adaptar o currículo.
    Adiciona detalhes de experiências, certificações se fornecidos.
    """
    prompt = f"""
    Olá, meu nome é {nome}.
    Meu email é {email}.
    Meu Linkedin é {Linkedin}.
    Meu Github é {Github}.
    Tenho formações em {formacoes}.
    Falo os seguintes idiomas: {idiomas}.
    
    Aqui estão meus requisitos para a vaga:
    {requisitos}.
    """
    
    # Adicionar experiência profissional, se fornecida
    if experiencias:
        prompt += f"""
        Experiências Profissionais:
        {experiencias}
        """
    
    # Adicionar certificações, se fornecidas
    if certificacoes:
        prompt += f"""
        Certificações:
        {certificacoes}
        """

    prompt += """
    Por favor, siga o formato de um currículo profissional, com seções e subseções claramente definidas e organizadas verticalmente. Nenhuma seção ou subtítulo deve estar ao lado de outra, todos os textos devem ser organizados um abaixo do outro. O currículo deve ter no máximo 2 páginas.

    O nome da pessoa deve estar na primeira linha, em **caixa alta** e em **negrito**, com o mesmo tamanho de um título, destacando-o. Abaixo do nome, devem ser exibidas as informações de contato, incluindo e-mail, LinkedIn e GitHub, se disponíveis. Esses dados de contato devem estar em uma linha separada e o e-mail, LinkedIn e GitHub devem estar em formato de hiperlink, clicáveis.

    Cada seção do currículo deve ter um **título em negrito** e de tamanho maior que o conteúdo da seção, facilitando a leitura. As seções devem ser: **Objetivo**, **Formação**, **Idiomas**, **Formações Complementares** se tiver, e **Habilidades** se tiver.

    A seção **Objetivo** deve conter um parágrafo objetivo, descrevendo o que a pessoa busca em termos profissionais, com um tom proativo e orientado para a aplicação dos conhecimentos, adeque esta seção de acordo com os requisitos que foram enviados pelo usuário, para garantir que o objetivo se alinhe ao que ele possui e ao que a vaga pede.

    Na seção **Formação**, cada curso deve ser descrito com nome do curso, instituição, período (se aplicável), e ano de conclusão ou previsão de conclusão. As informações devem ser separadas por barras verticais (|) para maior clareza.

    Na seção **Idiomas**, liste os idiomas que a pessoa possui conhecimento, seguido do nível de proficiência.

    A seção **Formações Complementares** deve listar cursos extracurriculares relevantes, mencionando o nome do curso, o nome da instituição ou instrutor e o ano de conclusão. Também use barras verticais (|) para separar as informações de forma clara.

    Na seção **Habilidades**, liste as habilidades relevantes, de acordo com os requisitos da vaga, em uma lista, separadas por barras verticais (|). As habilidades mais relevantes para a vaga ou área de interesse devem estar listadas primeiro.

    Use formatação simples, sem o uso de cores ou elementos gráficos. O foco deve ser no conteúdo e na clareza, garantindo que as informações sejam fáceis de ler e localizar rapidamente.
"""
    
    return prompt

def adaptar_curriculo(nome, nascimento, email, Linkedin, Github, formacoes, idiomas, requisitos):
    """
    Usa a API do ChatGPT para adaptar o currículo com base no prompt gerado.
    """
    prompt = gerar_prompt(nome, nascimento, email, Linkedin, Github, formacoes, idiomas, requisitos)
    
    try:
        response = openai.Completion.create(
            model="text-davinci-003",  
            prompt=prompt,
            max_tokens=1000,  # Ajustar conforme a necessidade
            temperature=0.7  # Controle de criatividade
        )
        
        # Extrai a resposta gerada pelo modelo
        curriculo_gerado = response['choices'][0]['text'].strip()
        
        return curriculo_gerado

    except Exception as e:
        print(f"Ocorreu um erro ao adaptar o currículo: {e}")
        return None

# Exemplo de uso
if __name__ == "__main__": 
    nome = "Leandro"
    email = "leandro@email.com"
    Linkedin = "linkedin.com/in/leandro"
    Github = "github.com/leandro"
    formacoes = "Ciência da Computação, Sistemas de Informação"
    idiomas = "Português, Inglês"
    requisitos = "Conhecimento em desenvolvimento backend, experiência com Python e Streamlit"

    curriculo = adaptar_curriculo(nome, email, Linkedin, Github, formacoes, idiomas, requisitos)
    if curriculo:
        print("Currículo adaptado:")
        print(curriculo)
