# 🎓 Student Placement Predictor ✨

<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit Badge"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn Badge"/>
  <img src="https://img.shields.io/badge/Built%20With-Love%20%26%20Sparkles-ff69b4?style=for-the-badge" alt="Built With Love"/>
</p>

<p align="center">
  <font size="5"><b>🎒 Predict your academic placement outcome with a vibrant, bubbly interactive UI! ✏️</b></font>
</p>

<p align="center">
  <a href="https://student-progress-analyzer.streamlit.app/">
    <img src="https://img.shields.io/badge/🎈%20Launch%20Live%20App%20-%20Click%20Here!-ff4b72?style=for-the-badge&logo=streamlit" width="320px"/>
  </a>
</p>

---

### 🌟 About The Project
Welcome to the **Student Placement Predictor** dashboard! Moving away from basic, monotonous tabular dashboards, this interactive web application features a hyper-customized, **vibrant, shiny, and bubbly UI/UX** matching a playful student aesthetic (complete with spinning pencil details, candy-colored input fields, and bouncing cartoon animations!).

The engine utilizes a **Logistic Regression** pipeline trained on a student performance dataset of 10,000 rows. By evaluating clean behavioural indicators, it delivers immediate deployment predictions via dynamic pop-up layouts.

---

### 🚀 Interactive Features
* **✏️ Bubbly & Shiny Interface:** Custom embedded CSS styling featuring soft pastel gradients (`#fbc2eb` to `#a6c1ee`), rounded cards, and smooth micro-interactions.
* **🎯 Key Behavioural Sliders:** Smooth input selectors for your previous scores, class attendance, homework completions, and sleep schedules.
* **📦 Lightened Model Schema:** The underlying machine learning structure deliberately isolates target-leaking traits (like explicit `exam_scores`) to assure true behavioral inference.
* **🎉 Pop-In Animation Cards:** Dynamic result pop-ups that react in real-time depending on whether the student status scales to "Placed" or needs an extra study push!

---

### 📊 Model Optimization Architecture
During exploratory analysis, adding direct testing scores created an artificial 100% boundary limit due to data-leakage profiles embedded inside the synthetic dataset matrix. 

By dropping absolute exam markers and building prediction modeling around raw behavioral metrics, the **Logistic Regression** pipeline achieved a robust, balanced, and realistic **90% classification accuracy rating** on test cross-validation:

* **True Positives Registered:** 1,611 successful predictions
* **True Negatives Registered:** 193 successful predictions

---

### 🛠️ File Structure
```bash
├── app.py                         # Complete bubbly UI Streamlit application code
├── logistic_placement_model.pkl   # Exported Scikit-Learn (v1.6.1) pipeline object
├── requirements.txt               # Locked cloud ecosystem packages
└── README.md                      # This beautiful documentation file

---

🤝 Let's Connect!
If you love this design style or want to talk machine learning pipelines, reach out directly across my personal platforms:
📬 Email: englandengland271@gmail.com
💼 LinkedIn:-[https://www.linkedin.com/in/mohammed-nafay-ali-16519138a?utm_source=share_via&utm_content=profile&utm_medium=member_android]
