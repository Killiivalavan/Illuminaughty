import random
import datetime
import json
import ollama
import re
from io import BytesIO
from fpdf import FPDF

class EvidenceGenerator:
    """
    Generates fictional supporting evidence for conspiracy theories,
    such as research papers, articles, and other "proof" documents.
    """
    
    def __init__(self, model="llama3.2:latest"):
        self.model = model
        
        # Realistic university names for fake research papers
        self.universities = [
            "Northwestern University", "University of Michigan", "Stanford Research Institute",
            "Massachusetts Institute of Technology", "Cambridge University", "ETH Zurich",
            "University of Tokyo", "University of California", "University of Chicago",
            "Yale University", "Oxford University", "Princeton University",
            "Technical University of Berlin", "Moscow State University", "University of Delhi",
            "University of Sydney", "National University of Singapore", "Seoul National University"
        ]
        
        # Realistic journal names for citations
        self.journals = [
            "Journal of Applied Research", "International Review of Social Sciences",
            "Archives of Environmental Studies", "Frontiers in Systems Analysis",
            "Contemporary Issues in Technology", "Journal of Policy Research",
            "Studies in Global Phenomena", "Annual Review of Applied Sciences",
            "Journal of Pattern Recognition", "International Policy Review",
            "Research Quarterly", "Global Affairs Analysis", "Public Administration Review",
            "Technical Systems Journal", "Advances in Theoretical Physics",
            "Archives of Behavioral Analysis", "Quantum Applications Research"
        ]
        
        # Realistic government agencies
        self.agencies = [
            "Department of Defense", "National Security Agency", "Central Intelligence Agency",
            "Federal Bureau of Investigation", "Department of Energy", "Department of State",
            "National Reconnaissance Office", "Defense Advanced Research Projects Agency",
            "National Oceanic and Atmospheric Administration", "Federal Emergency Management Agency",
            "Department of Homeland Security", "Health and Human Services", 
            "Office of Naval Research", "National Science Foundation"
        ]
        
        # Realistic corporate names
        self.corporations = [
            "Raytheon Technologies", "Northrop Grumman", "General Dynamics",
            "Lockheed Martin", "Boeing Defense", "Palantir Technologies",
            "Leidos", "CACI International", "BAE Systems", "L3Harris Technologies",
            "Thales Group", "Booz Allen Hamilton", "SAIC", "General Electric",
            "IBM Research", "Microsoft Research", "Oracle Systems"
        ]

    def generate_research_paper(self, topic, conspiracy_elements):
        """Generate a fictional research paper as PDF"""
        
        prompt = f"""
        Generate a fictional research paper abstract and snippets that could serve as "evidence" for a conspiracy theory about: {topic}
        
        Use these elements in your response:
        {conspiracy_elements}
        
        Include:
        1. Title (make it sound academic and plausible)
        2. Authors (2-4 authors with academic affiliations)
        3. Abstract (technical language, statistics, methodology)
        4. Key findings (2-3 bullet points that seem to support the conspiracy theory)
        5. Small snippets from the "methodology" and "results" sections
        6. A few citations in the proper format
        
        Make it sound realistic, technical, and academically credible. Include specific numbers, dates, and technical terminology.
        """
        
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    'role': 'system',
                    'content': "You are an expert in creating fictional but realistic-looking academic content. Your task is to generate professional-sounding research snippets that appear legitimate."
                },
                {
                    'role': 'user',
                    'content': prompt
                }
            ],
            options={"temperature": 0.8}
        )
        
        paper_content = response['message']['content']
        
        # Create PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        
        # Add university logo placeholder
        pdf.set_font("Arial", "B", 16)
        pdf.cell(0, 10, "RESEARCH PAPER", ln=True, align="C")
        
        # Format and add content
        pdf.set_font("Arial", "", 11)
        for line in paper_content.split('\n'):
            if line.strip().startswith('#') or 'TITLE:' in line.upper() or 'AUTHORS:' in line.upper():
                # Heading
                pdf.set_font("Arial", "B", 12)
                clean_line = line.replace('#', '').strip()
                pdf.cell(0, 10, clean_line, ln=True)
                pdf.set_font("Arial", "", 11)
            else:
                # Regular text
                pdf.multi_cell(0, 5, line)
                
        # Add footer with date and disclaimers
        pdf.set_y(-30)
        pdf.set_font("Arial", "I", 8)
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        pdf.cell(0, 10, f"Document generated on {current_date}", ln=True, align="C")
        pdf.cell(0, 10, "NOTICE: This document was created for fictional entertainment purposes only.", ln=True, align="C")
        
        # Get PDF as bytes
        pdf_bytes = pdf.output(dest='S').encode('latin1')
        
        # Generate a title for the file
        title_match = re.search(r'title:?\s*(.+?)\n', paper_content, re.IGNORECASE)
        if title_match:
            title = title_match.group(1).strip()
            filename = f"{title.replace(' ', '_')[:30]}.pdf"
        else:
            filename = f"Research_Paper_{random.randint(1000, 9999)}.pdf"
            
        return BytesIO(pdf_bytes), filename, paper_content
        
    def generate_declassified_document(self, topic, conspiracy_elements):
        """Generate a fictional declassified government document"""
        
        agency = random.choice(self.agencies)
        classification = random.choice(["TOP SECRET", "SECRET", "CONFIDENTIAL"])
        year = random.randint(1960, 2010)
        
        prompt = f"""
        Generate a fictional declassified {agency} document from {year} that could serve as "evidence" for a conspiracy theory about: {topic}
        
        Use these elements in your response:
        {conspiracy_elements}
        
        Format it like a real declassified document with:
        1. Classification markings ({classification})
        2. Document ID and dates
        3. Redacted portions [REDACTED]
        4. Internal memo style formatting
        5. References to projects, operations, or initiatives
        6. Include signatures and distribution lists
        
        Make it look authentic with official-sounding language, redacted sections, and specific details. 
        Include some seemingly significant revelations related to the conspiracy theory.
        """
        
        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    'role': 'system',
                    'content': "You are an expert in creating fictional but realistic-looking government documents. Your task is to generate professional-sounding content that appears legitimate."
                },
                {
                    'role': 'user',
                    'content': prompt
                }
            ],
            options={"temperature": 0.7}
        )
        
        doc_content = response['message']['content']
        
        # Create PDF
        pdf = FPDF()
        pdf.add_page()
        
        # Add header
        pdf.set_font("Courier", "B", 14)
        pdf.cell(0, 10, classification, ln=True, align="C")
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        
        # Agency name
        pdf.set_font("Courier", "B", 12)
        pdf.cell(0, 10, agency.upper(), ln=True, align="C")
        
        # Add content with redactions
        pdf.set_font("Courier", "", 10)
        for line in doc_content.split('\n'):
            # Simulate redactions
            if '[REDACTED]' in line:
                parts = line.split('[REDACTED]')
                current_x = pdf.get_x()
                current_y = pdf.get_y()
                
                for i, part in enumerate(parts):
                    if i > 0:
                        # Draw redaction box
                        pdf.set_fill_color(0, 0, 0)
                        box_width = random.randint(15, 50)
                        pdf.rect(current_x, current_y, box_width, 5, style='F')
                        current_x += box_width + 2
                    
                    pdf.set_xy(current_x, current_y)
                    pdf.cell(0, 5, part, ln=0)
                    current_x = pdf.get_x()
                
                pdf.ln()
            else:
                pdf.multi_cell(0, 5, line)
        
        # Add footer with classification again
        pdf.set_y(-20)
        pdf.line(10, pdf.get_y(), 200, pdf.get_y())
        pdf.set_font("Courier", "B", 14)
        pdf.cell(0, 10, classification, ln=True, align="C")
        pdf.set_font("Courier", "I", 8)
        pdf.cell(0, 10, "NOTICE: This document was created for fictional entertainment purposes only.", ln=True, align="C")
        
        # Get PDF as bytes
        pdf_bytes = pdf.output(dest='S').encode('latin1')
        doc_id = f"FOIA-{agency[:3]}-{random.randint(10000, 99999)}-{year}"
        
        return BytesIO(pdf_bytes), f"{doc_id}.pdf", doc_content
    
    def generate_evidence(self, topic, conspiracy_text):
        """Generate random evidence based on the topic and conspiracy text"""
        
        # Extract key elements from conspiracy text
        elements = self._extract_key_elements(conspiracy_text)
        
        # Randomly choose which type of evidence to generate
        evidence_type = random.choice(["research", "declassified"])
        
        if evidence_type == "research":
            return self.generate_research_paper(topic, elements)
        else:
            return self.generate_declassified_document(topic, elements)
    
    def _extract_key_elements(self, conspiracy_text):
        """Extract key elements from the conspiracy text to use in evidence"""
        
        # Extract proper nouns, dates, organizations, and other key elements
        elements = []
        
        # Look for dates (YYYY or YYYY-YYYY format)
        dates = re.findall(r'\b(19|20)\d{2}(-\d{2,4})?\b', conspiracy_text)
        if dates:
            elements.append(f"Reference years: {', '.join([d[0] + (d[1] or '') for d in dates[:3]])}")
        
        # Look for organization names
        orgs = []
        for corp in self.corporations + self.agencies:
            if corp in conspiracy_text:
                orgs.append(corp)
        
        if orgs:
            elements.append(f"Organizations to mention: {', '.join(orgs[:3])}")
        
        # Look for capitalized phrases (potential proper nouns)
        proper_nouns = re.findall(r'\b[A-Z][a-zA-Z]*([ -][A-Z][a-zA-Z]*)+\b', conspiracy_text)
        if proper_nouns:
            elements.append(f"Key terms: {', '.join(list(set(proper_nouns))[:5])}")
        
        # If we couldn't extract good elements, add some generic ones
        if len(elements) < 2:
            elements.append(f"Topic: {topic}")
            elements.append(f"Include some statistical data and technical terminology")
            elements.append(f"Reference at least one government agency or research institution")
        
        return "\n".join(elements)