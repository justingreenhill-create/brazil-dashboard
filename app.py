import streamlit as st

st.set_page_config(page_title="Sollinda Brasil", page_icon="🇧🇷", layout="wide")

st.markdown("""<style>
[data-testid="stAppViewContainer"] { background-color: #f7f7f7; }
[data-testid="stSidebar"] { background-color: #002776; }
[data-testid="stSidebar"] * { color: white !important; }
[data-testid="stSidebarContent"] { padding-top: 0; }
.brand-name { font-size: 17px; font-weight: 600; color: white; margin-bottom: 2px; }
.brand-sub { font-size: 11px; color: rgba(255,255,255,0.5); margin-bottom: 14px; }
.flag-display { width: 100%; height: 64px; background: #009C3B; border-radius: 8px; border: 0.5px solid rgba(255,255,255,0.2); display: flex; align-items: center; justify-content: center; margin-bottom: 4px; }
.flag-diamond { width: 46px; height: 36px; background: #FFDF00; clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%); di.flag-circle { width: 24px; height: 24px; background: #002776; border-radius: 50%; border: 1.5px solid rgba(255,255,255,0.3); }
.topbar { background: #009C3B; padding: 12px 24px; margin: -1rem -1rem 1.5rem -1rem; border-bottom: 4px solid #002776; }
.topbar-title { font-size: 15px; font-weight: 500; color: white; }
.metric-card { background: white; border-radius: 10px; padding: 14px 16px; border: 0.5px solid #e0e0e0; border-top: 3px solid #009C3B; margin-bottom: 8px; }
.metric-card.yellow { border-top-color: #FFDF00; }
.metric-card.blue { background: #002776; border-top-color: #002776; }
.metric-label { font-size: 11px; color: #888; margin-bottom: 6px; }
.metric-value { font-size: 20px; font-weight: 500; color: #111; }
.regime-badge { display: inline-block; background: #002776; color: #FFDF00; font-size: 12px; font-weight: 500; padding: 5px 14px; border-radius: 20px; margin-bottom: 20px; }
</style><div style="padding: 20px 16px 14px; border-bottom: 0.5px solid rgba(255,255,255,0.1); margin-bottom: 12px;">
<div class="brand-name">Sollinda Brasil</div>
<div class="brand-sub">model dashboard</div>
<div class="flag-display"><div class="flag-diamond"><div class="flag-circle"></div></div></div>
</div>""", unsafe_allow_html=True)

section = st.sidebar.radio(" ", ["USD/BRL", "Ibovespa", "DI Rates", "Mean Reversion", "Momentum", "Settings"])

if section == "USD/BRL":
    st.markdown('<div class="topbar"><div class="topbar-title">USD/BRL</div></div>', unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["Model 1 - WDO Overlay", "Coming Soon"])
    with tab1:
        st.markdown('<div class="regime-badge">Regime: carry-driven</div>', unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown('<div class="metric-card"><div class="metric-label">Signal score</div><div class="metric-value">+0.62</div></div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="metric-card yellow"><div class="metric-label">Recommended</div><div class="metric-value">38 WDO</div></div>', unsafe_allow_html=True)
        with col3:
            st.markdown('<div class="metric-card blue"><div class="metric-label" style="color:rgba(255,255,255,0.6);">Margin used</div><div class="metric-value" style="color:#FFDF00;">R$68k</div></div>', unsafe_allow_html=True)
        with col4:
            st.markdown('<div class="metric-card"><div class="metric-label">USD/BRL</div><div class="metric-value">5.012</div></div>', unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.info("Model under construction. Data pipeline coming next.")
    with tab2:
        st.info("Additional USD/BRL models coming soon.")
elif section == "Ibovespa":
    st.markdown('<div class="topbar"><div class="topbar-title">Ibovespa</div></div>', unsafe_allow_html=True)
    st.info("Ibovespa models coming soon.")
elif section == "DI Rates":
    st.markdown('<div class="topbar"><div class="topbar-title">DI Rates</div></div>', unsafe_allow_html=True)
    st.info("DI Rates models coming soon.")
elif section == "Mean Reversion":
    st.markdown('<div class="topbar"><div class="topbar-title">Mean Reversion</div></div>', unsafe_allow_html=True)
    st.info("Mean Reversion models coming soon.")
elif section == "Momentum":
    st.markdown('<div class="topbar"><div class="topbar-title">Momentum</div></div>', unsafe_allow_html=True)
    st.info("Momentum models coming soon.")
elif section == "Settings":
    st.markdown('<div class="topbar"><div class="topbar-title">Settings</div></div>', unsafe_allow_html=True)
    st.subheader("Portfolio")
    st.metric("Total Portfolio", "R$ 3,051,113.65")
    st.metric("Margin Budget (5%)", "R$ 152,557")
    st.metric("USD/BRL", "5.012")
    st.metric("Max WDO Contracts", "84")
