[![Apache 2.0 License](https://img.shields.io/badge/license-Apache-blue.svg?style=flat)](LICENSE.md)

# gpt-code-translator
Translate any of your source code file into Python code, or translate the source code for other languages.

Dependencies
------------
- requests

Usage
-----
1. Modify the api_key, target_lang, source_path & output_path in Translator.py
2. Run Translator.py

Limitations
-----------
The total number of tokens in the source code file must be less than 2048. This corresponds to a file size of around 10K.
