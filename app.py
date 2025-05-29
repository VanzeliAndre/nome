import streamlit as st
import pandas as pd
import random
from datetime import datetime

# Simulador de verificação de colidência
base_simulada_poca = ["Tylenol", "Advil", "Dipirona", "Paracetaliv", "Panadol"]

# Função de geração de nomes fictícios (mock)
def gerar_nomes(molecula, classe, concorrentes, atributos, qtd):
    base = ["zef", "dral", "bem", "lix", "tor", "ven", "clav", "xol", "quim", "nex"]
    nomes = []
    for _ in range(qtd):
        nome = random.choice(base).capitalize() + random.choice(base)
        nomes.append(nome)
    return nomes

# Função de verificação simples de colidência com base simulada
def verificar_colidencia(nome):
    for registrado in base_simulada_poca:
        if registrado.lower()[:4] == nome.lower()[:4]:
            return f"Colidência potencial com {registrado} (simulado)"
    return "Sem colidência relevante (simulado)"

st.title("💊 Gerador de Nomes para Medicamentos")
st.markdown("Baseado na RDC 59/2014 e OS 43/2017")

# Entradas
molecula = st.text_input("Nome da Molécula *", "Paracetamol")
classe = st.text_input("Classe Terapêutica *", "Analgésico")
publico = st.text_input("Público-alvo *", "Adultos")
concorrentes = st.text_area("Concorrentes Atuais", "Tylenol, Advil, Dipirona")
atributos = st.text_area("Atributos Desejados", "Eficácia, Rapidez, Segurança")
derivar_dci = st.selectbox("Derivar da DCI?", ["Sim", "Não"])
restricoes = st.text_area("Restrições ou Observações", "Evitar palavras que remetam a efeitos colaterais")
qtd = st.slider("Quantidade de nomes a gerar", 5, 20, 10)

if st.button("Gerar Nomes"):
    nomes = gerar_nomes(molecula, classe, concorrentes, atributos, qtd)
    resultados = []
    for nome in nomes:
        status = verificar_colidencia(nome)
        resultados.append({"Nome Gerado": nome, "Status": status})

    df_resultado = pd.DataFrame(resultados)
    st.dataframe(df_resultado)

    # Exportação
    csv = df_resultado.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Baixar resultado em CSV",
        data=csv,
        file_name=f"nomes_gerados_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv"
    )
