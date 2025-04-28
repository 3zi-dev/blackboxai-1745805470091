"""
Personality management module.
Handles loading, updating, and applying the personality or master prompt that shapes chatbot responses.
"""

import json

class PersonalityManager:
    def __init__(self, personality_data=None):
        """
        Initialize with existing personality data or default.
        personality_data: dict with keys like 'name', 'description', 'style', 'master_prompt'
        """
        if personality_data is None:
            self.personality = {
                "name": "DefaultBot",
                "description": "A friendly and helpful chatbot.",
                "style": "polite and informative",
                "master_prompt": "You are a friendly and helpful assistant."
            }
        else:
            self.personality = personality_data

    def get_personality(self):
        """Return the current personality data."""
        return self.personality

    def set_personality(self, personality_data):
        """Set personality data."""
        self.personality = personality_data

    def interactive_update(self):
        """Interactively update personality fields."""
        print("Updating personality profile. Press Enter to keep current value.\n")
        for key in ["name", "description", "style", "master_prompt"]:
            current = self.personality.get(key, "")
            prompt = f"{key.capitalize()} [{current}]: "
            new_value = input(prompt).strip()
            if new_value:
                self.personality[key] = new_value
        print("Personality updated.\n")

    def apply_personality(self, input_text):
        """
        Apply personality shaping to input text.
        For this simple implementation, prepend the master prompt to input.
        """
        prompt = self.personality.get("master_prompt", "")
        return f"{prompt}\nUser said: {input_text}"
