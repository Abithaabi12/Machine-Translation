# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l1Venuo5qT8djXij2tJV5HjnfJFO1smF
"""

from transformers import pipeline

# Initialize the translation pipeline
translator = pipeline("translation_en_to_de", model="Helsinki-NLP/opus-mt-en-de")

# Example English text
english_text = "Hello, world! This is a test of the machine translation system."

# Translate the English text to German
translated = translator(english_text, max_length=40)

# Print the translated text
print(translated[0]['translation_text'])