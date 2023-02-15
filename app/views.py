from django.shortcuts import render
from django.views.generic import TemplateView

import openai
import os
import environ


env = environ.Env()
env.read_env(os.path.join(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))), '.env'))

# 対話用のプロンプトエンジニアリングが必要
class IndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = {
            'response': "返信をここに表示します",
        }
        return render(request, 'index.html', context)

    def post(self, request, *args, **kwargs):
        openai.api_key = env('GPT3_KEY')
        input_text = request.POST['sentence']
        engine_type = request.POST['engine type']

        # 対話用のプロンプトを仕込む
        response = openai.Completion.create(
            engine=engine_type,
            prompt=input_text,
            temperature=0.7,
            max_tokens=100,
            top_p=1,
            frequency_penalty=1,
            presence_penalty=0,

        )

        print(response['choices'][0]['text'])
        context = {
            'response': response['choices'][0]['text'],
            'input_text': input_text,
        }
        return render(request, 'index.html', context)