
import streamlit as st
import pyttsx3

st.set_page_config(page_title="Career Task System", page_icon="🚀", layout="centered")

st.title(" Welcome to Career Task System")

# --- SESSION STATE VARIABLES ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "current_view" not in st.session_state:
    st.session_state.current_view = "home"  # "home", "login", "signup", "dashboard", "tict", "analytical"

if "show_suggestion" not in st.session_state:
    st.session_state.show_suggestion = False

# --- BUTTON HANDLERS ---
def show_login():
    st.session_state.current_view = "login"

def show_signup():
    st.session_state.current_view = "signup"

def go_to_tict():
    st.session_state.current_view = "tict"
   
def go_to_analytical():
    st.session_state.current_view = "analytical" 


def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)  # speaking speed
    engine.say(text)
    engine.runAndWait()

def MentorConnect():
    st.markdown("careerCue@gmail.com")
       

# --- HOMEPAGE (LOGIN / SIGN UP OPTIONS) ---
if not st.session_state.authenticated and st.session_state.current_view == "home":
    st.markdown("Choose an option below:")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.button("Login", use_container_width=True, on_click=show_login)
        st.button("Sign Up", use_container_width=True, on_click=show_signup)

# --- LOGIN FORM ---
if not st.session_state.authenticated and st.session_state.current_view == "login":
    st.markdown("###  Login")
    with st.form("login_form"):
        email = st.text_input("Gmail")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        if submitted:
            st.success(f"Logged in as {email}")
            st.session_state.authenticated = True
            st.session_state.current_view = "dashboard"

# --- SIGNUP FORM ---
if not st.session_state.authenticated and st.session_state.current_view == "signup":
    st.markdown("###  Sign Up")
    with st.form("signup_form"):
        name = st.text_input("Name",placeholder="enter your name here")
        mobile = st.text_input("Mobile Number",placeholder="enter mobile number exactly ten digits")
        email = st.text_input("Gmail",placeholder="enter your gmail id")
        password = st.text_input("Password", type="password",placeholder="enter your password")
        confirm_password = st.text_input("Confirm Password", type="password",placeholder="enter your password again for confirming it")
        submitted = st.form_submit_button("Create Account")
        if submitted:
                        if not name or not mobile or not email or not password or not confirm_password:
                            st.error("❗ All fields are required. Please fill in every detail.")
                        elif not mobile.isdigit() or len(mobile) != 10:
                            st.error("📵 Mobile number must be exactly 10 digits.")
                        elif password != confirm_password:
                            st.error("❌ Passwords do not match.")
                        else :

# --- DASHBOARD ---
                            if st.session_state.authenticated and st.session_state.current_view == "dashboard":
    st.markdown("---")
    st.markdown("### *“Discover yourself through the tasks you enjoy.”*")
    st.markdown("### You're ready to begin your journey!")

    if st.button(" Start Doing Tasks", use_container_width=True):
        st.success("Opening your first creativity task...")
        go_to_tict()

# --- TICT CREATIVE TEST SECTION ---
if st.session_state.current_view == "tict":
    st.markdown("##  TICT – Creativity Assessment")

    # st.markdown("###  Task 1: Unusual Uses")
    # st.write("List **3 unusual uses** for a paperclip. Be imaginative!")
    # paperclip_uses = st.text_area("Your Response")

    st.markdown("###  Task 1: Unusual Uses")
    task1_text = "List 3 unusual uses for a paperclip. Be imaginative!"
    st.write(task1_text)
    if st.button("🔊"):
        speak_text(task1_text)
        paperclip_uses = st.text_area("Your Response")



    st.markdown("###  Task 2: Finish the Story")
    task2_text ="You wake up one day and realize you can see people's thoughts as colors...\""
    st.write(task2_text)
    if st.button("🔊 "):
        speak_text(task2_text)
        paperclip_uses = st.text_area("Write what happens next...")


    st.markdown("###  Task 3: Design Thinking")
    task2_text = (" People often waste food at parties. Design a system or idea to reduce food waste.")
    st.write(task2_text)
    if st.button("🔊  "):
        speak_text(task2_text)
        paperclip_uses = st.text_area("Describe your creative solution:")


    if st.button(" Submit Your Creativity Tasks"):
        st.success(" Thank you! Your responses have been recorded for analysis.")
        st.balloons()
        go_to_analytical()

