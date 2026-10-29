# 🤖 Automated Code Reviewer & Explainer

An AI-powered code analysis tool built with **Python, Streamlit, and Groq LLMs** that helps developers review code for potential bugs, understand program logic, and improve code quality through natural-language explanations.

## 🚀 Features

- **🐛 Bug Review:** Identify potential syntax errors, logical bugs, runtime errors, security concerns, and performance issues.
- **📖 Code Explanation:** Understand code through line-by-line explanations and step-by-step execution flow.
- **⚡ Code Optimization:** Get suggestions to improve readability, performance, and maintainability.
- **💻 Multi-language Support:** Analyze Python and SQL code.
- **🧠 LLM-powered Analysis:** Use Groq's API to access supported large language models.
- **📝 Markdown Responses:** Display structured analysis with headings, explanations, and code snippets.
- **🔐 Secure API Configuration:** Store API credentials in environment variables.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Interactive web interface |
| Groq API | LLM inference |
| Large Language Models | Code review and explanation |
| python-dotenv | Environment variable management |
| Git and GitHub | Version control |

## 🏗️ Project Structure

```text
automated-code-reviewer/
├── app.py              # Streamlit user interface
├── llm_service.py      # Groq API integration
├── prompts.py          # Task-specific prompts
├── requirements.txt    # Python dependencies
├── .env                # API key (not committed)
├── .gitignore          # Files excluded from Git
└── README.md           # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/automated-code-reviewer.git
cd automated-code-reviewer
```

Replace `YOUR_USERNAME` with your GitHub username and use your actual repository URL.

### 2. Create a virtual environment

**Windows PowerShell:**

```powershell
python -m venv test_env
.\test_env\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

If you haven't created `requirements.txt` yet, add:

```text
streamlit
groq
python-dotenv
```

Then run the installation command again.

### 4. Configure the Groq API key

Create a `.env` file in the project root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get your API key from the [Groq Console](https://console.groq.com/).

**Security:** Never commit your `.env` file or publish your API key. Ensure `.env` is included in `.gitignore`.

### 5. Configure the LLM model

Select a currently supported model ID from the [Groq model documentation](https://console.groq.com/docs/models).

Ensure the model ID entered in the application matches an available model.

### 6. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

## 🖥️ How to Use

1. Launch the Streamlit application.
2. Select a programming language: Python or SQL.
3. Choose an action:
   - Review for Bugs
   - Explain Logic
   - Optimize Code
4. Paste your source code into the editor.
5. Enter a supported Groq model ID if requested by the application.
6. Click **Analyze Code**.
7. Review the AI-generated feedback and suggested improvements.

## 📌 Example

### Input

```python
def divide(a, b):
    return a / b

print(divide(10, 0))
```

### Expected analysis

The LLM may identify the following issue:

- **Issue
