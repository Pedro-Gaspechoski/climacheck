import streamlit as st
import inteligencia

st.set_page_config(layout="wide")
chave = st.secrets["GEMINI_CHAVE"]

st.image('logotipo_climacheck.png', width=150)

st.markdown("<h1 style='text-align: center;'>CLIMACHECK</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Combatendo o negacionismo climático!</h3>", unsafe_allow_html=True)

st.write("")
st.markdown("#### Juntos contra a crise climática!")
st.write("Você pode digitar uma afirmação/pergunta abaixo ou inserir o link de uma notícia para descobrir sua veracidade.")

st.write("")
st.write("")

col1, col2 = st.columns(2)

if "info" not in st.session_state:
    st.session_state.info = ""
if "link" not in st.session_state:
    st.session_state.link = ""

with col1:
    st.session_state.info = st.text_area("Digite uma afirmação ou pergunta:", height=150, value=st.session_state.info)
    st.markdown("<style>.stTextInput input, .stTextArea textarea {color: #ffffff; background-color: #2C3E50;}</style>",
                unsafe_allow_html=True)
    if st.button("Verificar", key="verificar_info"):
        with st.spinner("Analisando as informações..."):
            if st.session_state.info:
                resultado, explicacao = inteligencia.teste(chave, st.session_state.info)
                st.markdown(f"**Resultado:** {resultado}")
                st.markdown(f"**Explicação:** {explicacao}")
            else:
                st.warning("Insira uma afirmação ou pergunta.")

    if st.button("Limpar resposta", key="limpar_info"):
        st.session_state.info = ""

with col2:
    st.session_state.link = st.text_area("Insira o link da notícia:", height=150, value=st.session_state.link)
    st.markdown("<style>.stTextInput input, .stTextArea textarea {color: #ffffff; background-color: #2C3E50;}</style>",
                unsafe_allow_html=True)
    if st.button("Verificar link", key="verificar_link"):
        with st.spinner("Analisando o link..."):
            if st.session_state.link:
                resultado_link, explicacao_link = inteligencia.verificar_link(chave, st.session_state.link)
                st.markdown(f"**Resultado:** {resultado_link}")
                st.markdown(f"**Explicação:** {explicacao_link}")
            else:
                st.warning("Insira um link.")

    if st.button("Limpar resposta", key="limpar_link"):
        st.session_state.link = ""

st.write("")
st.write("")
st.write("")
st.write("")
st.markdown("<p style='text-align: center; font-size: 12px;'>Projeto desenvolvido por Pedro Gaspechoski</p>", unsafe_allow_html=True)