# --- ANALYTICAL TASKS SECTION ---
if st.session_state.current_view == "analytical":
    st.markdown("##  Analytical Thinking Test")
    st.markdown("Let's test your logic, patterns, and problem-solving!")

    st.markdown("###  Task 1: Short Problem-Solving Challenge")
    task3_text ="""
There are **3 switches** downstairs. Only one controls a **bulb upstairs**.  
You can go upstairs **only once**.  
**How will you find out which switch controls the bulb?**
"""
    st.write(task3_text)
    if st.button("🔊   "):
        speak_text(task3_text)
    paperclip_uses = st.text_area(" Your strategy:", key="analytical1",placeholder="enter your strategy")
else:
    if not paperclip_uses:
             st.error("❗ Please fill in this detail.")
            

    st.markdown("###  Task 2: Pattern Recognition")
    task4_text ="What comes next in the sequence? 2, 4, 8, 16, ?"
    st.write(task4_text)
    if st.button("🔊    "):
        #speak_text(task4_text)
    pattern_choice = st.radio("Choose one:", ["18", "20", "24", "32"], key="analytical2")
   
    st.markdown("###  Task 3: Logic Trap")
    task5_text = ("""
A bat and a ball cost ₹110 in total.  
The bat costs ₹100 more than the ball.  
**How much does the ball cost?**
""")
    st.write(task5_text)
    if st.button("🔊     "):
        speak_text(task5_text)
    ball_choice = st.radio("Your answer:", ["₹5", "₹10", "₹15", "₹20"], key="analytical3")

    if st.button(" Submit Analytical Tasks"):
        st.success("Thanks for completing the tasks!")
        st.session_state.show_suggestion = True

        st.markdown("---")
        st.markdown("###  Correct Explanations:")

        with st.expander(" Task 1: Switch & Bulb Solution"):
            st.info("""
1. Turn ON switch 1 for 5 minutes, then turn it OFF.  
2. Turn ON switch 2.  
3. Leave switch 3 OFF.  
Go upstairs:
- If bulb is ON → switch 2  
- If bulb is OFF but warm → switch 1  
- If bulb is OFF and cold → switch 3
""")

        with st.expander(" Task 2: Pattern"):
            st.markdown("**Correct Answer:** `32`")
            st.caption("It’s doubling each time: 2 → 4 → 8 → 16 → 32")

        with st.expander(" Task 3: Bat & Ball"):
            st.markdown("**Correct Answer:** ₹5")
            st.caption("If ball is ₹5, bat is ₹105 (₹100 more), total ₹110.")

# --- SELF EVALUATION + CAREER SUGGESTION ---
if st.session_state.get("show_suggestion", False):

    st.markdown("---")
    st.markdown("##  Self Evaluation")
    st.markdown("###  Rate your performance (honestly):")

    creativity_score = st.slider(" How creative were your TICT responses?", 0, 10, 5)

    # Safely get multiple choice answers
    pattern_choice = st.session_state.get("analytical2", "")
    ball_choice = st.session_state.get("analytical3", "")
    analytical_score = 0

    if pattern_choice == "32":
        analytical_score += 1
    if ball_choice == "₹5":
        analytical_score += 1

    analytical_self = st.slider(" How confident are you in your switch-bulb solution?", 0, 2, 1)
    analytical_score += analytical_self

    if st.button(" Get Career Suggestion"):
        st.markdown("---")
        st.markdown("### 💼 Career Suggestion Based on Your Results:")

        if creativity_score >= 7 and analytical_score >= 3:
            st.success(" You are a **Creative & Logical Thinker**.\n**Suggested Careers**: Product Designer, Research Scientist, Entrepreneur")
        elif creativity_score >= 7 and analytical_score < 3:
            st.success(" You are a **Creative Mind**.\n**Suggested Careers**: Writer, Artist, Creative Director, Content Strategist")
        elif creativity_score < 5 and analytical_score >= 3:
            st.success(" You are an **Analytical Problem Solver**.\n**Suggested Careers**: Data Analyst, Engineer, Doctor, Software Developer")
        else:
            st.success(" You have **Balanced Skills**.\n**Suggested Careers**: Psychologist, UX Designer, Teacher, Social Worker")
                        
st.markdown("<br><br><br><br><br><br><br><br><br><br><br><br><br><br>", unsafe_allow_html=True)
connect_col = st.empty()
with connect_col:
    if st.button(" ***Connect us***"):
        MentorConnect()
            