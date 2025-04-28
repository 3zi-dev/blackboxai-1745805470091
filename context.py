"""
Context management module.
Handles storing, loading, and managing conversation history to maintain coherent dialogue.
"""

class ContextManager:
    def __init__(self, context_data=None):
        """
        Initialize with existing context data or empty.
        context_data: dict with keys 'messages' which is a list of dicts with 'role' and 'text'.
        """
        if context_data is None:
            self.context = {"messages": []}
        else:
            self.context = context_data

    def get_context(self):
        """Return the current conversation context."""
        return self.context

    def set_context(self, context_data):
        """Set conversation context."""
        self.context = context_data

    def add_user_message(self, text):
        """Add a user message to the context."""
        self.context["messages"].append({"role": "user", "text": text})

    def add_bot_message(self, text):
        """Add a bot message to the context."""
        self.context["messages"].append({"role": "bot", "text": text})

    def get_recent_context(self, max_messages=10):
        """
        Get the most recent messages up to max_messages.
        Useful for response generation context window.
        """
        return self.context["messages"][-max_messages:]
