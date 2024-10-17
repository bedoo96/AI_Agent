
import streamlit as st

class ChatInterface:
    def __init__(self, memory_manager, llm_model):
        self.memory_manager = memory_manager
        self.llm_model = llm_model

    def display_chat(self):
        st.title("Conversational Chat With Memory")
        st.caption("Have a friendly conversation with LLM model 💯")

        for message in self.memory_manager.get_messages():
            if message["role"] == "user":
                st.markdown(f"<div style='text-align: right;'><b>User:</b> {message['content']}</div>\n", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='text-align: left;'><b>Assistant:</b> {message['content']}</div>\n", unsafe_allow_html=True)

    def get_user_input(self):
        return st.chat_input("What is up?")

    def display_user_message(self, prompt):
        self.memory_manager.add_message("user", prompt)
        st.markdown(f"<div style='text-align: right;'><b>User:</b> {prompt}</div>\n", unsafe_allow_html=True)

    def display_response(self, response):
        self.memory_manager.add_message("assistant", response)
        st.markdown(f"<div style='text-align: left;'><b>Assistant:</b> {response}</div>\n", unsafe_allow_html=True)

    def run(self):
        self.memory_manager.initialize_memory()
        self.display_chat()

        if prompt := self.get_user_input():
            self.display_user_message(prompt)
            response = self.llm_model.get_response(prompt)
            self.display_response(response)
