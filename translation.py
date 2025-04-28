"""
Translation module.
Implements offline translation using Argos Translate.
"""

import argostranslate.package
import argostranslate.translate
import os
import sys

class Translator:
    def __init__(self, src_lang="en", tgt_lang="en"):
        """
        Initialize translator with source and target language codes (e.g., 'en', 'es').
        Loads Argos Translate packages if available.
        """
        self.src_lang = src_lang
        self.tgt_lang = tgt_lang
        self.installed_languages = argostranslate.translate.get_installed_languages()
        self.src_lang_obj = None
        self.tgt_lang_obj = None
        self.translation_installed = False

        self._setup_translation()

    def _setup_translation(self):
        """
        Setup translation languages and check if translation package is installed.
        """
        src = None
        tgt = None
        for lang in self.installed_languages:
            if lang.code == self.src_lang:
                src = lang
            if lang.code == self.tgt_lang:
                tgt = lang
        if src and tgt:
            self.src_lang_obj = src
            self.tgt_lang_obj = tgt
            # Check if translation between src and tgt is available
            for translation in src.translations:
                if translation.to_lang.code == self.tgt_lang:
                    self.translation_installed = True
                    break

    def translate_to_internal(self, text):
        """
        Translate user input from source language to internal language (English).
        If source language is English, returns text unchanged.
        """
        if self.src_lang == "en" or not self.translation_installed:
            return text
        try:
            translation = self.src_lang_obj.get_translation(self.tgt_lang_obj)
            return translation.translate(text)
        except Exception as e:
            print(f"Translation error: {e}")
            return text

    def translate_from_internal(self, text):
        """
        Translate response from internal language (English) to target language.
        If target language is English, returns text unchanged.
        """
        if self.tgt_lang == "en" or not self.translation_installed:
            return text
        try:
            translation = self.tgt_lang_obj.get_translation(self.src_lang_obj)
            return translation.translate(text)
        except Exception as e:
            print(f"Translation error: {e}")
            return text
