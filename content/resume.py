import streamlit as st

def load_resume_latex():

    # PAGE CONFIG
    st.set_page_config(layout="wide")

    # GLOBAL STYLE
    st.markdown("""
        <style>
            body {
                font-size: 14px;
            }
            .section-title {
                font-size: 18px;
                font-weight: bold;
                border-bottom: 1px solid #aaa;
                margin-top: 20px;
                margin-bottom: 10px;
            }
            .item-title {
                font-weight: bold;
            }
            .sub-item {
                margin-left: 10px;
            }
            .contact a {
                text-decoration: none;
            }
        </style>
    """, unsafe_allow_html=True)

    # HEADER
    st.markdown("""
    <div align="center" class="contact">
        <h2><a href="https://www.linkedin.com/in/jithendra-siddartha/">Jithendra Sri SivaKesava Siddartha Puppala</a></h2>
        <p><a href="tel:+91 9666802496">+91 9666802496</a> | <a href="mailto:jithendra.mail.me@gmail.com">jithendra.mail.me@gmail.com</a></p>
        <p>Graduate Student – M.S. in Computer Science, New York University (Expected May 2027), New York, NY</p>
    </div>
    """, unsafe_allow_html=True)

    # SUMMARY
    st.markdown('<div class="section-title">Summary</div>', unsafe_allow_html=True)
    st.markdown(
        "Aspiring Data Scientist with 2+ years of industry experience in building and deploying machine learning models. Passionate about solving real-world problems through time-series modeling, semi-supervised learning, and scalable ML APIs.")

    # EDUCATION
    st.markdown('<div class="section-title">Education</div>', unsafe_allow_html=True)
    st.markdown("""
    - **[New York University](https://www.nyu.edu/)** – M.S. in Computer Science _(Aug 2025 – May 2027)_, New York, NY
    - **[National Institute of Technology Karnataka (NIT Surathkal)](https://www.nitk.ac.in/)** – B.Tech in Computer Science Engineering _(July 2019 – May 2023)_, Surathkal, Mangaluru
    """)

    # SKILLS
    st.markdown('<div class="section-title">Skills</div>', unsafe_allow_html=True)
    st.markdown("""
    - **Programming & Data Processing**: Python, SQL, Pandas, NumPy, Time-series Analysis, C  
    - **Machine Learning & Tools**: Scikit-learn, TensorFlow, Computer Vision, ARIMA, Deep Learning  
    - **Data Visualization & Deployment**: Django, Matplotlib, Seaborn, REST API, Jupyter, Docker, Git, VIM, Anaconda  
    - **Workflow & Platforms**: Google Workspace, Notion, Trello, Linux, GitHub, Cloud (AWS, GCP), HuggingFace
    """)

    # EXPERIENCE
    st.markdown('<div class="section-title">Experience</div>', unsafe_allow_html=True)

    st.markdown(
        "**[Jio Platforms Limited](https://www.jio.com/platforms/)** – Data Scientist _(June 2023 – July 2025)_, Bengaluru, India")
    st.markdown("""
    - Built and deployed machine learning models for cattle heat and health detection using time-series and ensemble techniques, improving **precision by 11%** and **recall by 14%**.  
    - Contributed to a **4x YoY revenue growth** (~₹2 Crore) by integrating models into production on IoT-based monitoring devices.  
    - Developed Flask-based REST APIs to serve real-time predictions on production.  
    - Engineered ARIMA residual-based time-series features.  
    - Optimized cattle activity detection pipeline, achieving **20x** speedup and accuracy improvement from 89% to 93%.  
    - Built dashboards with analytics/frontend teams, enabling **10x** faster field decisions.
    """)

    st.markdown(
        "**[Accenture](https://www.accenture.com/in-en)** – Advanced App Engineering Analyst (Intern) _(June 2022 – July 2022)_, Bengaluru, India")
    st.markdown("""
    - Researched observability practices to improve system performance monitoring.  
    - Presented findings to 25+ engineers with best practices and insights.
    """)

    # PROJECTS
    st.markdown('<div class="section-title">Projects</div>', unsafe_allow_html=True)

    st.markdown("**MixMatch on Custom Dataset** _(Mar 2022 – Apr 2022)_")
    st.markdown("- Implemented semi-supervised learning technique MixMatch on a custom dataset.")

    st.markdown(
        "**[Generic Library Management System (Django)](https://github.com/jithendra1798/SE-Project)** _(Aug 2021 – Dec 2021)_")
    st.markdown(
        "- Built Django-based web app with book search, issue tracking, user auth, and admin dashboard using SQLite and Bootstrap.")

    # LEADERSHIP
    st.markdown('<div class="section-title">Leadership & Achievements</div>', unsafe_allow_html=True)
    st.markdown("""
    - **[Finalist – Harvard Crossroads Emerging Leaders Program (CELP)](https://drive.google.com/file/d/1X08Syl_F5H8oMfZ5oDMyTn66X5TJBcQi/view?usp=sharing)** – 2021  
      Selected in top **114 of 10,000+** global applicants.  
    - JEE Mains Rank: **2683**, Advanced Rank: **6111** (Top 1% among 1.15M)  
    - **[Campus Director – Millennium Fellowship (UNAI & MCN)](https://drive.google.com/file/d/1BPhY9ftuJTWheoCDw8I7wM8muYZtdkRx/view)**  
      Led 15+ fellows in SDG projects; organized workshops and campaigns.  
    - **[Webinar Host – Competitiveness Mindset Institute](https://drive.google.com/file/d/1i-bYQ44CWYS5dZLpjUhjJIdBYyOA0dua/view?usp=sharing)**  
      Conducted webinars across 3 NIT campuses (NITK, NIT Surat, NIT Rourkela).  
    - **[Cadet – National Cadet Corps (NCC)](https://www.nitk.ac.in/ncc)**  
      Completed leadership and civic training with campus and community collaboration.
    """)

    # INTERESTS
    st.markdown('<div class="section-title">Interests</div>', unsafe_allow_html=True)
    st.markdown("Reading about ethical AI, tech-enabled social change, and mentoring student developers.")

def load_resume_pdf():
    import streamlit as st

    # st.set_page_config(page_title="Jithendra Puppala's Resume", layout="centered")
    # st.title("📄 Jithendra Puppala's Resume")

    # PDF hosted on GitHub Pages
    PDF_URL = "https://jithendra1798.github.io/Jithendra_Resume/resume.pdf"

    # Google Docs Viewer to force render
    viewer_url = f"https://docs.google.com/gview?url={PDF_URL}&embedded=true"

    # Embed the viewer iframe
    st.components.v1.html(
        f'<iframe src="{viewer_url}" width="100%" height="1000" style="border: none;"></iframe>',
        height=1050,
    )

    # Optional download button
    st.markdown(f"[📥 Download Resume (PDF)]({PDF_URL})", unsafe_allow_html=True)