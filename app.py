import gradio as gr
from transformers import pipeline
import PyPDF2
import io
import re
from typing import List, Tuple

# Initialize components
pdf_text = ""
qa_pipeline = pipeline(
    "question-answering",
    model="deepset/roberta-base-squad2",  # More accurate model
    device=-1  # Use CPU
)

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Improved PDF text extraction with better preprocessing"""
    global pdf_text
    try:
        # Convert bytes to file-like object
        pdf_file = io.BytesIO(file_bytes)
        reader = PyPDF2.PdfReader(pdf_file)
        
        # Extract and clean text from each page
        clean_text = []
        for page in reader.pages:
            text = page.extract_text() or ""  # Handle None returns
            # Basic cleaning
            text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
            text = re.sub(r'[^\w\s.,;:!?()-]', ' ', text)  # Remove special chars
            clean_text.append(text.strip())
        
        pdf_text = " ".join(clean_text)
        if not pdf_text.strip():
            return "⚠️ PDF loaded but no text could be extracted"
        return f"✅ PDF loaded ({len(reader.pages)} pages, {len(pdf_text.split())} words)"
    except Exception as e:
        return f"❌ Error loading PDF: {str(e)}"

def answer_from_pdf(question: str) -> Tuple[str, float]:
    """Enhanced PDF answering with better confidence handling"""
    if not pdf_text or len(pdf_text.split()) < 20:  # Minimum 20 words
        return "", 0.0
    
    try:
        result = qa_pipeline(
            question=question,
            context=pdf_text,
            top_k=3,  # Get multiple potential answers
            max_answer_len=150,
            handle_impossible_answer=True
        )
        
        # Select best answer with sufficient confidence
        for answer in result:
            if answer['score'] > 0.4 and answer['answer'].strip():  # Higher threshold
                return answer['answer'], answer['score']
        
        return "", 0.0
    except:
        return "", 0.0

def generate_response(question: str) -> str:
    """Smart response generation with multiple fallbacks"""
    question = question.strip()
    if not question:
        return "Please ask a question about the PDF"
    
    # Try to answer from PDF
    pdf_answer, confidence = answer_from_pdf(question)
    if confidence > 0:
        return f"📄 Answer (confidence: {confidence:.0%}): {pdf_answer}"
    
    # Fallback responses
    fallbacks = {
        "hello": "Hello! Ask me about the PDF you uploaded.",
        "hi": "Hi there! How can I help you with the PDF?",
        "thank you": "You're welcome!",
        "what can you do": "I can answer questions about PDF documents you upload.",
        "who are you": "I'm your PDF analysis assistant.",
        "help": "I can help you with questions about the PDF. Just ask!",
        "bye": "Goodbye! Feel free to return if you have more questions.",
        "thanks": "No problem! Let me know if you have more questions.",
        "goodbye": "Goodbye! I'm here if you need help with the PDF.",
        "what is your name": "I'm your PDF assistant. You can call me PDF Bot.",
        "how are you": "I'm just a program, but thanks for asking! How can I assist you today?",
        "what is this": "This is a PDF question-answering assistant. Upload a PDF and ask questions about it.",
        "what is pdf": "PDF stands for Portable Document Format. It's a file format used to present documents in a manner independent of application software, hardware, and operating systems.",
        "what is your purpose": "My purpose is to help you find information in PDF documents by answering your questions.",
        "can you help me": "Of course! Just ask your question about the PDF.",
        "can you answer questions": "Yes, I can answer questions about the PDF you uploaded.",
        "can you read pdf": "Yes, I can read and extract information from PDF documents.",
        "can you summarize": "I can help summarize information from the PDF if you ask specific questions.",
    }
    
    # Check for similar fallback questions
    q_lower = question.lower()
    for key in fallbacks:
        if key in q_lower:
            return fallbacks[key]
    
    # Final fallback
    return "I couldn't find a specific answer in the PDF. Try asking differently or check if the PDF contains relevant information."

def chat_interface(message: str, history: List[Tuple[str, str]]) -> Tuple[str, List[Tuple[str, str]]]:
    """Handle chat interactions"""
    response = generate_response(message)
    history.append((message, response))
    return "", history

# Create Gradio interface
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 📄 PDF Question Answering")
    
    with gr.Row():
        with gr.Column(scale=1):
            pdf_upload = gr.File(
                label="Upload PDF",
                type="binary",
                file_types=[".pdf"]
            )
            upload_status = gr.Textbox(label="Status")
        
        with gr.Column(scale=2):
            chatbot = gr.Chatbot(height=450)
            question = gr.Textbox(
                label="Ask about the PDF",
                placeholder="Type your question here..."
            )
            clear = gr.Button("Clear Chat")
    
    # Event handlers
    pdf_upload.change(
        extract_text_from_pdf,
        inputs=pdf_upload,
        outputs=upload_status
    )
    
    question.submit(
        chat_interface,
        inputs=[question, chatbot],
        outputs=[question, chatbot]
    )
    
    clear.click(
        lambda: [],
        None,
        chatbot,
        queue=False
    )

if __name__ == "__main__":
    demo.launch(server_port=7860)