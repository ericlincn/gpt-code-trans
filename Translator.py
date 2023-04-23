from GPTUtil import GPTUtil
from StringUtil import StringUtil
import json

api_key = 'YOUR OPENAI_API_KEY'
target_lang = 'python'
source_path = 'source file path'
output_path = 'output file path'

model_id = 'text-davinci-003'

f = open(source_path, 'rb')
content = f.read()
rows = StringUtil.findLastNewlinePosition(content, 1400)
print(rows)
f.close()

f = open(source_path, 'r')
content = f.read()
str_list = StringUtil.splitFromRows(content, rows)
f.close()

translated_code_chunks = []

for i in range(len(str_list)):
    prompt_str = f"##### Translate this code into {target_lang}\n### Code\n"+ str_list[i] + f"\n### {target_lang}"
    response = GPTUtil.createTextCompletion(api_key, model_id, prompt_str, 2048, 0, ["###"])
    translated_code_chunks.append(json.loads(response)['choices'][0]['text'])

translated_code = "\n".join(translated_code_chunks)

with open(output_path, 'w') as f:
    f.write(translated_code)
