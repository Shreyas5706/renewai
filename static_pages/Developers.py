import streamlit as st



import os


def safe_image(image_path, width=150):
    """
    Displays image if found, otherwise shows Default.jpg
    """
    try:
        if os.path.exists(image_path):
            st.image(image_path, width=width)
        else:
            st.image("assets/developers/Default.jpg", width=width)
    except Exception:
        st.image("assets/developers/Default.jpg", width=width)

def show():
        
    # --------------------------------------------------
    # PAGE HEADER
    # --------------------------------------------------
    st.markdown("""
    <div style="
    padding:25px;
    border-radius:16px;
    background:linear-gradient(90deg,#141e30,#243b55);
    ">
        <h1 style="color:white;margin-bottom:5px;">👨‍💻 Developers</h1>
        <h4 style="color:#cfe9ff;margin-top:0;">
            The team behind RenewAI
        </h4>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    RenewAI is developed by a collaborative team working at the intersection of  
    **Artificial Intelligence, Renewable Energy, and Sustainability Analytics**.
    """)

    st.markdown("---")

    # --------------------------------------------------
    # TEAM LEADER
    # --------------------------------------------------
    st.markdown("## 👑 Team Leader")

    col1, col2 = st.columns([1, 3])

    with col1:
        safe_image("assets/developers/Srushti.jpg", width=180)

    with col2:
        st.markdown("""
        ### Vekariya Srushti  
        **Team Lead | Project Coordination & Presentation Lead**

        Coordinates the overall project execution, manages task distribution among team members,
        and is responsible for preparing project presentations (PPTs) and documentation.
        Ensures clarity of objectives, timely progress, and alignment with project goals.
        """)

        link_col1, link_col2 = st.columns(2)

        with link_col1:
            st.markdown(
                
                "[🔗 LinkedIn](https://www.linkedin.com/in/srushti-vekariya-a6563a2b7/)",
                unsafe_allow_html=True
            )

        with link_col2:
            st.markdown("[🐙 GitHub](https://github.com/SRUSHTI0401)  ")

    st.markdown("---")

    # --------------------------------------------------
    # TEAM MEMBERS
    # --------------------------------------------------
    st.markdown("## 👥 Team Members")

    c1, c2 = st.columns(2)

    with c1:
        safe_image("assets/developers/Shreyas.jpeg", width=150)
        st.markdown("""
        **Solanki Shreyas – Frontend Developer | Dashboard & UI Engineering**

        Responsible for designing and implementing the interactive frontend using Streamlit.
        Developed the dashboard layout, sidebar navigation, animations, and user experience flow
        across all modules of RenewAI.
        """)

        st.markdown(
            "[🐙 GitHub](https://github.com/Shreyas5706)  |  "
            "[🔗 LinkedIn](https://www.linkedin.com/in/shreyas-solanki-1b6458285)",
            unsafe_allow_html=True
        )

    with c2:
        safe_image("assets/developers/Disha.jpg", width=150)
        st.markdown("""
        **Thanki Disha – Machine Learning Developer | Data Modeling & Implementation**

        Works on building and training machine learning models using renewable energy datasets.
        Handles data preprocessing, feature selection, and model validation
        """)

        st.markdown(
            "[🐙 GitHub](https://github.com/dishathanki)  |  "
            "[🔗 LinkedIn](https://www.linkedin.com/in/disha-thanki-b18ab7259/)",
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    c3, c4 = st.columns(2)

    with c3:
        safe_image("assets/developers/Om.jpeg", width=150)
        st.markdown("""
        **Bhinsara Om – Machine Learning Developer | Model Implementation**

        Focuses on implementing predictive models for energy forecasting and plant performance.
        Contributes to experimentation, tuning, and evaluation of ML models.
        """)

        st.markdown(
            "[🐙 GitHub](https://github.com/om-bhinsara)  |  "
            "[🔗 LinkedIn](https://www.linkedin.com/in/om-j-bhisra/)",
            unsafe_allow_html=True
        )

    with c4:
        safe_image("assets/developers/Shaiv.jpeg", width=150)
        st.markdown("""
        **Patel Shaiv – Machine Learning Developer | Testing & Analysis**

        Assists in testing machine learning models, validating outputs,
        and ensuring consistency and reliability of analytical results.
        """)

        st.markdown(
            "[🐙 GitHub](https://github.com/Shaiv05)  |  "
            "[🔗 LinkedIn](www.linkedin.com/in/shaivpatel05)",
            unsafe_allow_html=True
        )

    st.markdown("---")

    # --------------------------------------------------
    # FOOTER
    # --------------------------------------------------
    st.caption(
        "📬 Click on the icons to visit developer profiles. "
    )
