import streamlit as st
from groq import Groq
from datetime import datetime

# Configurar a página

st.set_page_config(page_title="Luna Bíblia Chatbot", page_icon="🙏")

# Estilizar o sidebar sempre aberto

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

# Inicializar o cliente Groq (só será usado na opção de perguntas)
API_KEY = st.secrets["API_KEY"]
client = Groq(api_key=API_KEY)

# Prompt Base para perguntas gerais
PROMPT_BASE = """
Você é Luna, uma assistente cristã especializada em conhecimento bíblico. 
Sua missão é ajudar com amor, sabedoria e humildade, sempre citando passagens da Bíblia 
e incentivando a fé em Deus. Quando não souber a resposta, seja sincera e acolhedora.
"""

# Função para gerar resposta personalizada
def gerar_resposta(pergunta_usuario):
    resposta = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": PROMPT_BASE},
            {"role": "user", "content": pergunta_usuario}
        ],
        temperature=0.7,
        max_tokens=700
    )
    return resposta.choices[0].message.content

# Função para mostrar devocional diário completo
def devocional_diario():
    devocionais = {
        0: """
🌟 **Tema: Confiança em Deus**

📖 _"Confia no Senhor de todo o teu coração e não te estribes no teu próprio entendimento."_ (Provérbios 3:5)

✍️ **Reflexão**:  
Confiar plenamente em Deus nos ensina a abrir mão de nossas limitações humanas e a descansar na sabedoria divina. Mesmo quando não entendemos os caminhos, podemos confiar que Ele nos guia para o melhor.

🙏 **Oração**:  
Senhor, ensina-me a confiar em Ti de todo o meu coração. Que eu possa entregar meus caminhos em Tuas mãos e seguir com fé, mesmo sem entender tudo. Amém.
""",
        1: """
🌟 **Tema: Perseverança**

📖 _"Bem-aventurado o homem que suporta com perseverança a provação."_ (Tiago 1:12)

✍️ **Reflexão**:  
As dificuldades fazem parte da nossa caminhada de fé. A perseverança nos molda, fortalece e nos aproxima mais de Deus. Cada prova superada é uma vitória espiritual.

🙏 **Oração**:  
Pai, fortalece meu coração para que eu persevere em meio às dificuldades. Que eu nunca desista do propósito que o Senhor tem para mim. Amém.
""",
        2: """
🌟 **Tema: Amor ao Próximo**

📖 _"Um novo mandamento vos dou: que vos ameis uns aos outros; assim como eu vos amei."_ (João 13:34)

✍️ **Reflexão**:  
Amar o próximo é o centro da mensagem de Jesus. Não se trata apenas de palavras, mas de ações práticas que demonstram compaixão, perdão e generosidade.

🙏 **Oração**:  
Senhor, ensina-me a amar como Tu amas. Que eu seja instrumento do Teu amor para todos ao meu redor. Amém.
""",
        3: """
🌟 **Tema: Esperança em Deus**

📖 _"Porque eu bem sei os pensamentos que penso de vós, diz o Senhor; pensamentos de paz e não de mal, para vos dar um futuro e uma esperança."_ (Jeremias 29:11)

✍️ **Reflexão**:  
Deus tem planos de esperança para nós, mesmo quando as circunstâncias parecem adversas. Nossa esperança não está nas coisas passageiras, mas em Deus eterno.

🙏 **Oração**:  
Deus amado, renova minha esperança a cada dia. Que eu jamais perca de vista o futuro que preparaste para mim. Amém.
""",
        4: """
🌟 **Tema: Paz Interior**

📖 _"E a paz de Deus, que excede todo o entendimento, guardará os vossos corações e as vossas mentes em Cristo Jesus."_ (Filipenses 4:7)

✍️ **Reflexão**:  
A paz de Deus não depende das circunstâncias externas. Mesmo em meio às tempestades da vida, podemos encontrar serenidade e segurança no amor de Cristo.

🙏 **Oração**:  
Senhor Jesus, dá-me a paz que só Tu podes dar. Guarda meu coração e minha mente de toda ansiedade. Amém.
""",
        5: """
🌟 **Tema: Gratidão**

📖 _"Rendei graças ao Senhor, porque ele é bom; porque a sua misericórdia dura para sempre."_ (Salmos 136:1)

✍️ **Reflexão**:  
A gratidão abre nossos olhos para reconhecer a bondade de Deus em todas as áreas da nossa vida. Agradecer é uma forma de adoração que nos aproxima ainda mais do Pai.

🙏 **Oração**:  
Senhor, obrigado por Tua infinita bondade e misericórdia. Ensina-me a ser sempre grato, mesmo nas pequenas coisas. Amém.
""",
        6: """
🌟 **Tema: Renovação Espiritual**

📖 _"Mas os que esperam no Senhor renovarão as suas forças, subirão com asas como águias."_ (Isaías 40:31)

✍️ **Reflexão**:  
Deus nos oferece renovação para que não desanimemos. Em Sua presença, nossas forças são restauradas e nossos sonhos, revigorados.

🙏 **Oração**:  
Deus poderoso, renova minha fé e minhas forças neste dia. Que eu possa viver segundo a Tua vontade. Amém.
"""
    }
    
    dia_semana = datetime.today().weekday()
    st.markdown(devocionais[dia_semana])

