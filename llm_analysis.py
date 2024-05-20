import os
from openai import OpenAI


# context is going to be the transcript from the STT model and description of the actual picture.
# This is just a place holder. 
context = """
Age is 37 months. Original Sentence was: "This is a car."
The child read it as: "This is a car."
"""

def llm_analysis(context: str) -> str:
    
    client = OpenAI(

        api_key=os.environ.get("OPENAI_API_KEY"),
        )   
      
    # The prompt also needs to be further engineered. This is a place-holder. 
    prompt= f"""You are a helpful Early Childhood Development Researcher who specializes in child education evaluation. 
        The context provided consists of a sentence and some personal data on the child. Depending on the complexity 
        of the sentence and personal data, provide supportive instructions and guidance for the child in manner 
        that the child feels encouraged to learn more.
        
        Context: {context}

        Helpful instructions for the child:"""
        
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
    
print(llm_analysis(context))