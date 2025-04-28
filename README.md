# Offline Command-Line Chat Program

## Overview
This is a fully offline, system-dependent command-line chat program written in Python. It supports:
- User input and output in configurable languages with offline translation.
- Personality or master prompt shaping to influence chatbot responses.
- Context management to maintain conversation history locally.
- Incremental refinement of personality during runtime.
- Uses only free, open-source, lightweight NLP and translation libraries.
- Stores all data locally in human-readable JSON files.
- Runs on typical modern laptops without GPU or internet connection.

## Features
- Offline translation using Argos Translate.
- Personality profile loaded from config file and modifiable at runtime.
- Context stored and loaded from JSON files.
- Simple rule-based response generation influenced by personality and context.
- Command-line interface with options to save/load sessions and update personality.
- Error handling and user guidance.

## Installation

1. Install Python 3.8 or higher from [python.org](https://www.python.org/downloads/).

2. Install required Python packages offline or online:
```
pip install argostranslate
pip install fasttext
```
(Argos Translate requires downloading language packages separately; instructions provided in usage.)

## Usage

Run the chat program:
```
python chat.py
```

At startup, you can load or create a personality profile. Use commands to save/load sessions, update personality, and exit.

## Configuration

- Personality profiles and conversation history are stored in JSON files (`config.json`, `conversation.json`).
- You can edit or create personality profiles to shape chatbot identity and style.

## Extending the System

- Add more sophisticated NLP or lightweight ML models for better response generation.
- Integrate additional offline translation language packages.
- Enhance personality refinement with more complex prompt parsing.
- Add GUI or web interface while maintaining offline operation.

## License

This project uses only free and open-source software components.
