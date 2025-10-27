# streamlit_app.py
import streamlit as st
from PIL import Image

# ---------- Page Config ----------
st.set_page_config(
    page_title="Chiti Nkhuwa — Portfolio",
    page_icon="🧑‍💻",
    layout="wide",
)

# ---------- Sidebar / Navigation ----------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Skills", "Education & Certifications", "Contact"])

ACCENT_COLOR = "#5BC0EB"  # light blue

# ---------- Helper functions ----------
def show_project_card(title, summary, link=None):
    st.subheader(title)
    st.write(summary)
    if link:
        st.markdown(f"[View Project]({link})")
    st.markdown("---")

# ---------- Pages ----------
if page == "Home":
    st.title("Chiti Nkhuwa")
    st.markdown(f"### Data Scientist")
    
    cols = st.columns([1,2])
    with cols[0]:
        try:
            st.image("assets/headshot.jpg", caption="Chiti Nkhuwa", width=200)
        except:
            st.write("")  # optional headshot
    with cols[1]:
        st.markdown("""
        **Professional Summary:**  
        Versatile professional with a Master’s in Business Analytics and AWS certification, blending machine learning expertise with a solid background in finance and operations. Skilled in building and deploying ML/AI models on GitHub and Hugging Face, with real-world applications in resource optimization, agriculture, mining, and sustainability.
        """)
        st.markdown("**Connect with me:**")
        st.markdown(f"[LinkedIn](https://www.linkedin.com/in/chiti-nkhuwa-62b414159/) | [GitHub](https://github.com/ChitiNkhuwa) | [Hugging Face](https://huggingface.co/ChitiN7) | [Email](mailto:cnkhuwacn7@gmail.com)")

elif page == "Projects":
    st.title("Projects & Case Studies")
    show_project_card(
        title="Smart Leaf: Deep Learning-Based Multi-Crop Disease Detection",
        summary="SmartLeaf focuses on building a convolutional neural network (CNN) to classify and detect diseases in four crop species (Corn, Potato, Rice, and Wheat).",
        link="https://github.com/ChitiNkhuwa/Smart-Leaf-Disease-Detector"
    )
    show_project_card(
        title="MLPayGrade: Predicting Salaries in the Machine Learning Job Market",
        summary="MLPayGrade is an end-to-end project built on 2024 salary data for machine learning-related roles.",
        link="https://huggingface.co/spaces/ChitiN7/ML_Salary_Predictor"
    )
    show_project_card(
        title="AI-Notetaker",
        summary="A useful notetaker that transcribes uploaded audio files or voice recordings made on the cloud.",
        link="https://huggingface.co/spaces/ChitiN7/ai-notetaker"
    )
    show_project_card(
        title="EduSpend: Global Higher-Education Cost Analytics & Planning",
        summary="EduSpend transforms a rich international dataset of tuition fees, living-cost indices, rent, visa charges, and insurance premiums into actionable insights for students, consultants, and policymakers.",
        link="https://github.com/ChitiNkhuwa/EduSpend-Cost-Predictor"
    )
    st.info("More projects coming soon!")

elif page == "Skills":
    st.title("Technical Skills")
    st.markdown(f"**Machine Learning & AI:** Regression, Classification, Clustering, CNNs, XGBoost, Random Forest, LLMs")
    st.markdown(f"**Deep Learning Tools:** PyTorch, TensorFlow, Keras")
    st.markdown(f"**Cloud & Dev Tools:** AWS (EC2, S3, EBS), Git, Streamlit, Gradio")
    st.markdown(f"**Data Analysis:** Pandas, NumPy, Matplotlib, SQL (PostgreSQL)")
    st.markdown(f"**Finance Background:** Cost accounting, asset management, reconciliations")
    st.markdown(f"**Programming Languages:** Python, R")
    
elif page == "Education & Certifications":
    st.title("Education & Certifications")
    st.subheader("Education")
    st.markdown("- **Grand Canyon University, Phoenix, AZ** — MSc in Business Analytics (2020–2022)")
    st.markdown("- **Minot State University, Minot, ND** — Bachelor’s Degree in Accounting (2015–2019)")
    st.subheader("Certifications")
    st.markdown("- AWS Certified: Cloud Practitioner")
    st.markdown("- SuperDataScience: Machine Learning, Deep Learning & AI")

elif page == "Contact":
    st.title("Contact Me")
    st.write("Reach out via email or connect through LinkedIn / GitHub / Hugging Face.")
    contact_name = st.text_input("Your Name")
    contact_email = st.text_input("Email")
    contact_message = st.text_area("Message")
    if st.button("Send Message"):
        st.success("Thank you! This is a demo — integrate with email or backend to receive messages.")
        st.write("---")
        st.write({"name": contact_name, "email": contact_email, "message": contact_message})

# Footer
st.markdown("---")
st.markdown(f"Chiti Nkhuwa | Accent color: {ACCENT_COLOR}")