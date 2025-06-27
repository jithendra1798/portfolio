import streamlit as st
from pathlib import Path

# --- CONFIGURATION ---
st.set_page_config(
    page_title="Jithendra Puppala | Portfolio",
    layout="wide",
    page_icon="📊"
)

# --- SIDEBAR CONTACT CARD ---
st.sidebar.image("assets/profile.jpg", width=150)
st.sidebar.markdown("### Jithendra Puppala")
st.sidebar.write("Data Scientist | MS CS @ NYU Tandon")

st.sidebar.markdown("""
<style>
a.sidebar-link {
    text-decoration: none;
    font-size: 15px;
    display: block;
    margin: 8px 0;
}
a.sidebar-link:hover {
    color: #4c8bf5;
}
</style>
<a href="#about-me" class="sidebar-link">📌 About Me</a>
<a href="#skills" class="sidebar-link">🛠 Skills</a>
<a href="#projects" class="sidebar-link">📂 Projects</a>
<a href="#contact" class="sidebar-link">📬 Contact</a>
""", unsafe_allow_html=True)


st.sidebar.markdown("[📄 Resume](resume/Jithendra_Resume.pdf)", unsafe_allow_html=True)
st.sidebar.markdown("[📧 Email](mailto:jithendra.mail.me@gmail.com)")
st.sidebar.markdown("[💼 LinkedIn](https://linkedin.com/in/jithendra-siddartha)")
st.sidebar.markdown("[💻 GitHub](https://github.com/jithendra1798)")

# --- LOADER FOR PAGES ---
def load_about_me():
    about_path = Path("content/about_me.md")
    if about_path.exists():
        st.markdown(about_path.read_text(), unsafe_allow_html=True)
    else:
        st.warning("About Me content not found.")

def load_resume():
    resume_path = Path("resume/Jithendra_Resume.pdf")
    if resume_path.exists():
        st.download_button(
            label="📄 Download My Resume",
            data=resume_path.read_bytes(),
            file_name="Jithendra_Resume.pdf",
            mime="application/pdf"
        )
        st.info("You can also find my resume on LinkedIn or GitHub.")
    else:
        from content.resume import load_resume_latex, load_resume_pdf
        # load_resume_latex()
        load_resume_pdf()
        # st.warning("Resume file not found.")

def load_contact():
    # st.subheader("📬 Contact Me")
    st.write("Feel free to reach out via email or connect with me on LinkedIn.")
    st.markdown("- 📧 Email: [jithendra.mail.me@gmail.com](mailto:jithendra.mail.me@gmail.com)")
    st.markdown("- 🔗 LinkedIn: [linkedin.com/in/jithendra-siddartha](https://www.linkedin.com/in/jithendra-siddartha)")
    st.markdown("- 💻 GitHub: [github.com/jithendra1798](https://github.com/jithendra1798)")


# --- MAIN PAGE CONTENT ---

# About Me
st.markdown("<h2 id='about-me'>📌 About Me</h2>", unsafe_allow_html=True)
load_about_me()
# about_path = Path("content/about_me.md")
# if about_path.exists():
#     st.markdown(about_path.read_text(), unsafe_allow_html=True)
# else:
#     st.warning("About Me content not found.")

# Skills
st.markdown("<h2 id='skills'>🛠 Skills</h2>", unsafe_allow_html=True)
st.markdown("""
**Programming & Data:** Python, SQL, Pandas, NumPy, Time-series Analysis, C  
**Machine Learning:** Scikit-learn, TensorFlow, XGBoost, Semi-Supervised Learning, ARIMA  
**Tools & Deployment:** Flask, REST APIs, Git, Jupyter, Docker, Anaconda  
**Visualization:** Matplotlib, Seaborn, Dash, Power BI  
**Workflow & Platforms:** Google Workspace, Notion, Trello, Linux, GitHub  
**Soft Skills:** Communication, Time Management, Collaboration, Peer Mentoring
""")

# Projects
st.markdown("<h2 id='projects'>📂 Projects</h2>", unsafe_allow_html=True)
st.markdown("Below are brief overviews of selected projects. Click to view details.")

with st.expander("🔬 Semi-Supervised Learning with MixMatch"):
    st.markdown("""
**Tools:** PyTorch, Matplotlib, Scikit-learn  
Implemented MixMatch algorithm on a custom dataset to demonstrate semi-supervised learning. Achieved improved classification performance with only 20% labeled data. [GitHub](https://github.com/jithendra1798)  
""")

