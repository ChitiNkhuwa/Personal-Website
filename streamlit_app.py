# streamlit_app.py
import streamlit as st

# ---------- Page Config ----------
st.set_page_config(
    page_title="Chiti Nkhuwa — Portfolio",
    page_icon="🧑‍💻",
    layout="wide",
)

# ---------- Sidebar / Navigation ----------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Work Experience", "Skills", "Education & Certifications"])

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
    
    # Create columns for profile picture and summary
    cols = st.columns([1, 2])
    with cols[0]:
        try:
            st.image("assets/profile_picture.jpg", caption="Chiti Nkhuwa", width=250)
        except:
            st.info("💡 **Upload your profile picture:** Place your image at `assets/profile_picture.jpg` to display it here.")
    
    with cols[1]:
        st.markdown("""
        **Professional Summary:**  
        Data Scientist with a Master's in Business Analytics and AWS certification. Skilled in building and deploying ML/AI models with real-world applications across multiple industries.
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
    show_project_card(
        title="Mineral Identification with Deep Learning",
        summary="A deep learning project focused on classifying minerals using convolutional neural networks (CNNs). The project aims to develop a model capable of accurately distinguishing between different types of minerals based on images.",
        link="https://github.com/ChitiNkhuwa/Mineral_Identification"
    )
    show_project_card(
        title="Spent Lithium-ion Battery Recycling (SLIBR) Classification",
        summary="This project aims to classify spent lithium-ion batteries into cathode and anode mineral classes using Convolutional Neural Networks (CNNs) implemented in PyTorch. The classification model is trained on a dataset of images representing different types of spent lithium-ion batteries.",
        link="https://github.com/ChitiNkhuwa/Lithium_Recycling_Classification"
    )
    
    st.markdown("---")
    st.info("💡 **To see all projects:** Visit my [GitHub profile](https://github.com/ChitiNkhuwa)")

elif page == "Work Experience":
    st.title("Work Experience")
    
    st.markdown("---")
    st.markdown("### Machine Learning Engineer (Freelance)")
    st.markdown("**Duration:** January 2023 - Present")
    st.markdown("**2+ years' experience** *(Projects completed in personal time, not conflicting with full-time roles)*")
    st.markdown("""
    **Key Responsibilities:**
    - Built and deployed machine learning models for real-world use cases, including predictive analytics and optimization projects
    - Designed and maintained end-to-end data pipelines using Python, SQL, and cloud platforms
    - Applied deep learning frameworks (PyTorch, TensorFlow) to computer vision and NLP tasks
    - Delivered insights and model results to clients through dashboards, reports, and interactive visualizations
    """)
    
    st.markdown("---")
    st.markdown("### Staff Accountant")
    st.markdown("**Nevada Copper Mines | Yerington, Nevada**")
    st.markdown("**Duration:** April 2023 - August 2024")
    st.markdown("""
    **Key Responsibilities:**
    - Assisted with and analyzed cost reports, site-based financial statements and other financial information requests using Microsoft Dynamics 365
    - Managed fixed asset accounting (Prepaids, Depreciation, CIP, Month end)
    - Charged expenses to accounts, cost centers, and WBS elements by expertly analyzing invoices and expense reports
    - Ensured timely management of month-end accounts payable work-papers
    """)
    
    st.markdown("---")
    st.markdown("### Data Analyst")
    st.markdown("**Nevada Successful Solutions | Sparks, Nevada**")
    st.markdown("**Duration:** December 2022 - April 2023")
    st.markdown("""
    **Key Responsibilities:**
    - Analyzed credit worthiness of potential clients using regression models
    - Proposed solutions and strategies to tackle business problems by coordinating with relevant teams
    - Managed team interactions with clients and provided support in the business investment process
    - Maintained accounting books by monitoring income and expenses to ensure the company maintained liquidity requirements
    """)

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

# Footer
st.markdown("---")
st.markdown("© 2025 Chiti Nkhuwa. All rights reserved.")