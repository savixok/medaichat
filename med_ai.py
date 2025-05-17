import streamlit as st
import openai


openai.api_key = st.secrets["OPENAI_API_KEY"]

# Modo escuro e visual chique
st.set_page_config(page_title="med.ai", layout="wide")
st.markdown("""
    <style>
    html, body, [class*="css"]  {
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
    </style>
""", unsafe_allow_html=True)

st.title("💊 med.ai — Assistente Inteligente de Medicamentos")

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

pergunta = st.text_input("❓ Digite sua pergunta:")

if pergunta:
    with st.spinner("Consultando inteligência médica..."):
        try:
            resposta = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt_base + pergunta}],
                max_tokens=800,
                temperature=0.5
            )
            st.markdown("### 🧠 Resposta da med.ai:")
            st.markdown(resposta.choices[0].message["content"])
        except Exception as e:
            st.error(f"Erro ao consultar a IA: {e}")
else:
    st.markdown("_Exemplo: posso tomar dipirona com febre?_\n\n---")