with st.expander("📈 Time-Series Cattle Heat Detection"):
    st.markdown("""
**Tools:** Python, ARIMA, Flask, REST API  
Built and deployed a time-series based cattle heat detection model that increased precision by 11% and recall by 14%, contributing to a 4x revenue growth in production systems.  
""")

with st.expander("📚 Library Management System (Django)"):
    st.markdown("""
**Tools:** Django, SQLite, Bootstrap  
Developed a web-based portal for library book management with role-based access and admin dashboard features.  
""")

# Resume
st.markdown("<h2 id='resume'>📄 Resume</h2>", unsafe_allow_html=True)
resume_path = Path("resume/Jithendra_Resume.pdf")
if resume_path.exists():
    st.download_button(
        label="Download My Resume",
        data=resume_path.read_bytes(),
        file_name="Jithendra_Resume.pdf",
        mime="application/pdf"
    )
else:
    st.warning("Resume file not found.")
# load_resume()


# Contact Info
st.markdown("<h2 id='contact'>📬 Contact Me</h2>", unsafe_allow_html=True)
# st.markdown("""
# - 📧 Email: [jithendra.mail.me@gmail.com](mailto:jithendra.mail.me@gmail.com)
# - 🔗 LinkedIn: [linkedin.com/in/jithendra-siddartha](https://www.linkedin.com/in/jithendra-siddartha)
# - 💻 GitHub: [github.com/jithendra1798](https://github.com/jithendra1798)
# """)
load_contact()
# import streamlit as st
# from pathlib import Path
#
# # --- CONFIGURATION ---
# st.set_page_config(
#     page_title="Jithendra Puppala | Portfolio",
#     layout="wide",
#     page_icon="📊"
# )
#
# # --- SIDEBAR NAVIGATION ---
# st.sidebar.image("assets/profile.jpg", width=150)
# st.sidebar.markdown("### Jithendra Puppala")
# st.sidebar.write("Data Scientist | MS CS @ NYU Tandon")
# st.sidebar.markdown("[📄 Resume](resume/Jithendra_Resume.pdf)", unsafe_allow_html=True)
# st.sidebar.markdown("[📧 Email](mailto:jithendra.mail.me@gmail.com)")
# st.sidebar.markdown("[💼 LinkedIn](https://linkedin.com/in/jithendra-siddartha)")
# st.sidebar.markdown("[💻 GitHub](https://github.com/jithendra1798)")
#
# # --- LOADER FOR PAGES ---
# def load_about_me():
#     about_path = Path("content/about_me.md")
#     if about_path.exists():
#         st.markdown(about_path.read_text(), unsafe_allow_html=True)
#     else:
#         st.warning("About Me content not found.")
#
# def load_resume():
#     resume_path = Path("resume/Jithendra_Resume.pdf")
#     if resume_path.exists():
#         st.download_button(
#             label="📄 Download My Resume",
#             data=resume_path.read_bytes(),
#             file_name="Jithendra_Resume.pdf",
#             mime="application/pdf"
#         )
#         st.info("You can also find my resume on LinkedIn or GitHub.")
#     else:
#         from content.resume import load_resume_latex, load_resume_pdf
#         # load_resume_latex()
#         load_resume_pdf()
#         # st.warning("Resume file not found.")
#
# def load_contact():
#     st.subheader("📬 Contact Me")
#     st.write("Feel free to reach out via email or connect with me on LinkedIn.")
#     st.markdown("- 📧 Email: [jithendra.mail.me@gmail.com](mailto:jithendra.mail.me@gmail.com)")
#     st.markdown("- 🔗 LinkedIn: [linkedin.com/in/jithendra-siddartha](https://www.linkedin.com/in/jithendra-siddartha)")
#     st.markdown("- 💻 GitHub: [github.com/jithendra1798](https://github.com/jithendra1798)")
#
#
# # --- ROUTING ---
# if page == "About Me":
#     load_about_me()
#
# elif page == "Projects":
#     st.header("Projects")
#     st.info("Project section under development.")
#
# elif page == "Resume":
#     # st.header("Resume")
#     from content.resume import load_resume_latex, load_resume_pdf
#     load_resume_pdf()
#
# elif page == "Contact":
#     st.header("Contact")
#     load_contact()
