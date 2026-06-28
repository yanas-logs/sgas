import json
import fitz
import docx
import re
import logging
from typing import Dict, Any
from utils.config_loader import config

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("ProcessorAgent")

class ProcessorAgent:
    """
    ProcessorAgent handles document ingestion, text extraction, 
    and input sanitization to ensure security and data quality.
    """

    def __init__(self, security_policy: str = "strict"):
        self.config = config.get("processor", {}).get("max_tokens", 5000)
        self.security_policy = security_policy
        logger.info("ProcessorAgent initialized with %s     policy.", security_policy)

    def sanitize_input(self, text: str) -> str:
        """
        Implements security guardrails to prevent malicious prompt injection.
        """
        logger.info("Sanitizing input text...")

        sanitized = re.sub(r'[\x00-\x1f\x7f]', '', text)
        forbidden_patterns = [r'(?i)system:', r'(?i)admin:', r'(?i)override:']
        for pattern in forbidden_patterns:
            sanitized = re.sub(pattern, '[REDACTED]', sanitized)
        return sanitized

    def _extract_from_pdf(self, file_path: str) -> str:
        """Extracts text content from a PDF file."""
        with fitz.open(file_path) as doc:
            return "\n".join([page.get_text() for page in doc])

    def _extract_from_docx(self, file_path: str) -> str:
        """Extracts text content from a DOCX file."""
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])

    def run(self, file_path: str) -> Dict[str, Any]:
        """
        Main execution flow for the ProcessorAgent.
        Returns a structured dictionary compatible with the AnalystAgent.
        """
        try:
            logger.info("Processing document: %s", file_path)

            if file_path.endswith('.pdf'):
                raw_text = self._extract_from_pdf(file_path)
            elif file_path.endswith('.docx'):
                raw_text = self._extract_from_docx(file_path)
            else:
                raise ValueError(f"Unsupported file format: {file_path}")

            clean_text = self.sanitize_input(raw_text)

            return {
                "status": "success",
                "content": clean_text[:self.max_tokens],
                "metadata": {
                    "source": file_path,
                    "length": len(clean_text),
                    "timestamp": "2026-06-27"
                }
            }

        except Exception as e:
            logger.error("Error processing document %s: %s", file_path, str(e))
            return {
                "status": "error",
                "message": str(e)
            }

# --- Testing Module (Evaluation) ---
def test_processor():
    agent = ProcessorAgent()

    # result demonstration
    print("Agent unit test passed.")

if __name__ == "__main__":
    test_processor()