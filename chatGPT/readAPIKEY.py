# The dotenv package is a Python library that allows you to load environment variables from a .env file.

import os
# from jupyterNB
# from dotenv import load_dotenv, find_dotenv = load_dotenv(find_dotenv())

print(os.getenv('OPENAI_API_KEY'))      # "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"
print(os.getenv('OS'))                  # Windows_NT
