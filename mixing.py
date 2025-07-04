import streamlit as st
import os
import pyttsx3
import speech_recognition as sr
import pandas as pd
from sklearn.linear_model import LinearRegression
import paramiko
from streamlit.components.v1 import html

# 🎨 ONE Sidebar Menu at the top
section = st.sidebar.radio("Choose Section", [
    "🌐 Web Utilities",
    "🖥️ Remote Access",
    "🤖 ML Demo",
    "🎙️ Voices"
])

# 🌐 Web Utilities Section
if section == "🌐 Web Utilities":
    st.title("🌐 Web Utility Panel")

    html_code = """     <h3>📍 Location & Camera Tools</h3>
    <button onclick="openMapWithLocation()">Show My Location</button><br><br>
    <button onclick="findNearbyGrocery()">Find Grocery Store Nearby</button><br><br>
    <video id="preview" width="300" autoplay muted></video><br>
    <button onclick="startCamera()">Start Camera</button>

    <script>
      function openMapWithLocation() {
        navigator.geolocation.getCurrentPosition(function(position) {
          const lat = position.coords.latitude;
          const lon = position.coords.longitude;
          const mapUrl = `https://www.google.com/maps?q=${lat},${lon}`;
          window.open(mapUrl, '_blank');
        });
      }

      function findNearbyGrocery() {
        navigator.geolocation.getCurrentPosition(function(position) {
          const lat = position.coords.latitude;
          const lon = position.coords.longitude;
          const query = `https://www.google.com/maps/search/grocery+stores/@${lat},${lon},15z`;
          window.open(query, '_blank');
        });
      }

      function startCamera() {
        navigator.mediaDevices.getUserMedia({ video: true, audio: false })
          .then(function(stream) {
            document.getElementById('preview').srcObject = stream;
          })
          .catch(function(err) {
            alert("Camera access failed: " + err);
          });
      }
    </script> """  # Your HTML code for camera and location
    html(html_code, height=500)

# 🖥️ Remote Access Section
elif section == "🖥️ Remote Access":
    st.title("🖥️ Remote Linux & Docker Command Runner")

    user = st.text_input("SSH Username")
    ip = st.text_input("Remote IP Address")
    password = st.text_input("SSH Password", type="password")

    st.subheader("🔧 Linux Commands")
    linux_cmd = st.selectbox("Choose Linux Command", ["cal", "ls -l", "whoami", "uname -a", "ifconfig"])

    st.subheader("🐳 Docker Commands")
    docker_cmd = st.selectbox("Choose Docker Command", [
        "docker images",
        "docker ps -a",
        "docker run -it ubuntu",
        "docker system df",
        "docker pull ubuntu"
    ])

    def run_remote_cmd(command):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=ip, username=user, password=password)
            stdin, stdout, stderr = ssh.exec_command(command)
            output = stdout.read().decode()
            error = stderr.read().decode()
            ssh.close()
            return output if output else error
        except Exception as e:
            return f"❌ Connection failed: {e}"

    if st.button("Run Linux Command"):
        if user and ip and password:
            result = run_remote_cmd(linux_cmd)
            st.code(result)
        else:
            st.warning("Please fill in all SSH credentials.")

    if st.button("Run Docker Command"):
        if user and ip and password:
            result = run_remote_cmd(docker_cmd)
            st.code(result)
        else:
            st.warning("Please fill in all SSH credentials.")
    # SSH input + command logic here...

# 🤖 ML Demo Section
elif section == "🤖 ML Demo":
    st.title("📈 Linear Regression Demo")

    st.markdown("Upload a CSV file with columns like `value` and `marks` to train a model.")

    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded_file:
        dataset = pd.read_csv(uploaded_file)
        st.write("📊 Preview of Data", dataset.head())

        if "value" in dataset.columns and "marks" in dataset.columns:
            X = dataset[['value']]
            y = dataset['marks']

            model = LinearRegression()
            model.fit(X, y)

            st.success("✅ Model trained successfully!")

            st.write(f"🧮 Coefficient (slope): {model.coef_[0]:.2f}")
            st.write(f"📍 Intercept: {model.intercept_:.2f}")

            input_value = st.number_input("Enter a value to predict marks", value=0.0)
            if st.button("Predict"):
                prediction = model.predict([[input_value]])
                st.write(f"📌 Predicted marks for input {input_value}: **{prediction[0]:.2f}**")
        else:
            st.error("❌ CSV must contain 'value' and 'marks' columns.")

    # CSV upload + regression logic here...

# 🎙️ Voices Section
elif section == "🎙️ Voices":
    st.title("🎙️ Voices Assistant")

    st.subheader("🔊 Text to Speech")
    text_input = st.text_input("Enter something to speak")
    if st.button("Speak"):
        engine = pyttsx3.init()
        engine.say(text_input)
        engine.runAndWait()

    st.subheader("🎧 Voice to Text")
    if st.button("Start Listening"):
        recognizer = sr.Recognizer()
        mic = sr.Microphone()
        with mic as source:
            st.write("🎤 Listening...")
            audio = recognizer.listen(source)
            result = recognizer.recognize_google(audio)
            st.write("📝 You said:", result)

            if "open notepad" in result.lower():
                os.system("notepad")
            elif "open calculator" in result.lower():
                os.system("calc")
            elif "shutdown" in result.lower():
                os.system("shutdown /s /t 1")
            elif "open cmd" in result.lower():
                os.system("start cmd")
            else:
                st.write("🗂️ No matching command found.")
