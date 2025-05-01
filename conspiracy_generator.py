import sys
import ollama
import json

def generate_conspiracy_theory(user_input, model="llama3.2:latest"):
    """
    Generate a conspiracy theory based on user input text using Ollama.
    
    Args:
        user_input (str): Text provided by the user to seed the conspiracy theory
        model (str): The Ollama model to use
    
    Returns:
        str: The generated conspiracy theory
    """
    # Define the system prompt to guide the model's behavior
    system_prompt = """You are the AI Conspiracy Theorist, an expert at creating subtle and believable conspiracy theories that seem plausible.
    
    Your approach is characterized by these elements:
    
    1. Begin with verifiable, documented facts and events as your foundation
    2. Make small, seemingly reasonable connections between real events that most wouldn't notice
    3. Identify plausible (but fictional) patterns where others see coincidence
    4. Suggest realistic motivations based on established interests (financial gain, power, influence)
    5. Reference actual organizations, publications, and figures while implying their involvement
    6. Use precise dates, statistics, and technical terminology to add credibility
    7. Employ phrases like "some analysts suggest," "according to insiders," and "documents indicate"
    8. Create subtle implications rather than making direct accusations
    9. Include minor inconsistencies that mirror real-world conspiracy narratives
    10. Blend factual events with speculative interpretation seamlessly
    
    Your theories should feel like they *could* be true to someone who's skeptical but open-minded. They should make readers think "I'm not saying I believe this, but it does make you wonder..."
    
    Always preface your response with "NOTICE: The following is FICTIONAL content created for entertainment purposes only."
    """
    
    # Define the user prompt with the provided input
    user_prompt = f"Based on the topic '{user_input}', create a subtle and believable conspiracy theory that connects real-world events and entities in ways that seem plausible but speculative. Maintain a serious, analytical tone throughout."
    
    try:
        # Make a request to Ollama
        response = ollama.chat(
            model=model,
            messages=[
                {
                    'role': 'system',
                    'content': system_prompt
                },
                {
                    'role': 'user',
                    'content': user_prompt
                }
            ]
        )
        
        # Extract the response
        conspiracy_theory = response['message']['content']
        return conspiracy_theory
    
    except Exception as e:
        return f"Error generating conspiracy theory: {str(e)}"

def main():
    """
    Main function to run the conspiracy theory generator from command line.
    """
    if len(sys.argv) > 1:
        # Join all command line arguments as the input text
        user_input = " ".join(sys.argv[1:])
    else:
        # If no arguments provided, prompt the user
        user_input = input("Enter a topic for your conspiracy theory: ")
    
    print("\nGenerating conspiracy theory...\n")
    conspiracy_theory = generate_conspiracy_theory(user_input)
    print(conspiracy_theory)

if __name__ == "__main__":
    main() 