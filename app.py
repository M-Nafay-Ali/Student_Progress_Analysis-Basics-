import streamlit as str
import pandas as pd
import numpy as np
import pickle

# --- PAGE CONFIGURATION ---
str.set_page_config(
    page_title="GraduPulse - Placement Predictor",
    page_icon="🎓",
    layout="centered"
)

# --- BUBBLY & VIBRANT CUSTOM CSS ---
str.markdown("""
    <style>
    /* Import a playful font */
    @import url('https://fonts.googleapis.com/css2?family=Fredoka+One&family=Quicksand:wght@500;700&display=swap');
    
    /* Main App Background and Font Setup */
    .stApp {
        background: linear-gradient(135deg, #fbc2eb 0%, #a6c1ee 100%);
        font-family: 'Quicksand', sans-serif;
    }
    
    /* Global Card/Container styling */
    div[data-testid="stVerticalBlock"] > div {
        background-color: rgba(255, 255, 255, 0.85);
        border-radius: 24px;
        padding: 20px;
        box-shadow: 0px 10px 25px rgba(0, 0, 0, 0.05);
        margin-bottom: 15px;
    }
    
    /* Shiny Title Styling */
    .main-title {
        font-family: 'Fredoka One', cursive;
        color: #ff4b72;
        text-shadow: 2px 2px #fff, 4px 4px rgba(0,0,0,0.1);
        font-size: 3rem !important;
        text-align: center;
        margin-bottom: 5px;
    }
    
    .subtitle {
        text-align: center;
        color: #4a5568;
        font-weight: 700;
        margin-bottom: 25px;
    }

    /* Bubbly Slider Customizations */
    div[data-baseweb="slider"] {
        background-color: #ffeef2 !important;
        border-radius: 15px;
        padding: 10px;
    }
    
    /* Vibrant Bubbly Predict Button */
    .stButton > button {
        background: linear-gradient(45deg, #ff4b72, #ff8753);
        color: white !important;
        font-family: 'Fredoka One', cursive !important;
        font-size: 1.4rem !important;
        padding: 12px 35px !important;
        border-radius: 50px !important;
        border: 3px solid #ffffff !important;
        box-shadow: 0 8px 20px rgba(255, 75, 114, 0.4) !important;
        transition: all 0.3s ease-in-out !important;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: scale(1.05) rotate(-1deg);
        box-shadow: 0 12px 25px rgba(255, 75, 114, 0.6) !important;
        background: linear-gradient(45deg, #ff8753, #ff4b72);
    }
    
    /* Animation Keyframes for Success/Failure Popups */
    @keyframes popIn {
        0% { transform: scale(0.7); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }
    
    /* Result Display Cards */
    .result-card-placed {
        background: linear-gradient(135deg, #a8ff78 0%, #78ffd6 100%);
        border: 4px solid #ffffff;
        border-radius: 25px;
        padding: 25px;
        text-align: center;
        animation: popIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    
    .result-card-not {
        background: linear-gradient(135deg, #ff9999 0%, #ff5e62 100%);
        border: 4px solid #ffffff;
        border-radius: 25px;
        padding: 25px;
        text-align: center;
        color: white !important;
        animation: popIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    
    /* Floating Icon Style */
    .floating-icon {
        font-size: 3rem;
        animation: bounce 2s infinite;
        text-align: center;
    }
    
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    </style>
    """, unsafe_allow_html=True)

# --- APP HEADER ---
str.markdown('<div class="floating-icon">✏️🤖🎒</div>', unsafe_allow_html=True)
str.markdown('<h1 class="main-title">GraduPulse</h1>', unsafe_allow_html=True)
str.markdown('<p class="subtitle">Will you secure your placement? Let\'s check your behavioral stats!</p>', unsafe_allow_html=True)

str.markdown("---")

# --- USER INPUT FORM ---
# Dropped 'exam_score' and 'internet_usage' as per your notebook analysis conclusions.
str.markdown("### 📝 Enter Behavioral Metrics:")

col1, col2 = str.columns(2)

with col1:
    previous_score = str.slider("🎯 Previous Term Score", min_value=0, max_value=100, value=75, step=1)
    attendance = str.slider("🏫 Attendance Percentage (%)", min_value=0, max_value=100, value=85, step=1)
    study_hours = str.slider("⏳ Weekly Study Hours", min_value=0, max_value=24, value=6, step=1)

with col2:
    assignments_completed = str.slider("📚 Assignments Completed", min_value=0, max_value=20, value=12, step=1)
    sleep_hours = str.slider("😴 Average Sleep Hours", min_value=3, max_value=12, value=7, step=1)

str.markdown("<br>", unsafe_allow_html=True)

# --- PREDICTION ENGINE ---
if str.button("✨ Predict My Status ✨"):
    # Arrange metrics exactly as the LogisticRegression model expects (X_train schema)
    input_features = np.array([[
        previous_score,
        attendance,
        study_hours,
        assignments_completed,
        sleep_hours
    ]])
    
    try:
        # Load your trained model artifact
        with open('logistic_placement_model.pkl', 'rb') as file:
            model = pickle.load(file)
            
        prediction = model.predict(input_features)[0]
        
        str.markdown("---")
        
        # Display results with bubbly pop-up animations
        if prediction == 1:
            str.markdown("""
                <div class="result-card-placed">
                    <h2 style="color: #155724; font-family: 'Fredoka One'; font-size: 2.2rem;">🎉 Congratulations! 🎉</h2>
                    <p style="color: #155724; font-size: 1.2rem; font-weight: bold;">
                        Your habits are locked in. The model predicts you are highly likely to be <b>Placed</b>! 🚀
                    </p>
                </div>
            """, unsafe_allow_html=True)
        else:
            str.markdown("""
                <div class="result-card-not">
                    <h2 style="color: #ffffff; font-family: 'Fredoka One'; font-size: 2.2rem;">💪 Keep Pushing! 💪</h2>
                    <p style="color: #ffffff; font-size: 1.2rem; font-weight: bold;">
                        The model predicts <b>Not Placed</b> currently. Time to pick up that pencil ✏️ and boost those hours!
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
    except FileNotFoundError:
        str.error("⚠️ `logistic_placement_model.pkl` file not found! Please export your trained pipeline model first.")

