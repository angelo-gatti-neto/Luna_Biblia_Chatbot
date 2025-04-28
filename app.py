import streamlit as st
from groq import Groq
from config import API_KEY  # Importa a sua chave Groq segura

# Inicializar o cliente Groq
client = Groq(api_key=API_KEY)

# Configurar a página
st.set_page_config(page_title="Luna Bíblia Chatbot", page_icon="🙏")

# Forçar o sidebar aberto por padrão
st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            min-width: 300px;
            max-width: 300px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Título e descrição inicial
st.title("🙏 Luna Bíblia Chatbot")
st.subheader("Sabedoria cristã ao alcance de uma pergunta!")

# Mensagem chamativa para abrir o menu
st.info("👉 Selecione uma categoria no menu à esquerda para começar!")

# Definir o Prompt Base da assistente
PROMPT_BASE = """
Você é Luna, uma assistente cristã especializada em conhecimento bíblico. 
Sua missão é ajudar com amor, sabedoria e humildade, sempre citando passagens da Bíblia 
e incentivando a fé em Deus. Quando não souber a resposta, seja sincera e acolhedora.
"""

# Função para gerar a resposta conforme a categoria
def gerar_resposta_categoria(pergunta_usuario, categoria):
    if categoria == "Pergunta":
        prompt_categoria = PROMPT_BASE
    elif categoria == "Devocional diário":
        prompt_categoria = PROMPT_BASE + "\nOfereça um devocional diário motivador e reconfortante."
    elif categoria == "Histórias bíblicas":
        prompt_categoria = PROMPT_BASE + "\nConte uma história bíblica interessante e com ensinamento."
    elif categoria == "Ensinamentos de Jesus":
        prompt_categoria = PROMPT_BASE + "\nFoque nos ensinamentos de Jesus para orientar e inspirar."
    elif categoria == "Versículos":
        prompt_categoria = PROMPT_BASE + "\nForneça um versículo bíblico com contexto explicativo."
    elif categoria == "Princípios cristãos":
        prompt_categoria = PROMPT_BASE + "\nExplique um princípio cristão fundamental de forma clara e inspiradora."
    else:
        prompt_categoria = PROMPT_BASE

    resposta = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": prompt_categoria},
            {"role": "user", "content": pergunta_usuario}
        ],
        temperature=0.7,
        max_tokens=700
    )
    return resposta.choices[0].message.content

# Sidebar para selecionar categoria
st.sidebar.header("Selecione a Categoria")

categoria = st.sidebar.radio(
    "Categorias disponíveis:",
    (
        "Pergunta",
        "Devocional diário",
        "Histórias bíblicas",
        "Ensinamentos de Jesus",
        "Versículos",
        "Princípios cristãos"
    )
)

# Campo de entrada para a pergunta
pergunta = st.text_input("Digite sua pergunta ou deixe vazio para receber conteúdo automático:")

# Botão de envio
if st.button("Enviar"):
    if not pergunta:
        pergunta = "Forneça um conteúdo relevante para a categoria selecionada."
    resposta = gerar_resposta_categoria(pergunta, categoria)
    
    st.success("Resposta da Luna Bíblia:")
    st.write(resposta)

# Rodapé
st.markdown("---")
st.caption("Projeto de Inteligência Artificial para compartilhar conhecimento bíblico de forma acolhedora. 🙏")
