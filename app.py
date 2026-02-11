import streamlit as st

st.set_page_config(page_title="Auracelle Charlie 3 - War Gaming Stress-Testing Policy Governance Research Simulation/Prototype", layout="wide", initial_sidebar_state="collapsed")
st.title("🔐 Auracelle Charlie 3 - War Gaming Stress-Testing Policy Governance Research Simulation/Prototype")

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    st.markdown("### 🎮 Phase 3 Features and Functionality")

    st.markdown("**Capabilities**")

    capabilities = [
        "🌍 World Bank API (GDP, military expenditure, internet penetration)",
        "🚫 US Export Controls API (sanctions screening)",
        "💥 External shock injection system",
        "🎭 Deception detection with real-world data",
        "🗺️ 3-D Influence Map",
        "🛡️ Red Teaming Foresight",
        "🧠 Evans-AGPO-HT Cognitive Science Framework"
    ]

    for c in capabilities:
        st.write(c)


    submit = st.form_submit_button("Login")

if submit:
    if password == "charlie2025":
        st.session_state["authenticated"] = True
        st.session_state["username"] = username
        st.switch_page("pages/2_Simulation.py")
    else:
        st.error("Incorrect password. Access denied.")

if st.session_state.get("authenticated", False):
    st.switch_page("pages/2_Simulation.py")
