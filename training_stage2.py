#The goal of this file is to create Job ID
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
#api_key = open_file('openaiapikey2.txt')

openai.api_key = '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'

# Using the provided file_id
file_id = "file-qsuXuuHC5t4BM8lRzijAxjRJ" #(where replace it with a new file id created from stage1)

# Using the base model if you prefer
model_name = "gpt-3.5-turbo"  # Or another base model if you prefer

response = openai.FineTuningJob.create(
    training_file=file_id,
    model=model_name
)

job_id = response['id']
print(f"Fine-tuning job created successfully with ID: {job_id}")
