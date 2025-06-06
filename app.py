import streamlit as st
import pandas as pd 
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

modelo = LinearRegression()

x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x, y)

st.title("prevendo o valor da pizza")
st.divider()
diametro = st.number_input("informe o diametro da  pizza:")

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"o valor da pizza com diametro de {diametro:.2f} cm é de R$ {preco_previsto:.2f}")
        