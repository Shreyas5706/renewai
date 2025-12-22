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
        **Team Lead | Project Coordination & System Design**

        Leads overall project planning, coordination, and system integration.
        Ensures alignment of analytics with sustainability objectives.
        """)

        link_col1, link_col2 = st.columns(2)

        with link_col1:
            st.markdown(
                "[🔗 LinkedIn](https://www.linkedin.com/in/srushti-vekariya-a6563a2b7/)",
                unsafe_allow_html=True
            )

        with link_col2:
            st.markdown("🐙 GitHub: _To be added_")

    st.markdown("---")

    # --------------------------------------------------
    # TEAM MEMBERS
    # --------------------------------------------------
    st.markdown("## 👥 Team Members")

    c1, c2 = st.columns(2)

    with c1:
        safe_image("assets/developers/Shreyas.jpeg", width=150)
        st.markdown("""
        **Solanki Shreyas – AI & Data Analytics**

        Works on machine learning models, data preprocessing,
        and predictive analytics integration.
        """)

        st.markdown(
            "[🐙 GitHub](https://github.com/Shreyas5706)  |  "
            "[🔗 LinkedIn](https://www.linkedin.com/in/shreyas-solanki-1b6458285)",
            unsafe_allow_html=True
        )

    with c2:
        safe_image("assets/developers/Disha.jpg", width=150)
        st.markdown("""
        **Thanki Disha – Data Handling & Analysis**

        Contributes to dataset preparation, validation,
        and analytical interpretation.
        """)

        st.markdown(
            "🐙 GitHub: _To be added_  |  "
            "[🔗 LinkedIn](https://www.linkedin.com/in/disha-thanki-b18ab7259/)",
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    c3, c4 = st.columns(2)

    with c3:
        safe_image("assets/developers/Om.jpg", width=150)
        st.markdown("""
        **Bhinsara Om – Research & Sustainability Analysis**

        Focuses on CO₂ reduction logic and renewable feasibility analysis.
        """)

        st.markdown(
            "🐙 GitHub: _To be added_  |  "
            "[🔗 LinkedIn](https://www.linkedin.com/in/om-j-bhisra/)",
            unsafe_allow_html=True
        )

    with c4:
        safe_image("assets/developers/Shaiv.jpg", width=150)
        st.markdown("""
        **Patel Shaiv – Testing & Documentation**

        Responsible for testing workflows and system documentation.
        """)

        st.markdown(
            "🐙 GitHub: _To be added_  |  "
            "🔗 LinkedIn: _To be added_"
        )

    st.markdown("---")

    # --------------------------------------------------
    # FOOTER
    # --------------------------------------------------
    st.caption(
        "📬 Click on the icons to visit developer profiles. "
        "More links can be added as the project evolves."
    )
