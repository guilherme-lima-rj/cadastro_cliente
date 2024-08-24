pip install streamlit-authenticator streamlit-extras
############
import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
import yaml

# Carregar as credenciais
with open('config.yaml') as file:
    config = yaml.safe_load(file)

authenticator = stauth.Authenticate(
    config['credentials'],
    'cookie_name',
    'signature_key',
    cookie_expiry_days=30
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    st.success(f'Bem-vindo {name}')
    if st.button('Logout'):
        authenticator.logout('Logout', 'main')
        switch_page('login')
    else:
        switch_page('main')
elif authentication_status == False:
    st.error('Nome de usuário ou senha incorretos')
elif authentication_status == None:
    st.warning('Por favor, insira seu nome de usuário e senha')
##########


import streamlit as st
import streamlit_authenticator as stauth
from streamlit_extras.switch_page_button import switch_page
import yaml

# Carregar as credenciais
with open('config.yaml') as file:
    config = yaml.safe_load(file)

authenticator = stauth.Authenticate(
    config['credentials'],
    'cookie_name',
    'signature_key',
    cookie_expiry_days=30
)

st.title('Página Principal')
st.write('Você está logado com sucesso!')

if st.button('Logout'):
    authenticator.logout('Logout', 'main')
    switch_page('login')
