import streamlit as st
def calculate_emi(p,n,r):
  emi=p * (r/100) * (1 + r/100)**n / ((1+r/100)**n -1)
  return round(emi,3)

st.title('EMI Calculator App')
principal=st.slider('Principal',0,100000)
tenure=st.slider('Tenure (in years)',0,100)
roi=st.slider('Rate of Interest',0,100)
n= tenure*12
r=roi/12

if st.button('Predict'):
  emi=calculate_emi(principal,n,r)
  st.write('The EMI is', emi)