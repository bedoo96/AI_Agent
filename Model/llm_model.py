from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory

class LLMModel:
    def __init__(self, api_key, model_name="gpt-4", temperature=0.3):
        self.memory = ConversationBufferMemory(return_messages=True)
        self.llm = ChatOpenAI(
            api_key=api_key,
            model=model_name,
            temperature=temperature
        )
        self.prompt = ChatPromptTemplate.from_template(
            """You're an AI Assistant. respond to the following conversation:
               {full_conversation}
            """
        )

        self.chain = LLMChain(llm=self.llm, prompt=self.prompt, memory=self.memory)

    def get_response(self, user_input):
        # Access messages from the memory object
        chat_history = self.memory.load_memory_variables({})['history']
        
        # Combine chat history and user input into a single string
        full_conversation = "\n".join(chat_history) + f"\nUser: {user_input}"
        
        # Prepare the input dictionary for the prompt
        input_data = {
            "full_conversation": full_conversation,
        }
        
        # Use the LLMChain to generate a response
        response = self.chain.invoke(input_data)

        # Extract the assistant's response content
        assistant_response = response['text']  # Assuming 'text' contains the assistant's reply
        
        return assistant_response  # Return only the content of the response
