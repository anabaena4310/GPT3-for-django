from django.shortcuts import render
from django.views.generic import TemplateView

import openai
import os

# sample用
import requests

# gpt3_key = os.environ['GPT3_KEY']
a3rt_key = os.environ['A3RT_KEY']

class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = {
            'response': "返信をここに表示します",
        }
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        # openai.api_key = gpt3_key
        input_text = request.POST['sentence']
        engine_type = request.POST['engine type']

        # response = openai.Completion.create(
        #     engine=engine_type,
        #     prompt="Human: " + input_text + "\nAI: ",
        #     temperature=0.9,
        #     max_tokens=30,
        #     top_p=1,
        #     frequency_penalty=1,
        #     presence_penalty=0.6,
        #     stop = ["\n", " Human:", " AI:"]

        # )

        # sample用
        params = {'apikey': a3rt_key, 'query': input_text}

        response = requests.post('https://api.a3rt.recruit.co.jp/talk/v1/smalltalk', params)

        # print(response['choices'][0]['text'])
        context = {
            'response': response.json()['results'][0]['reply'],
            'input_text': input_text,
        }
        return render(request, 'index.html', context)