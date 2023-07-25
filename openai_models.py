# Author: Viet Dac Lai
import openai
import pprint

openai.organization = "org-zJaiA5ioH4J7kitzHfUJms3O"
openai.api_key = "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"

GPT4 = 'gpt-3.5-turbo-16k'
MODEL_NAME = GPT4
model = openai.Model(MODEL_NAME)

def list_all_models():
    model_list = openai.Model.list()['data']
    model_ids = [x['id'] for x in model_list]
    model_ids.sort()
    pprint.pprint(model_ids)

def send_message(message):
       response = openai.ChatCompletion.create(
           model=GPT4,  # Choose the appropriate model for your use case
           messages=[
               {"role": "system", "content": "You are a helpful assistant."},
               {"role": "user", "content": message}
           ]
       )
       return response.choices[0].message.content
message = "HOLA GPT"
response = send_message(message)
print(response)