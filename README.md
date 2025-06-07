# TalentScout - AI/ML Intern Assignment

This project is a **Streamlit-based Hiring Assistant chatbot** developed for the AI/ML Intern assignment at TalentScout. It simulates an intelligent recruitment assistant that interacts with candidates, collects essential information, and generates tailored technical questions based on their declared tech stack using a Large Language Model (LLM).

---

## 🔍 Features

- 🤖 Smart conversational chatbot built with LLM
- 📋 Gathers key candidate information:
  - Full Name
  - Email Address
  - Phone Number
  - Years of Experience
  - Desired Role
  - Current Location
  - Tech Stack
- ❓ Generates 3–5 technical questions for each declared technology
- 🧠 Maintains context across conversation
- 🛡️ Handles unknown inputs and provides fallbacks
- 🛑 Detects exit keywords and ends the chat gracefully

---

## 🚀 Live Demo

- 🌐 [Streamlit App](https://ankit-nagdeve-talentscout-chatbot-app-kbqevn.streamlit.app/)
- 🎥 [Loom Video Demo](https://www.loom.com/share/17508a993b274af090d9e52061220070?sid=c5218384-6adb-4707-9c22-26205572e5f2)

---

## 🛠️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/talentscout-chatbot.git
cd talentscout-chatbot
```

### 2. Set up Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate     # Windows
# OR
source venv/bin/activate  # macOS/Linux
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

---

## 🧠 Prompt Engineering

We used prompt engineering to:

- Collect structured candidate information  
- Ask tech-stack-based questions  
- Maintain context  
- Handle fallback responses  

**Example Prompt:**

```bash
Generate 3 technical questions for a candidate who is skilled in Python and React.
```

---

## 🧰 Tech Stack

- Python – Core language  
- Streamlit – UI development  
- OpenAI GPT-3.5/4 – For intelligent response generation  
- Prompt Engineering – Custom designed LLM prompts  
- GitHub – Version control  

---

## 🧩 Challenges & Solutions

| Challenge                                 | Solution                                     |
|------------------------------------------|----------------------------------------------|
| Stateless UI                             | Used `st.session_state` in Streamlit         |
| Unexpected input from user               | Fallback logic with LLM prompt tweaks        |
| Generating tech-specific questions       | Dynamic prompt logic with tech detection     |

---

## 📄 Deliverables

- ✅ Source code uploaded on GitHub  
- ✅ README.md with setup instructions and prompt design  
- ✅ Streamlit Hosted App  
- ✅ Demo Video on Loom  
- ✅ Google Doc with explanation  
- ✅ Resume and Cover Letter  

---

## 📎 Important Links

- 🔗 GitHub Repo: https://github.com/ankit-nagdeve/talentscout-chatbot  
- 🔗 Hosted App: https://ankit-nagdeve-talentscout-chatbot-app-kbqevn.streamlit.app/ 
- 🔗 Demo Video: https://www.loom.com/share/17508a993b274af090d9e52061220070?sid=c5218384-6adb-4707-9c22-26205572e5f2  
- 🔗 Project Document: https://docs.google.com/document/d/1OW2ql-iufsgOGLEFaF0uPLaFNayPrbc2MR5QyuPzeuc/edit?tab=t.0
- 📄 Resume: (https://drive.google.com/file/d/1XN8NkueFDifIQHubC8bcKM8H5oHhsGFe/view?usp=drive_link)  

---

## 👨‍💻 Author

**Ankit Nagdeve**  
📧 ankitnagdeve@example.com  
🔗 [LinkedIn](https://linkedin.com/in/ankit-nagdeve-980917211)
