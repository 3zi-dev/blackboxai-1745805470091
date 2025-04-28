"""
Response generation module.
Generates contextually rich, emotionally nuanced responses based on personality and conversation context.
Implements a simple rule-based system for demonstration.
"""

import random

class ResponseGenerator:
    def __init__(self, personality_manager, context_manager):
        """
        Initialize with personality and context managers.
        """
        self.personality_manager = personality_manager
        self.context_manager = context_manager

    def generate_response(self):
        """
        Generate a response based on recent conversation context and personality.
        This simple implementation uses personality style and master prompt to influence response.
        """
        personality = self.personality_manager.get_personality()
        style = personality.get("style", "friendly")
        master_prompt = personality.get("master_prompt", "")

        recent_messages = self.context_manager.get_recent_context(max_messages=6)

        # Extract last user message
        last_user_message = None
        for msg in reversed(recent_messages):
            if msg["role"] == "user":
                last_user_message = msg["text"]
                break

        if not last_user_message:
            return "Hello! How can I assist you today?"

        # Simple rule-based response examples
        greetings = ["hello", "hi", "hey", "greetings"]
        farewells = ["bye", "goodbye", "see you", "farewell"]

        lower_msg = last_user_message.lower()

        if any(greet in lower_msg for greet in greetings):
            responses = [
                f"Hello! I'm here to help you.",
                f"Hi there! How can I assist you today?",
                f"Hey! What can I do for you?"
            ]
            return random.choice(responses)

        if any(farewell in lower_msg for farewell in farewells):
            responses = [
                "Goodbye! Have a great day!",
                "See you later! Take care!",
                "Farewell! I'm here whenever you need me."
            ]
            return random.choice(responses)

        # For other inputs, echo with personality style
        response_templates = [
            f"As a {style} assistant, I think: {{}}",
            f"Considering my personality as {style}, I would say: {{}}",
            f"In my {style} style, here's my response: {{}}"
        ]

        # Simple echo with slight modification
        response_content = f"I received your message: '{last_user_message}'. Let's talk more!"

        response = random.choice(response_templates).format(response_content)

        return response
