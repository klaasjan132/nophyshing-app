import streamlit as st

# Functie om gegevens op te slaan
def save_data(username, password):
   with open("phishing_log.txt", "a") as file:
       file.write(f"Username: {username}, Password: {password}\n")

# Titel en uitleg in de web-app
st.title("Phishing Simulation")
st.write("""
   This is a phishing simulation. Never share your credentials!
   Fill in the form below to simulate a login.
""")

# Maak invoervelden voor gebruikersnaam en wachtwoord
username = st.text_input("Enter your username:")
password = st.text_input("Enter your password:", type="password")

# Als de gebruiker de knop indrukt, sla de gegevens op
if st.button("Login"):
   if username and password:
       save_data(username, password)
       st.success("This was a phishing simulation! Never share your credentials.")
   else:
       st.error("Please enter both username and password.")