# Função para mostrar histórias bíblicas
def historias_biblicas():
    st.header("📖 Histórias Bíblicas")
    historia = st.selectbox(
        "Escolha uma história:",
        ("Criação do Mundo", "Arca de Noé", "Moisés e o Êxodo", "Davi e Golias", "Nascimento de Jesus")
    )
    if historia == "Criação do Mundo":
        st.write("Deus criou o mundo em 6 dias e no sétimo descansou. (Gênesis 1)")
    elif historia == "Arca de Noé":
        st.write("Noé construiu uma arca e salvou sua família e os animais do dilúvio. (Gênesis 6-9)")
    elif historia == "Moisés e o Êxodo":
        st.write("Moisés liderou o povo de Israel para fora do Egito, rumo à Terra Prometida. (Êxodo 3-14)")
    elif historia == "Davi e Golias":
        st.write("O jovem Davi derrotou o gigante Golias com uma pedra e sua fé. (1 Samuel 17)")
    elif historia == "Nascimento de Jesus":
        st.write("Jesus nasceu em Belém, cumprindo as promessas de Deus. (Mateus 1-2)")

# Função para mostrar ensinamentos de Jesus
def ensinamentos_de_jesus():
    st.header("🕊️ Ensinamentos de Jesus")
    st.markdown("""
- **Amar a Deus acima de tudo** (Mateus 22:37)
- **Amar o próximo como a si mesmo** (Mateus 22:39)
- **Perdoar infinitamente** (Mateus 18:21-22)
- **Ser humilde como uma criança** (Mateus 18:3-4)
- **Buscar primeiro o Reino de Deus** (Mateus 6:33)
- **Ser sal da terra e luz do mundo** (Mateus 5:13-16)
- **Dar a outra face** (Mateus 5:39)
- **Orar com sinceridade** (Mateus 6:5-6)
""")

# Função para mostrar versículos
def versiculos():
    st.header("📜 Versículos Bíblicos")
    versiculo = st.selectbox(
        "Escolha um versículo:",
        ("João 3:16", "Salmo 23", "Romanos 8:28", "Filipenses 4:13", "Salmos 119:105")
    )
    if versiculo == "João 3:16":
        st.write('"Porque Deus amou o mundo de tal maneira que deu o seu Filho unigênito."')
    elif versiculo == "Salmo 23":
        st.write('"O Senhor é o meu pastor; nada me faltará."')
    elif versiculo == "Romanos 8:28":
        st.write('"Todas as coisas cooperam para o bem daqueles que amam a Deus."')
    elif versiculo == "Filipenses 4:13":
        st.write('"Tudo posso naquele que me fortalece."')
    elif versiculo == "Salmos 119:105":
        st.write('"Lâmpada para os meus pés é a tua palavra, e luz para o meu caminho."')

# Função para mostrar princípios cristãos
def principios_cristaos():
    st.header("⚓ Princípios Cristãos")
    st.markdown("""
- **Amor**: Tudo o que Deus faz é motivado por amor. (1 João 4:8)
- **Fé**: Crer em Deus e confiar em Sua palavra. (Hebreus 11:1)
- **Perdão**: Assim como fomos perdoados, devemos perdoar. (Efésios 4:32)
- **Serviço**: Servir aos outros como Jesus serviu. (Mateus 20:28)
- **Esperança**: Nossa esperança está firmada em Cristo. (Romanos 15:13)
""")

# 🌟 Menu principal
st.sidebar.title("Menu")
categoria = st.sidebar.radio(
    "Escolha uma opção:",
    ("Pergunta", "Devocional diário", "Histórias bíblicas", "Ensinamentos de Jesus", "Versículos", "Princípios cristãos")
)

# 🌟 Direcionamento de páginas
if categoria == "Pergunta":
    st.subheader("Faça sua pergunta bíblica")
    pergunta = st.text_input("Digite sua pergunta aqui:")
    if st.button("Enviar"):
        if pergunta.strip() != "":
            resposta = gerar_resposta(pergunta)
            st.success("Resposta da Bíblia:")
            st.write(resposta)
        else:
            st.warning("Por favor, digite uma pergunta para enviar.")
elif categoria == "Devocional diário":
    devocional_diario()
elif categoria == "Histórias bíblicas":
    historias_biblicas()
elif categoria == "Ensinamentos de Jesus":
    ensinamentos_de_jesus()
elif categoria == "Versículos":
    versiculos()
elif categoria == "Princípios cristãos":
    principios_cristaos()

# Rodapé
st.markdown("---")
st.caption("🌟 Projeto de Inteligência Artificial para compartilhar sabedoria cristã com amor. 🙏")
