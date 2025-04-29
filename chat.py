#step 1: in terminal run --> pip install google-generativeai

#step 3: run the model
#import google.generativeai as ai 
from google import generativeai as ai

#API Key --> can't expose the API key as public 
API_KEY =''   #paste the API_KEY before run the program

#Configure the API
ai.configure(api_key=API_KEY)

#Create a new model
# model = ai.GenerativeModel("gemini-pro") #currently not available

model = ai.GenerativeModel("gemini-1.5-pro-latest")
#model = ai.GenerativeModel("gemini-pro-vision")--applicable
chat = model.start_chat()

#Start a conversation
while True:
    message = input('You: ')
    # if message.lower() == 'bye':
    if message == 'Thank you':
        print('Chatbot: Welcome!')
        break
    response = chat.send_message(message)
    print('Chatbot: ', response.text)

#step 2: to find the available gemini models
# from google import generativeai as ai

# ai.configure(api_key="") #paste the api key before run the program

# models = ai.list_models()
# for model in models:
#     print(model.name, model.supported_generation_methods)

#-->output of this program(currently available gemini model names are)
#         models/chat-bison-001 ['generateMessage', 'countMessageTokens']
# models/text-bison-001 ['generateText', 'countTextTokens', 'createTunedTextModel']  
# models/embedding-gecko-001 ['embedText', 'countTextTokens']
# models/gemini-1.0-pro-vision-latest ['generateContent', 'countTokens']
# models/gemini-pro-vision ['generateContent', 'countTokens']
# models/gemini-1.5-pro-latest ['generateContent', 'countTokens']
# models/gemini-1.5-pro-001 ['generateContent', 'countTokens', 'createCachedContent']
# models/gemini-1.5-pro-002 ['generateContent', 'countTokens', 'createCachedContent']
# models/gemini-1.5-pro ['generateContent', 'countTokens']
# models/gemini-1.5-flash-latest ['generateContent', 'countTokens']
# models/gemini-1.5-flash-001 ['generateContent', 'countTokens', 'createCachedContent']
# models/gemini-1.5-flash-001-tuning ['generateContent', 'countTokens', 'createTunedModel']
# models/gemini-1.5-flash ['generateContent', 'countTokens']
# models/gemini-1.5-flash-002 ['generateContent', 'countTokens', 'createCachedContent']
# models/gemini-1.5-flash-8b ['createCachedContent', 'generateContent', 'countTokens']
# models/gemini-1.5-flash-8b-001 ['createCachedContent', 'generateContent', 'countTokens']
# models/gemini-1.5-flash-8b-latest ['createCachedContent', 'generateContent', 'countTokens']
# models/gemini-1.5-flash-8b-exp-0827 ['generateContent', 'countTokens']
# models/gemini-1.5-flash-8b-exp-0924 ['generateContent', 'countTokens']
# models/gemini-2.5-pro-exp-03-25 ['generateContent', 'countTokens', 'createCachedContent']
# models/gemini-2.5-pro-preview-03-25 ['generateContent', 'countTokens', 'createCachedContent']
# models/gemini-2.5-flash-preview-04-17 ['generateContent', 'countTokens', 'createCachedContent']
# models/gemini-2.0-flash-exp ['generateContent', 'countTokens', 'bidiGenerateContent']
# models/gemini-2.0-flash ['generateContent', 'countTokens', 'createCachedContent']
# models/gemini-2.0-flash-001 ['generateContent', 'countTokens', 'createCachedContent']
# models/gemini-2.0-flash-exp-image-generation ['generateContent', 'countTokens', 'bidiGenerateContent']
# models/gemini-2.0-flash-lite-001 ['generateContent', 'countTokens', 'createCachedContent']
# models/gemini-2.0-flash-lite ['generateContent', 'countTokens', 'createCachedContent']
# models/gemini-2.0-flash-lite-preview-02-05 ['generateContent', 'countTokens', 'createCachedContent']
# models/gemini-2.0-flash-lite-preview ['generateContent', 'countTokens', 'createCachedContent']
# models/gemini-2.0-pro-exp ['generateContent', 'countTokens', 'createCachedContent']
# models/gemini-2.0-pro-exp-02-05 ['generateContent', 'countTokens', 'createCachedContent']
# models/gemini-exp-1206 ['generateContent', 'countTokens', 'createCachedContent']
# models/gemini-2.0-flash-thinking-exp-01-21 ['generateContent', 'countTokens', 'createCachedContent']
# models/gemini-2.0-flash-thinking-exp ['generateContent', 'countTokens', 'createCachedContent']
# models/gemini-2.0-flash-thinking-exp-1219 ['generateContent', 'countTokens', 'createCachedContent']
# models/learnlm-1.5-pro-experimental ['generateContent', 'countTokens']
# models/learnlm-2.0-flash-experimental ['generateContent', 'countTokens']
# models/gemma-3-1b-it ['generateContent', 'countTokens']
# models/gemma-3-4b-it ['generateContent', 'countTokens']
# models/gemma-3-12b-it ['generateContent', 'countTokens']
# models/gemma-3-27b-it ['generateContent', 'countTokens']
# models/embedding-001 ['embedContent']
# models/text-embedding-004 ['embedContent']
# models/gemini-embedding-exp-03-07 ['embedContent', 'countTextTokens']
# models/gemini-embedding-exp ['embedContent', 'countTextTokens']
# models/aqa ['generateAnswer']
# models/imagen-3.0-generate-002 ['predict']
# models/gemini-2.0-flash-live-001 ['bidiGenerateContent', 'countTokens']
        
        