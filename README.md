# Illuminaughty

A Python-based tool that generates elaborate, believable conspiracy theories based on user input.

## Prerequisites

- Python 3.7+
- Ollama installed locally (https://ollama.ai)
- llama3.2:latest model pulled in Ollama

## Setup

1. Make sure Ollama is installed and running
2. Pull the llama3.2 model: `ollama pull llama3.2:latest`
3. Install required packages: `pip install -r requirements.txt`

## Usage

### Command Line

Run the basic script:

```bash
python conspiracy_generator.py "5G networks and birds"
```

Or run the advanced structured version:

```bash
python advanced_conspiracy_generator.py "The International Space Station and secret experiments"
```

### Web Interface (Streamlit)

For a nicer interface with full formatting:

```bash
streamlit run app.py
```

This will start a local web server and open the app in your browser. Enter your topic and click "Generate Conspiracy Theory" to create an elaborate conspiracy narrative.

## Features

### Basic Conspiracy Generator
- Creates detailed fictional conspiracy theories
- Connects seemingly unrelated events or people
- Identifies fictional hidden groups or organizations
- Explains supposed motivations and methods
- References fictional "evidence"
- Creates timelines of key events

### Advanced Conspiracy Generator
- Uses advanced prompt engineering and few-shot learning
- Creates more believable and nuanced conspiracy theories
- Includes key elements like:
  - A compelling main theory/premise
  - Historical background and context
  - Key players and their supposed motivations
  - "Evidence" that appears to support the theory
  - How the supposed conspiracy is maintained
  - Potential implications and significance
- Formats the theory in a style that mimics investigative journalism or academic analysis

## How It Works

The advanced generator creates compelling conspiracy theories by:

1. **Using advanced prompt engineering** - Carefully crafted system instructions
2. **Few-shot learning** - Providing detailed examples for the model to learn from
3. **Flexible formatting** - Adapting the structure to suit the specific topic
4. **Controlled creativity** - Balancing fact and fiction with realistic connections

This approach creates theories that feel like investigative journalism, connecting dots that most people miss. The result is a narrative that makes a skeptical reader pause and consider "What if this were true?"

## Next Steps

This is part of a larger project that will eventually include:
- Document synthesis (fake reports, emails, etc.)
- Data visualization (charts and graphs supporting the theory)
- AI-generated imagery of "evidence"

## Disclaimer

All conspiracy theories generated are entirely fictional and created for entertainment purposes only. None of the generated content should be taken as factual information. 
