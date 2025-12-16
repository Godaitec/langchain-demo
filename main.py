import os
from dotenv import load_dotenv

# 1. Import the specific components we need
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 2. Load Environment Variables (API Key)
load_dotenv()

if not os.getenv("GOOGLE_API_KEY"):
    print("Error: GOOGLE_API_KEY not found in .env file")
    exit()

# ---------------------------------------------------------
# STEP A: THE MODEL (The Brain)
# ---------------------------------------------------------
# We allow specific parameters like 'temperature' to control creativity (0 to 1).
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7 
)

# ---------------------------------------------------------
# STEP B: THE PROMPT TEMPLATE (The Instructions)
# ---------------------------------------------------------
# This template tells the AI *how* to behave, regardless of what the user asks.
# We use {topic} as a placeholder variable that we will fill in later.
template = """
You are a helpful expert assistant. 
Please write a short, 3-bullet-point summary about the following topic:

Topic: {topic}

Ensure the tone is professional and clear.
"""

prompt = PromptTemplate.from_template(template)

# ---------------------------------------------------------
# STEP C: THE OUTPUT PARSER (The Formatter)
# ---------------------------------------------------------
# The AI normally returns a complex "Message" object. 
# This parser automatically extracts just the string text from it.
parser = StrOutputParser()

# ---------------------------------------------------------
# STEP D: THE CHAIN (The Pipeline)
# ---------------------------------------------------------
# This uses the modern "|" operator to pipe data from one step to the next.
# Data Flow: Input -> Prompt -> Model -> Parser -> Output
chain = prompt | llm | parser

# ---------------------------------------------------------
# STEP E: EXECUTION (The Interaction)
# ---------------------------------------------------------
def main():
    print("--- AI Summary Generator ---")
    print("Type 'quit' to exit.")
    
    while True:
        # 1. Get user input
        user_input = input("\nEnter a topic: ")
        
        # 2. Check for exit
        if user_input.lower() in ["quit", "exit"]:
            print("Exiting program.")
            break
            
        print(f"Generating summary for '{user_input}'...")
        
        try:
            # 3. Invoke the chain
            # We pass a dictionary matching the variable '{topic}' in our template
            response = chain.invoke({"topic": user_input})
            
            # 4. Print clean output
            print("\nResult:")
            print(response)
            print("-" * 30)
            
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()