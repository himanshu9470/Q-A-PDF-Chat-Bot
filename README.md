````markdown
# 📄 PDF Question Answering Chatbot

This project is a smart, interactive PDF-based chatbot that allows users to upload PDF documents and ask natural language questions about the content. It uses Hugging Face's Transformers (Roberta-based QA model), Gradio for the UI, and PyPDF2 for extracting text from PDFs.

> 🔗 GitHub Repository: [Q-A-PDF-Chat-Bot](https://github.com/himanshu9470/Q-A-PDF-Chat-Bot)

---

## 🚀 Features

- ✅ Upload and read multi-page PDFs
- 🤖 Ask natural language questions about the PDF content
- 📊 Get context-aware answers with confidence scores
- 📥 Text preprocessing and cleaning for improved QA accuracy
- 🧠 Fallback response handling for generic or unrelated questions
- 💬 Chat history maintained in an interactive UI
- 🧰 Built using `Gradio`, `Transformers`, and `PyPDF2`

---

## 🛠️ Tech Stack

| Tech       | Description                               |
|------------|-------------------------------------------|
| Python     | Core programming language                 |
| Gradio     | UI interface for chatbot and PDF upload   |
| Transformers | QA model (`deepset/roberta-base-squad2`) |
| PyPDF2     | Extracts text from uploaded PDFs          |
| Regex      | Cleans and formats extracted text         |

---

## 🔧 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/himanshu9470/Q-A-PDF-Chat-Bot.git
   cd Q-A-PDF-Chat-Bot
````

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**

   ```bash
   python app.py
   ```

4. **Open in Browser:**

   ```
   http://localhost:7860
   ```

---

## 🖼️ Usage

1. **Upload PDF**: Use the file uploader to select and upload any `.pdf` file.
2. **Ask Questions**: Enter your question in natural language.
3. **View Answers**: Get AI-powered answers extracted from the PDF context.
4. **Fallbacks**: If the answer is not found, you'll receive a helpful fallback message.
5. **Clear Chat**: Reset the chatbot using the "Clear Chat" button.

---

## 📁 File Structure

```bash
Q-A-PDF-Chat-Bot/
│
├── app.py              # Main application script
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 📚 Example Questions

Try asking:

* *"What is the objective of this paper?"*
* *"Summarize the introduction section."*
* *"What are the key findings?"*

---

## 🤝 Contributions

Feel free to fork this repository and submit pull requests. Suggestions and issues are welcome!

---

## 🧑‍💻 Author

**Himanshu Kumar Vishwakarma**

GitHub: [@himanshu9470](https://github.com/himanshu9470)

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

```

---

Let me know if you'd like to include **screenshots**, **demo video link**, or **deployment instructions** (e.g., on Hugging Face Spaces or Streamlit).
```