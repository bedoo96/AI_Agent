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
        chat_history = self.memory.load_memory_variables({})['history']
        
        full_conversation = "\n".join(chat_history) + f"\nUser: {user_input}"
        input_data = {
            "full_conversation": full_conversation,
        }
        response = self.chain.invoke(input_data)
        assistant_response = response['text']  
        
        return assistant_response  # Return only the content of the response
