import streamlit as st
import openai
from PIL import Image

openai.api_key = st.secrets["OPENAI_API_KEY"]

# ===== CONFIGURAÇÃO VISUAL =====
st.set_page_config(page_title="med.ai", layout="wide")

# ===== CSS =====
st.markdown("""
    <style>
    html, body, [class*="css"] {
        background-color: #0f0f0f;
        color: #00ff88;
    }
    .stTextInput > div > input {
        background-color: #1c1c1c;
        color: #00ff88;
        border: 1px solid #00ff88;
        border-radius: 8px;
    }
    .stButton > button {
        background-color: #00ff88;
        color: black;
        border-radius: 8px;
        font-weight: bold;
    }
    .social-icons {
        display: flex;
        gap: 10px;
        justify-content: center;
        margin-bottom: 20px;
    }
    .social-icons a {
        text-decoration: none;
        color: #00ff88;
        font-size: 20px;
    }
    .logo {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 200px;
    }
    </style>
""", unsafe_allow_html=True)

# ===== LOGO LOCAL =====
logo_path = "logo_medai.png"  # 🔥 Só troca isso aqui pelo nome do seu arquivo
logo = Image.open(logo_path)
st.image(logo, width=200)

# ===== IDIOMA =====
idioma = st.selectbox("🌐 Escolha o idioma / Choose the language:", ["Português", "English"])

# ===== REDES SOCIAIS =====
st.markdown("""
<div class="social-icons">
    <a href="https://www.instagram.com/med.ai2025?igsh=MThpMzR0Z3dyZmhqbw==" target="_blank">📸 Instagram</a>
    <a href="https://x.com/Media1462180?t=NQGOQgyrxB0J7fVcscp7xQ&s=09" target="_blank">🐦 X (Twitter)</a>
</div>
""", unsafe_allow_html=True)

# ===== TEXTOS DEPENDENDO DO IDIOMA =====
if idioma == "Português":
    titulo = "💊 med.ai — Assistente Inteligente de Medicamentos"
    placeholder = "❓ Digite sua pergunta:"
    exemplo = "_Exemplo: posso tomar dipirona com febre?_"
    carregando = "Consultando inteligência médica..."
    resposta_titulo = "### 🧠 Resposta da med.ai:"
    aviso_erro = "Erro ao consultar a IA:"
    prompt_base = """
Você é uma IA médica chamada med.ai. Quando alguém te pergunta sobre um medicamento ou situação de saúde,
você responde com base em conhecimento científico, de forma responsável, clara e educativa.

Sempre adicione:
- Nome do medicamento (se houver)
- Para que serve
- Como geralmente é usado (posologia comum)
- Efeitos colaterais possíveis
- Contraindicações comuns
- Alertas de uso indevido
- Um aviso final: "med.ai não substitui orientação médica profissional."

Evite linguagem genérica. Seja preciso, claro e empático.

Agora responda à pergunta abaixo:
"""
else:
    titulo = "💊 med.ai — Smart Medicine Assistant"
    placeholder = "❓ Type your question:"
    exemplo = "_Example: can I take dipyrone if I have a fever?_"
    carregando = "Consulting medical intelligence..."
    resposta_titulo = "### 🧠 med.ai Response:"
    aviso_erro = "Error contacting AI:"
    prompt_base = """
You are a medical AI called med.ai. When someone asks you about a medication or health situation,
you answer based on scientific knowledge, in a responsible, clear, and educational manner.

Always include:
- Name of the medication (if applicable)
- What it is used for
- Common usage (typical dosage)
- Possible side effects
- Common contraindications
- Misuse warnings
- A final note: "med.ai does not replace professional medical advice."

Avoid generic language. Be precise, clear, and empathetic.

Now answer the question below:
"""

# ===== TÍTULO =====
st.title(titulo)

# ===== PERGUNTA =====
pergunta = st.text_input(placeholder)

# ===== RESPOSTA =====
if pergunta:
    with st.spinner(carregando):
        try:
            resposta = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt_base + pergunta}],
                max_tokens=800,
                temperature=0.5
            )
            st.markdown(resposta_titulo)
            st.markdown(resposta.choices[0].message["content"])
        except Exception as e:
            st.error(f"{aviso_erro} {e}")
else:
    st.markdown(f"{exemplo}\n\n---")
