import streamlit as st
import chatbot

# --- Page Config ---
st.set_page_config(
    page_title="AI Weather Chat",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- Custom CSS for Modern Dark AI Theme ---
st.markdown("""
<style>
    /* Import Modern Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Dark Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        background-size: 200% 200%;
        animation: gradientMove 10s ease infinite;
    }
    
    @keyframes gradientMove {
        0%, 100% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
    }
    
    /* Header with AI Gradient */
    h1 {
        background: linear-gradient(90deg, #00d4ff, #7b2ff7, #f107a3);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 700;
        font-size: 2.5rem !important;
        text-align: center;
        padding: 1.5rem 0 0.5rem 0;
        animation: fadeIn 0.8s ease-out;
        letter-spacing: 1px;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-15px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Caption */
    .stCaption {
        text-align: center;
        color: #a8b2d1 !important;
        font-size: 1rem;
        font-weight: 400;
        animation: fadeIn 1s ease-out 0.2s both;
        margin-bottom: 2rem;
    }
    
    /* Hide Avatar Icons */
    .stChatMessage > div:first-child {
        display: none !important;
    }
    
    /* Chat Messages - User */
    [data-testid="stChatMessage"]:has([data-testid="stChatMessageContent"]) {
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.1), rgba(123, 47, 247, 0.1));
        backdrop-filter: blur(15px);
        border-radius: 18px;
        border: 1px solid rgba(0, 212, 255, 0.2);
        padding: 1.2rem 1.5rem;
        margin: 1rem 0;
        animation: slideUp 0.4s ease-out;
        transition: all 0.3s ease;
    }
    
    /* Chat Messages - Assistant */
    .stChatMessage {
        background: linear-gradient(135deg, rgba(123, 47, 247, 0.1), rgba(241, 7, 163, 0.1));
        backdrop-filter: blur(15px);
        border-radius: 18px;
        border: 1px solid rgba(123, 47, 247, 0.2);
        padding: 1.2rem 1.5rem;
        margin: 1rem 0;
        animation: slideUp 0.4s ease-out;
        transition: all 0.3s ease;
    }
    
    .stChatMessage:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(123, 47, 247, 0.3);
        border-color: rgba(123, 47, 247, 0.4);
    }
    
    @keyframes slideUp {
        from {
            opacity: 0;
            transform: translateY(15px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    /* Message Text */
    [data-testid="stChatMessageContent"] {
        color: #e6f1ff !important;
        font-size: 1rem;
        line-height: 1.6;
    }
    
    /* Chat Input */
    .stChatInput {
        animation: fadeIn 0.8s ease-out 0.4s both;
    }
    
    .stChatInput > div {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border-radius: 28px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }
    
    .stChatInput > div:hover,
    .stChatInput > div:focus-within {
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(0, 212, 255, 0.4);
        box-shadow: 0 4px 20px rgba(0, 212, 255, 0.2);
    }
    
    .stChatInput input {
        color: #e6f1ff !important;
        font-size: 1rem;
    }
    
    .stChatInput input::placeholder {
        color: #8892b0 !important;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-color: #00d4ff !important;
        border-right-color: transparent !important;
    }
    
    /* Scrollbar */
    ::-webkit-scrollbar {
        width: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(135deg, #00d4ff, #7b2ff7);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(135deg, #7b2ff7, #f107a3);
    }
    
    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Container */
    .block-container {
        padding: 2rem 1rem;
        max-width: 800px;
    }
    
    /* Error Messages */
    .stError {
        background: rgba(255, 82, 82, 0.1);
        backdrop-filter: blur(15px);
        border-radius: 12px;
        border-left: 4px solid #ff5252;
        animation: slideUp 0.4s ease-out;
        color: #ffb3b3 !important;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        h1 {
            font-size: 2rem !important;
        }
        
        .stChatMessage {
            padding: 1rem;
        }
        
        .block-container {
            padding: 1rem 0.5rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.title("AI Weather Chat")
st.caption("Powered by AI • Get weather updates instantly")

# --- Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display Chat History ---
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Chat Input & Logic ---
if prompt := st.chat_input("Ask about weather..."):
    # 1. Display User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Get Bot Response
    with st.chat_message("assistant"):
        with st.spinner("Getting weather data..."):
            try:
                response = chatbot.ask_chatbot(prompt)
                st.markdown(response)
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                error_msg = "Unable to fetch weather data. Please try again."
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
