import streamlit as st

st.set_page_config(
    page_title="Trading Dashboard",
    page_icon="📈",
    layout="wide"
)

# Main navigation
st.sidebar.title("📈 Trading Dashboard")
st.sidebar.markdown("---")

section = st.sidebar.radio(
    "Select Section",
    [
        "🇧🇷 Brazilian Markets",
        "📊 Mean Reversion",
        "📈 Momentum",
        "⚙️ Settings"
    ]
)

# Brazilian Markets
if section == "🇧🇷 Brazilian Markets":
    st.title("🇧🇷 Brazilian Markets")
    tab1, tab2 = st.tabs(["USD/BRL Overlay", "Coming Soon"])
    with tab1:
        st.subheader("USD/BRL Overlay — WDO Futures")
        st.info("Model under construction. Data pipeline coming next.")
    with tab2:
        st.info("Additional Brazilian market strategies coming soon.")

# Mean Reversion
elif section == "📊 Mean Reversion":
    st.title("📊 Mean Reversion")
    st.info("U.S. ETF pairs strategy coming soon.")

# Momentum
elif section == "📈 Momentum":
    st.title("📈 Momentum")
    st.info("U.S. Country ETF momentum strategy coming soon.")

# Settings
elif section == "⚙️ Settings":
    st.title("⚙️ Settings")
    st.subheader("Portfolio")
    st.metric("Total Portfolio", "R$ 3,051,113.65")
    st.metric("Margin Budget (5%)", "R$ 152,557")
    st.metric("USD/BRL", "5.012")
    st.metric("Max WDO Contracts", "84")