import requests
import json

class GPTUtil:

    @staticmethod
    def createTextCompletion(key:str, modelId:str, prompt:str, maxTokens:int = 16, temperature:float = 1, stop:str = "\n"):
    
        url = "https://api.openai.com/v1/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + key
        }
        payload = {
            "model": modelId,
            "prompt": prompt,
            "suffix": None,
            "max_tokens": maxTokens,
            "temperature": temperature,
            "top_p": 1,
            "n": 1,
            "stream": False,
            "logprobs": None,
            "echo": False,
            "stop": stop,
            "presence_penalty": 0,
            "frequency_penalty": 0,
            "best_of": 1,
            "logit_bias": {},
            "user": ""
        }
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        return response.text