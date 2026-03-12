# AI Compliance Copilot for Meydan Free Zone

An AI-powered regulatory copilot designed to assist entrepreneurs in navigating company formation, licensing, visa procedures, and compliance workflows in Meydan Free Zone, Dubai.

This project demonstrates how Retrieval-Augmented Generation (RAG) can be applied to build domain-specific AI systems that provide grounded, context-aware guidance for real-world regulatory processes.

---

## Problem

Entrepreneurs setting up companies in UAE free zones often face:

- Fragmented regulatory information across multiple sources  
- Confusion around visa eligibility and sequencing  
- Delays due to incomplete documentation  
- Lack of clear compliance workflow visibility  
- Dependence on consultants for basic procedural guidance  

Even though free zones provide digital setup portals, founders still struggle to understand the end-to-end regulatory journey.

---

## Solution

The Meydan Free Zone AI Compliance Copilot provides:

- Context-aware regulatory guidance using curated knowledge sources  
- Step-by-step support for company formation workflows  
- AI-assisted understanding of licensing and visa procedures  
- Semantic retrieval of relevant compliance information  
- Grounded responses instead of generic chatbot outputs  

This transforms static regulatory documentation into an interactive decision-support system.

---

## System Architecture

The system follows a Retrieval-Augmented Generation (RAG) architecture.

### Pipeline

1. Regulatory documents are collected and stored as a domain knowledge base  
2. Documents are split into semantic chunks for efficient retrieval  
3. Each chunk is converted into vector embeddings  
4. A FAISS vector index enables fast similarity search  
5. User queries are embedded and matched against the vector store  
6. Relevant context is retrieved  
7. The language model generates a grounded, contextual response  

![Architecture](architecture.png)

### Why RAG?

Traditional chatbots generate generic responses.  
RAG enables:

- Domain grounding  
- Regulatory accuracy  
- Reduced hallucinations  
- Explainable AI behaviour  
- Scalable knowledge updates  

This approach is suitable for enterprise regulatory automation systems.

---

## Demo

### Application Interface

Below is the Streamlit interface demonstrating the AI Compliance Copilot.

![UI Screenshot](screenshots/ui.png)

### Example Query

**User Question**

> How do I register a company in Meydan Free Zone?

**AI Behaviour**

- Retrieves licensing workflow context  
- Identifies required regulatory steps  
- Generates structured procedural guidance  

---

## Tech Stack

- Python  
- Streamlit  
- OpenAI API    
- FAISS Vector Database  
- NumPy  

### AI Techniques Used

- Retrieval-Augmented Generation (RAG)  
- Semantic Search  
- Vector Embeddings  
- Context Grounding  

---

## Project Structure

```
meydan-ai-compliance-copilot
│
├── app
│   └── app.py
│
├── docs
│   ├── faq.txt
│   ├── license_renewal.txt
│   ├── setup_process.txt
│   └── visa_challenges.txt
│
├── screenshots
│   ├── ui.png
│   └── example-answer.png
│
├── architecture.png
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository:

```
git clone https://github.com/yourusername/meydan-ai-compliance-copilot.git
```

Navigate into the project directory:

```
cd meydan-ai-compliance-copilot
```

Install the required dependencies:

```
pip install -r requirements.txt
```

---

# Running the Application

Start the Streamlit application:

```
python -m streamlit run app/app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

Enter your OpenAI API key and start asking questions.

---

## Example Questions the System Can Handle

- How do I register a company in Meydan Free Zone?  
- What documents are required for trade license approval?  
- How does visa allocation work for founders?  
- What compliance steps must startups follow?  
- How does license renewal work in UAE free zones?  

---

## Future Improvements

- Integration with official free-zone APIs  
- Multilingual support (Arabic + English)  
- Workflow automation instead of static guidance  
- Live regulatory data updates  
- Support for multiple UAE free zones  
- Deployment as enterprise SaaS compliance platform  

---

## Use Cases

- Entrepreneurs planning UAE company formation  
- Free-zone authorities building AI support systems  
- Business consultants automating regulatory guidance  
- AI researchers exploring domain-specific RAG systems  

---

## Author

Ashish Seru  
MSc Artificial Intelligence  
De Montfort University Dubai  

---

## License

This project is intended for educational, research, and demonstration purposes.
## License

This project is intended for educational, research, and demonstration purposes.
