# import streamlit as st

# class ChatInterface:
#     def __init__(self, memory_manager, llm_model):
#         self.memory_manager = memory_manager
#         self.llm_model = llm_model

#     def display_chat(self):
#         st.title("Conversational Chat With memory")
#         st.caption("Have a friendly conversation with LLM model 💯")

#         # Display previous messages from memory
#         for message in self.memory_manager.get_messages():
#             with st.chat_message(message["role"]):
#                 st.markdown({message["content"]})

#     def get_user_input(self):
#         return st.chat_input("What is up?")

#     def display_user_message(self, prompt):
#         self.memory_manager.add_message("user", prompt)
#         with st.chat_message("user"):
#             st.markdown(prompt)

#     def display_response(self, response):
#         self.memory_manager.add_message("assistant", response)
#         with st.chat_message("assistant"):
#             st.markdown(response)

#     def run(self):
#         self.memory_manager.initialize_memory()
#         self.display_chat()

#         if prompt := self.get_user_input():
#             self.display_user_message(prompt)
#             # Ensure to call get_response with only user_input
#             response = self.llm_model.get_response(prompt)
#             self.display_response(response)


import streamlit as st

class ChatInterface:
    def __init__(self, memory_manager, llm_model):
        self.memory_manager = memory_manager
        self.llm_model = llm_model

    def display_chat(self):
        st.title("Conversational Chat With Memory")
        st.caption("Have a friendly conversation with LLM model 💯")

        # Display previous messages from memory
        for message in self.memory_manager.get_messages():
            if message["role"] == "user":
                # Display user messages on the right
                st.markdown(f"<div style='text-align: right;'><b>User:</b> {message['content']}</div>\n", unsafe_allow_html=True)
            else:
                # Display assistant messages on the left
                st.markdown(f"<div style='text-align: left;'><b>Assistant:</b> {message['content']}</div>\n", unsafe_allow_html=True)

    def get_user_input(self):
        return st.chat_input("What is up?")

    def display_user_message(self, prompt):
        self.memory_manager.add_message("user", prompt)
        # Display user messages on the right
        st.markdown(f"<div style='text-align: right;'><b>User:</b> {prompt}</div>\n", unsafe_allow_html=True)

    def display_response(self, response):
        self.memory_manager.add_message("assistant", response)
        # Display assistant messages on the left
        st.markdown(f"<div style='text-align: left;'><b>Assistant:</b> {response}</div>\n", unsafe_allow_html=True)

    def run(self):
        self.memory_manager.initialize_memory()
        self.display_chat()

        if prompt := self.get_user_input():
            self.display_user_message(prompt)
            # Ensure to call get_response with only user_input
            response = self.llm_model.get_response(prompt)
            self.display_response(response)
