from GPTUtil import GPTUtil
import json

# Modify these lines
api_key = 'YOUR OPENAI_API_KEY'
target_lang = 'python'
source_path = 'source file path'
output_path = 'output file path'
# End

model_id = 'text-davinci-003'

f = open(source_path, 'r')
content = f.read()
f.close()

prompt_str = f"##### Translate this code into {target_lang}\n### Code\n"+ content + f"\n### {target_lang}"
response = GPTUtil.createTextCompletion(api_key, model_id, prompt_str, 2048, 0, ["###"])
output_str = json.loads(response)['choices'][0]['text']

with open(output_path, 'w') as f:
    f.write(output_str)