#The goal of this file is to create File ID

import openai

# Define a function to open a file and return its contents as a string
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

# Define a function to save content to a file
def save_file(filepath, content):
    with open(filepath, 'a', encoding='utf-8') as outfile:
        outfile.write(content)

# Set the OpenAI API keys by reading them from files
#api_key = open_file('/Users/arthurandersen/Documents/MenoLearn/openaiapikey2.txt')

openai.api_key = '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'

# Assuming the file name is 'processed_data.jsonl'
with open("/Users/arthurandersen/Documents/MenoLearn/Fine_Tune_GPT/modified_clean_converted_data.jsonl", "rb") as file:
    response = openai.File.create(
        file=file,
        purpose='fine-tune'
    )

file_id = response['id']
print(f"File uploaded successfully with ID: {file_id}")
