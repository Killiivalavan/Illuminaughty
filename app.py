import streamlit as st
from advanced_conspiracy_generator import generate_advanced_conspiracy_theory

# Set page title and configuration
st.set_page_config(
    page_title="AI Conspiracy Theorist",
    page_icon="🔍",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .reportview-container {
        background-color: #0e1117;
    }
    .main .block-container {
        padding-top: 2rem;
    }
    h1, h2, h3 {
        color: #ff4b4b;
    }
    .stButton>button {
        background-color: #ff4b4b;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🔍 AI Conspiracy Theorist")
st.markdown("Generate conspiracy theories based on your input.")

# User input
user_input = st.text_area("Enter a topic or concept for your conspiracy theory:", 
                         placeholder="Enter any topic for a conspiracy theory...",
                         height=100)

# Advanced options
with st.expander("Advanced Options"):
    col1, col2 = st.columns(2)
    with col1:
        model_options = ["llama3.2:latest"]
        selected_model = st.selectbox("Select model:", model_options)
    with col2:
        creativity = st.slider("Creativity level:", min_value=0.1, max_value=1.0, value=0.85, step=0.05, 
                             help="Higher values produce more creative outputs")

# Generate button
if st.button("Generate Conspiracy Theory"):
    if user_input:
        with st.spinner("Generating conspiracy theory... This may take a minute."):
            conspiracy_theory = generate_advanced_conspiracy_theory(
                user_input, 
                model=selected_model,
                temperature=creativity
            )
            
            # Display the conspiracy theory
            st.markdown("## Generated Conspiracy Theory")
            
            # Check for filtering
            if any(phrase in conspiracy_theory.lower() for phrase in ["i can't", "cannot", "unable to", "not appropriate", "ethical", "against my", "sorry", "inappropriate"]):
                st.error("The AI had trouble generating content on this topic. Try rephrasing or selecting a different topic.")
            else:
                # Success - display the theory directly
                st.markdown(conspiracy_theory)
                
                # Add a download button for the theory
                st.download_button(
                    label="Download as Text",
                    data=conspiracy_theory,
                    file_name="conspiracy_theory.txt",
                    mime="text/plain"
                )
    else:
        st.error("Please enter a topic for your conspiracy theory.")

# Information about the approach
with st.expander("About the Conspiracy Generator"):
    st.markdown("""
    This generator creates elaborate conspiracy narratives using advanced AI techniques.
    
    **How it works:**
    1. The system uses creative writing techniques
    2. Each narrative includes elements like:
       - A compelling premise or theory
       - Background and context
       - Key players and motivations
       - "Evidence" and connections
       - Implications and significance
    
    **Features:**
    - Creates compelling narratives
    - Uses convincing language and terminology
    - References organizations and concepts
    - Maintains a creative storytelling approach
    """)

st.markdown("---")
st.markdown("This is an MVP for the AI Conspiracy Theorist project.") 