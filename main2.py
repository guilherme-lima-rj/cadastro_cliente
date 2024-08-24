import streamlit as st
import requests

def get_address(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

st.title("Consulta de Endereço por CEP")
cep_input = st.text_input("Digite o CEP: ")

if cep_input:
    address = get_address(cep_input)
    
    if address:
        st.info(f"**Endereço:** {address['logradouro']}")
        st.info(f"**Bairro:** {address['bairro']}")
        st.info(f"**Cidade:** {address['localidade']}")
        st.info(f"**Estado:** {address['uf']}")
    else:
        st.error("CEP não encontrado.")
