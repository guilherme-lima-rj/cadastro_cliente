import streamlit as st
import sqlite3
import pandas as pd
from banco_dados import criar_banco

def get_cliente(id):
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()
    c.execute("SELECT * FROM clientes WHERE id = ?", (id,))
    cliente = c.fetchone()
    conexao.close()
    return cliente

def get_clientes():
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()
    c.execute("SELECT * FROM clientes")
    rows = c.fetchall()
    conexao.close()
    return rows

def inserir_cliente(nome, sobrenome, email, telefone):
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()
    c.execute("INSERT INTO clientes (nome, sobrenome, email, telefone) VALUES (?, ?, ?, ?)",
              (nome, sobrenome, email, telefone))
    conexao.commit()
    conexao.close()

def atualizar_cliente(id, nome, sobrenome, email, telefone):
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()
    c.execute("UPDATE clientes SET nome = ?, sobrenome = ?, email = ?, telefone = ? WHERE id = ?",
              (nome, sobrenome, email, telefone, id))
    conexao.commit()
    conexao.close()

def deletar_cliente(id):
    conexao = sqlite3.connect('clientes.db')
    c = conexao.cursor()
    c.execute("DELETE FROM clientes WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()

criar_banco()

st.title("Sistema de Cadastro de Clientes")

# Estilizando o menu fixo à esquerda
st.markdown("""
    <style>
     .sidebar .sidebar-content h1 {
        font-size: 26px;
    }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.markdown("<h1>Menu</h1>", unsafe_allow_html=True)

menu = ["Inserir", "Consultar", "Atualizar", "Deletar"]
choice = st.sidebar.radio("", menu)

if choice == "Inserir":
    st.subheader("Inserir Cliente")
    nome = st.text_input("Nome")
    sobrenome = st.text_input("Sobrenome")
    email = st.text_input("Email")
    telefone = st.text_input("Telefone")
    if st.button("Inserir"):
        inserir_cliente(nome, sobrenome, email, telefone)
        st.success("Cliente inserido com sucesso!")

elif choice == "Consultar":
    st.subheader("Consultar Clientes")
    clientes = get_clientes()
    df = pd.DataFrame(clientes, columns=["ID", "Nome", "Sobrenome", "Email", "Telefone"])
    cliente_selecionado = st.selectbox("Selecione um cliente para atualizar", df["ID"])
    if st.button("Atualizar Cliente Selecionado"):
        st.session_state["cliente_id"] = cliente_selecionado
        st.rerun()

elif choice == "Atualizar":
    st.subheader("Atualizar Cliente")
    if "cliente_id" in st.session_state:
        id = st.session_state["cliente_id"]
        cliente = get_cliente(id)
        if cliente:
            st.text_input("ID Cliente: ",value=cliente[0], disabled=True)
            nome = st.text_input("Nome", value=cliente[1])
            sobrenome = st.text_input("Sobrenome", value=cliente[2])
            email = st.text_input("Email", value=cliente[3])
            telefone = st.text_input("Telefone", value=cliente[4])
            if st.button("Atualizar"):
                atualizar_cliente(id, nome, sobrenome, email, telefone)
                st.success("Cliente atualizado com sucesso!")
        else:
            st.error("Cliente não encontrado.")
    else:
        st.error("Nenhum cliente selecionado para atualização.")

elif choice == "Deletar":
    st.subheader("Deletar Cliente")
    id = st.number_input("ID do Cliente", min_value=1, step=1)
    if st.button("Deletar"):
        deletar_cliente(id)
        st.success("Cliente deletado com sucesso!")
