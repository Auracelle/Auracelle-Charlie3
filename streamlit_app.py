import streamlit as st
import requests

# --- Page Config ---
st.set_page_config(
    page_title="Auracelle Charlie | Policy Stress-Testing",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Session State ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# --- Captive Page ---
if not st.session_state.authenticated:
    st.markdown("# 🧭 Auracelle Charlie")
    st.markdown("### Strategic Cognitive Decision Science Platform")
    st.markdown("---")

    st.markdown(
        '''
        **Auracelle Charlie** is a policy stress-testing and
        computational governance simulation environment.

        This platform is used to explore how policy choices behave
        under uncertainty, institutional friction, and strategic interaction.

        ⚠️ Outputs are **exploratory signals**, not predictions.
        '''
    )

    st.markdown("### Access")
    access_code = st.text_input("Enter Access Code", type="password")

    if st.button("Enter Simulation"):
        if access_code:
            st.session_state.authenticated = True
            st.experimental_rerun()
        else:
            st.warning("Access code required.")

    st.stop()

# --- Simulation Page ---
st.markdown("# 🎯 Auracelle Charlie Mission Console")
st.markdown("Policy Stress-Testing Environment")
st.markdown("---")

API_URL = st.secrets.get("API_URL", "http://localhost:8000/v1")

actor = st.selectbox(
    "Select Actor",
    ["US", "UK", "EU", "China", "Japan", "NATO"]
)

if st.button("Run Baseline Metrics"):
    with st.spinner("Querying Research Engine..."):
        try:
            r = requests.get(
                f"{API_URL}/metrics",
                params={"actor": actor},
                timeout=30
            )
            st.json(r.json())
        except Exception as e:
            st.error(f"Backend unavailable: {e}")

st.markdown("---")
st.caption("Auracelle Charlie • Strategic Cognitive Governance Simulation")
