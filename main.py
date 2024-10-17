import streamlit as st
from Model.llm_model import LLMModel
from Memory.memory_manager import MemoryManager
from Streamlit.index import ChatInterface
from dotenv import load_dotenv
import os

load_dotenv()

# Retrieve the variables
openai_api_key = os.getenv("OPENAI_API_KEY")

memory_manager = MemoryManager(st.session_state)
llm_model = LLMModel(api_key=openai_api_key)
chat_interface = ChatInterface(memory_manager, llm_model)

chat_interface.run()