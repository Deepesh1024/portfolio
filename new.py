import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Deepesh Jha - Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced dark styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
        
        * {
            font-family: 'Poppins', sans-serif !important;
        }
        
        .main {
            background: linear-gradient(135deg, #1f1f1f 0%, #333333 100%);
            padding: 2rem;
            color: #e0e0e0;
        }
        
        .stButton button {
            width: 100%;
            border-radius: 20px;
            background: linear-gradient(45deg, #64b5f6, #1e88e5);
            border: none;
            color: white;
            font-weight: 500;
            transition: transform 0.3s ease;
        }
        
        .stButton button:hover {
            transform: translateY(-2px);
        }
        
        .css-1d391kg {
            padding: 3rem 1rem;
        }
        
        .block-container {
            padding-top: 1rem;
        }
        
        .profile-content {
            background: #424242;
            padding: 2rem;
            border-radius: 20px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            margin-bottom: 2rem;
            color: #e0e0e0;
        }
        
        .social-icons {
            font-size: 24px;
            margin: 0 10px;
            color: #bbdefb;
            text-decoration: none;
        }
        
        .skill-tag {
            background: #1e88e5;
            padding: 5px 15px;
            border-radius: 15px;
            display: inline-block;
            margin: 5px;
            color: white;
            font-size: 0.9rem;
        }
        
        .gradient-text {
            background: linear-gradient(45deg, #64b5f6, #1e88e5);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-size: 2.5rem !important;
            font-weight: 700 !important;
        }
        
        .card {
            background: #424242;
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 1rem;
            border-left: 4px solid #64b5f6;
            color: #e0e0e0;
        }
        
        .hero-section {
            background: linear-gradient(135deg, #1e88e5 0%, #1565c0 100%);
            color: white;
            padding: 3rem;
            border-radius: 20px;
            margin-bottom: 2rem;
        }
        
        .stat-box {
            background: rgba(255, 255, 255, 0.1);
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
            backdrop-filter: blur(10px);
            color: #e0e0e0;
        }
        
        .progress-bar {
            height: 10px;
            background: #333333;
            border-radius: 5px;
            margin-top: 5px;
        }
        
        .progress-fill {
            height: 100%;
            background: linear-gradient(45deg, #64b5f6, #1e88e5);
            border-radius: 5px;
            transition: width 0.5s ease;
        }
        
        /* Dark theme specific adjustments */
        .stTextInput input {
            background-color: #333333;
            color: #e0e0e0;
            border: 1px solid #555555;
        }
        
        .stTextArea textarea {
            background-color: #333333;
            color: #e0e0e0;
            border: 1px solid #555555;
        }
        
        .stMarkdown {
            color: #e0e0e0;
        }
        
        .css-1544g2n.e1fqkh3o4 {
            background-color: #333333;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("WhatsApp Image 2024-08-25 at 10.56.44.jpeg", width=150)
    st.markdown("<h2 style='text-align: center; color: #bbdefb;'>Deepesh Jha</h2>", unsafe_allow_html=True)
    selected = st.radio(
        "",
        ["Home", "About", "Skills", "Education", "Contact"],
        index=0
    )
    
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center;'>
            <h4 style='color: #bbdefb;'>Connect with me</h4>
            <a href='https://github.com/Deepesh1024' target='_blank'>
                <button style='margin: 5px; padding: 5px 15px; border-radius: 15px; border: none; background: #1e88e5; color: white;'>
                    GitHub
                </button>
            </a>
            <a href='https://linkedin.com/in/deepesh-jha/' target='_blank'>
                <button style='margin: 5px; padding: 5px 15px; border-radius: 15px; border: none; background: #1e88e5; color: white;'>
                    LinkedIn
                </button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

# Home
if selected == "Home":
    st.markdown(
        """
        <div class='hero-section'>
            <h1 style='font-size: 3rem; margin-bottom: 1rem;'>Hi, I'm Deepesh Jha 👋</h1>
            <h3 style='margin-bottom: 2rem;'>AI & MLOps Engineer | CSE '27</h3>
            <div style='display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem;'>
                <div class='stat-box'>
                    <h4>Tech Lead</h4>
                    <p>Microsoft Azure Developers Club</p>
                </div>
                <div class='stat-box'>
                    <h4>Research</h4>
                    <p>ARTPARK | IISC</p>
                </div>
                <div class='stat-box'>
                    <h4>Specialization</h4>
                    <p>Machine Learning & MLOps</p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            """
            <div class='card'>
                <h3 style='color: #bbdefb;'>What I Do</h3>
                <p>🤖 Develop AI Solutions</p>
                <p>☁️ Implement MLOps Practices</p>
                <p>🔄 Create Deployment Pipelines</p>
                <p>📊 Data Analysis & Visualization</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            """
            <div class='card'>
                <h3 style='color: #bbdefb;'>Current Focus</h3>
                <p>📚 Deep Learning Research</p>
                <p>🌐 Cloud Architecture</p>
                <p>🔨 DevOps Integration</p>
                <p>📈 Scalable AI Systems</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# About
elif selected == "About":
    st.markdown("<div class='profile-content'>", unsafe_allow_html=True)
    st.markdown("<h1 class='gradient-text'>About Me</h1>", unsafe_allow_html=True)
    st.write("""
    I am an Artificial Intelligence Developer passionate about pushing the boundaries of what's possible with AI. 
    With expertise in deep learning and advanced AI techniques, I focus on creating scalable and efficient solutions.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            """
            <div class='card'>
                <h3 style='color: #bbdefb;'>Experience</h3>
                <ul style='color: #e0e0e0;'>
                    <li>AIML Tech Lead at Microsoft Azure Developers Club</li>
                    <li>Research Assistant at ARTPARK | IISC</li>
                    <li>Google Developers Student Club Member</li>
                    <li>IEEE Computer Society Member</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            """
            <div class='card'>
                <h3 style='color: #bbdefb;'>Interests</h3>
                <ul style='color: #e0e0e0;'>
                    <li>Artificial Intelligence & Deep Learning</li>
                    <li>Cloud Computing & DevOps</li>
                    <li>Software Architecture</li>
                    <li>Open Source Development</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

# Skills
elif selected == "Skills":
    st.markdown("<div class='profile-content'>", unsafe_allow_html=True)
    st.markdown("<h1 class='gradient-text'>Skills & Expertise</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("<h3 style='color: #bbdefb;'>Technical Skills</h3>", unsafe_allow_html=True)
        skills = {
            "Python": 90,
            "Machine Learning": 85,
            "Deep Learning": 80,
            "MLOps": 75,
            "Cloud Computing": 85,
            "DevOps": 70
        }
        
        for skill, proficiency in skills.items():
            st.markdown(f"""
                <div style='margin-bottom: 1rem;'>
                    <div style='display: flex; justify-content: space-between; color: #e0e0e0;'>
                        <span>{skill}</span>
                        <span>{proficiency}%</span>
                    </div>
                    <div class='progress-bar'>
                        <div class='progress-fill' style='width: {proficiency}%;'></div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("<h3 style='color: #bbdefb;'>Tools & Frameworks</h3>", unsafe_allow_html=True)
        tools = [
            "TensorFlow", "PyTorch", "Docker",
            "Kubernetes", "AWS", "Azure",
            "Git", "Flask", "Streamlit"
        ]
        
        st.markdown(
            "<div style='display: flex; flex-wrap: wrap;'>" +
            "".join([f"<span class='skill-tag'>{tool}</span>" for tool in tools]) +
            "</div>",
            unsafe_allow_html=True
        )

# Education
elif selected == "Education":
    st.markdown("<div class='profile-content'>", unsafe_allow_html=True)
    st.markdown("<h1 class='gradient-text'>Education</h1>", unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class='card'>
            <h2 style='color: #bbdefb;'>Alliance University</h2>
            <p style='color: #9e9e9e;'>Bachelor of Technology - BTech, Computer Science</p>
            <p style='color: #9e9e9e;'>2023 - 2027</p>
            <br>
            <h4 style='color: #bbdefb;'>Key Activities</h4>
            <ul style='color: #e0e0e0;'>
                <li>AIML Tech Lead at Microsoft Azure Developers Club</li>
                <li>Active member of Google Developers Student Club</li>
                <li>IEEE Computer Society member</li>
                <li>Research focus on AI and Deep Learning</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

# Contact
elif selected == "Contact":
    st.markdown("<div class='profile-content'>", unsafe_allow_html=True)
    st.markdown("<h1 class='gradient-text'>Get In Touch</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            """
            <div class='card'>
                <h3 style='color: #bbdefb;'>Contact Information</h3>
                <p>📧 Email: d4deepeshpro@gmail.com</p>
                <p>📍 Location: Bengaluru, Karnataka, India</p>
                <p>💼 Open to collaborations and opportunities</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
    with col2:
        st.markdown("""<div class='card'><h3 style='color: #bbdefb;'>Send a Message</h3></div>""", unsafe_allow_html=True)
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        if st.button("Send Message"):
            st.success("Thanks for reaching out! I'll get back to you soon.")

# Footer
st.markdown(
    """
    <div style='text-align: center; margin-top: 2rem; padding: 1rem; background: #333333; border-radius: 10px; color: #e0e0e0;'>
        <p>© 2024 Deepesh Jha. All rights reserved.</p>
    </div>
    """,
    unsafe_allow_html=True
)