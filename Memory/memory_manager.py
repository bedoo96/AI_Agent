class MemoryManager:
    def __init__(self, session_state):
        self.session_state = session_state

    def initialize_memory(self):
        if "messages" not in self.session_state:
            self.session_state.messages = []

    def add_message(self, role, content):
        self.session_state.messages.append({"role": role, "content": content})


    def get_messages(self):
        return self.session_state.messages
