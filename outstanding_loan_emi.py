import streamlit as st
def calculate_emi(p,n,r):
  emi=p * (r/100) * (1 + r/100)**n / ((1+r/100)**n -1)
  return round(emi,3)
def improvised_emi_cal(p,n,r,m):
  balance= ((p*((1+(r/100))**n))-((1+(r/100))**m))/(((1+(r/100))**n)-1)
  return round(balance,3)

st.title('Imrovised EMI Calculator APP')

principal=st.slider('Principal',0,100000)
tenure=st.slider('Tenure (in years)',0,100)
roi=st.slider('Rate of Interest',0,100)
m=st.slider('Period after which the Outstanding Loan Balance is calculated (in months)')
n= tenure*12
r=roi/12

if st.button('Predict EMI'):
  emi=calculate_emi(principal,n,r)
  st.write('The EMI is', emi)

if st.button('Predict Outstanding Loan Balance'):
  outstanding_loan_balance=improvised_emi_cal(principal,n,r,m)
  st.write('The outstanding loan balance is', outstanding_loan_balance)