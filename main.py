import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('order_payments_dataset.csv')

st.title('Dashboard Data Penjualan')

st.subheader('Tabel Data Penjualan')
st.write(data)

st.subheader('Grafik Total Pembayaran per Metode Pembayaran')
total_per_payment_type = data.groupby('payment_type')['payment_value'].sum()
fig, ax = plt.subplots()
total_per_payment_type.plot(kind='bar', ax=ax)
plt.xlabel('Metode Pembayaran')
plt.ylabel('Total Pembayaran')
st.pyplot(fig)

st.subheader('Statistik Ringkasan Pembayaran')
st.write(data['payment_value'].describe())

st.sidebar.subheader('Filter Data')
min_value = st.sidebar.number_input('Nilai Minimum Pembayaran', min_value=0)
max_value = st.sidebar.number_input('Nilai Maksimum Pembayaran', min_value=0, value=1000)
filtered_data = data[(data['payment_value'] >= min_value) & (data['payment_value'] <= max_value)]
st.write('Data setelah difilter:')
st.write(filtered_data)