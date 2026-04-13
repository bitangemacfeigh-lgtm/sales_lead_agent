import streamlit as st
from agent import SalesLeadAgent

st.set_page_config(page_title="SalesLead AI", page_icon="🚀", layout="wide")

# Custom CSS for a cleaner look
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #FF4B4B; color: white; }
    .reportview-container .main .block-container { padding-top: 2rem; }
    </style>
    """, unsafe_allow_html=True) # <--- Fixed this line

st.title("💼 Sales Lead AI Agent")
st.caption("Strategic Intelligence & Outreach Generator powered by Mistral Large")

# Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1998/1998614.png", width=100)
    st.header("Control Panel")
    model_choice = st.selectbox("Intelligence Model", ["mistral-large-latest", "open-mixtral-8x22b"])
    st.divider()
    st.info("Tip: Be specific about the company's recent news (funding, mergers) for better results.")

# Input
lead_description = st.text_area("Prospect Context", height=150, 
    placeholder="e.g. Sarah Chen, VP Engineering at ShieldNet. Just raised $40M Series B...")

if st.button("🚀 Analyze & Generate Strategy"):
    if not lead_description:
        st.error("Please enter prospect details first.")
    else:
        agent = SalesLeadAgent()
        
        with st.spinner("Agent is deep-diving into the persona..."):
            try:
                # Run the pipeline
                research = agent.research_lead(lead_description)
                email = agent.draft_outreach(research)
                
                # Layout Results in Tabs
                tab1, tab2 = st.tabs(["📊 Strategic Research", "✉️ Outreach Drafts"])
                
                with tab1:
                    st.markdown(research)
                    st.download_button("Download Research", research, file_name="research.txt")
                
                with tab2:
                    st.markdown("### Primary Outreach Option")
                    st.info(email)
                    st.download_button("Download Email", email, file_name="email.txt")
                    
            except Exception as e:
                st.error(f"An error occurred: {e}")