import PyPDF2
import json

def extract_qa_from_pdf(pdf_path):
    """
    Extract questions and answers from a PDF file
    
    Args:
        pdf_path (str): Path to the PDF file
    
    Returns:
        list: List of dictionaries with 'question' and 'answer' keys
    """
    qa_pairs = []
    
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)
        
        # Extract text from all pages
        full_text = ""
        for page in pdf_reader.pages:
            full_text += page.extract_text()
        
        # Basic parsing (you may need to customize this)
        # Assumes questions and answers are separated by some pattern
        sections = full_text.split('\n\n')
        
        for section in sections:
            # Simple heuristic to separate questions and answers
            if '?' in section:
                parts = section.split('?', 1)
                if len(parts) == 2:
                    question = parts[0].strip() + '?'
                    answer = parts[1].strip()
                    
                    qa_pairs.append({
                        'text': f"Question: {question}\nAnswer: {answer}"
                    })
    
    return qa_pairs

def save_dataset(qa_pairs, output_path='memory_dataset.json'):
    """
    Save QA pairs to a JSON file for model training
    
    Args:
        qa_pairs (list): List of QA dictionaries
        output_path (str): Path to save the JSON file
    """
    with open(output_path, 'w') as f:
        json.dump(qa_pairs, f, indent=2)

def main():
    pdf_path = 'Chapter 1 Arjuna’s Dilemma.pdf'
    qa_pairs = extract_qa_from_pdf(pdf_path)
    save_dataset(qa_pairs)
    print(f"Extracted {len(qa_pairs)} Q&A pairs")

if __name__ == "__main__":
    main()