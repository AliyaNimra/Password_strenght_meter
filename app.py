
import streamlit as st
import re

st.set_page_config(page_title="🔐 Password Strength Checker", layout="centered")

st.title("🔐 Password Strength Meter")
st.write("Enter a password below to check how strong it is:")

# Password input
password = st.text_input("Enter your password", type="password")

def calculate_strength(password):
    length = len(password)
    lower = re.search(r"[a-z]", password) is not None
    upper = re.search(r"[A-Z]", password) is not None
    digit = re.search(r"\d", password) is not None
    symbol = re.search(r"[^\w]", password) is not None
    common_passwords = ['password', '123456', '12345678', '000000', 'abc123']

    score = 0

    if length >= 8:
        score += 1
    if lower and upper:
        score += 1
    if digit:
        score += 1
    if symbol:
        score += 1
    if password.lower() not in common_passwords:
        score += 1

    return score

def get_strength_label(score):
    if score <= 2:
        return "❌ Weak", "red"
    elif score == 3 or score == 4:
        return "⚠️ Medium", "orange"
    else:
        return "✅ Strong", "green"

# Check password when user enters it
if password:
    score = calculate_strength(password)
    label, color = get_strength_label(score)
    st.markdown(f"**Strength:** :{color}[{label}]")
    


