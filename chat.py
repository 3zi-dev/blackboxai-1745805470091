"""
Main script for the offline command-line chat program.
Handles user input/output, session management, and integrates personality, context, translation, and response modules.
"""

import os
import json
import sys
from personality import PersonalityManager
from context import ContextManager
from translation import Translator
from response import ResponseGenerator

CONFIG_FILE = "config.json"
CONVERSATION_FILE = "conversation.json"

def load_json_file(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def save_json_file(filepath, data):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def print_help():
    print("""
Commands:
  /help               Show this help message
  /save               Save current conversation and personality
  /load               Load conversation and personality from files
  /update_personality Update personality profile interactively
  /exit               Exit the chat program
""")

def main():
    print("Offline Command-Line Chat Program")
    print("Type /help for commands.\n")

    # Load or create personality
    personality_data = load_json_file(CONFIG_FILE)
    personality_manager = PersonalityManager(personality_data)

    # Load or create conversation context
    conversation_data = load_json_file(CONVERSATION_FILE)
    context_manager = ContextManager(conversation_data)

    # Initialize translator (default languages: English)
    translator = Translator(src_lang="en", tgt_lang="en")

    # Initialize response generator
    response_generator = ResponseGenerator(personality_manager, context_manager)

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting chat.")
            break

        if not user_input:
            continue

        if user_input.startswith("/"):
            # Handle commands
            cmd = user_input.lower()
            if cmd == "/help":
                print_help()
            elif cmd == "/save":
                save_json_file(CONFIG_FILE, personality_manager.get_personality())
                save_json_file(CONVERSATION_FILE, context_manager.get_context())
                print("Conversation and personality saved.")
            elif cmd == "/load":
                personality_data = load_json_file(CONFIG_FILE)
                if personality_data:
                    personality_manager.set_personality(personality_data)
                    print("Personality loaded.")
                else:
                    print("No personality config found.")
                conversation_data = load_json_file(CONVERSATION_FILE)
                if conversation_data:
                    context_manager.set_context(conversation_data)
                    print("Conversation loaded.")
                else:
                    print("No conversation history found.")
            elif cmd == "/update_personality":
                personality_manager.interactive_update()
            elif cmd == "/exit":
                print("Exiting chat.")
                break
            else:
                print("Unknown command. Type /help for list of commands.")
            continue

        # Translate user input to internal language (English)
        translated_input = translator.translate_to_internal(user_input)

        # Add user input to context
        context_manager.add_user_message(translated_input)

        # Generate response
        response_internal = response_generator.generate_response()

        # Add response to context
        context_manager.add_bot_message(response_internal)

        # Translate response to target language (user language)
        response_output = translator.translate_from_internal(response_internal)

        print(f"Bot: {response_output}")

if __name__ == "__main__":
    main()
