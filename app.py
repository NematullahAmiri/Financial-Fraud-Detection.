import streamlit as st

st.set_page_config(
    page_title="Financial Fraud Detection Platform",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Financial Fraud Detection Platform")

st.markdown("""
### Machine Learning Based Fraud Detection System

This platform predicts fraudulent financial transactions using machine learning.
""")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Transactions", "1,048,575")

with col2:
    st.metric("Precision", "89%")

with col3:
    st.metric("Recall", "95%")

with col4:
    st.metric("ROC-AUC", "99.43%")

st.markdown("---")

st.header("Project Overview")

st.write("""
This project applies machine learning techniques to detect fraudulent financial transactions.

### Features Used

- Transaction Amount
- Sender Balance
- Receiver Balance
- Transaction Type
- Balance Error Features

### Model Performance

- Precision: 89%
- Recall: 95%
- F1 Score: 92%
- ROC-AUC: 99.43%
""")
