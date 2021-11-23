import pandas as pd
import streamlit as st

side_click = st.sidebar.write("Contributors: John P Weldon, Ashley Guidot, Forrest Surles, Vishwanath Subramanian")

st.image('https://image.cnbcfm.com/api/v1/image/106962967-1634709558798-gettyimages-1235570383-porzycki-cryptocu210928_npbUe.jpeg?v=1635185551', width=350)


st.markdown("### Smart Risk Movements")
st.markdown("This application assists client portfolio management by calculating transaction fees associated with transferring between Ethereum and a fund before enabling the client to initiate the transfer. The application then automates the transfer of the amount between Etherum and a fund.")

with st.form("my_form"):
        mkt_account_input = st.text_input("Enter your Market Account Address:")
        st.write(mkt_account_input)
        
        private_key_input = st.text_input("Enter your Private Key:", type="password")
        
        options = st.selectbox("Which account would you like to transfer from?",
        ["Market Account", "Eth Account"])
        
        st.markdown("The fee associated with this transaction is 21,000 GWEI.")
        
        fee_agreement = st.selectbox("Would you like to proceed with transaction?",
        ["Yes", "No"])
        
        submitted = st.form_submit_button("Submit")
        
        if submitted:
                st.write("Market Account", mkt_account_input, "Private Key", private_key_input, "Account", options, "Fee Agreement", fee_agreement)

        st.write("Outside form")

form.form_submit_button("Submit")
