import threading
import openai
import kivy
from kivy.app import App
from kivy.base import AppBase
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

Config.set('graphics', 'minimum_width', '400')
Config.set('graphics', 'minimum_height', '600')
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '600')


class ChatApp(App):
    def build(self):
        # создаем главный контейнер
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # добавляем заголовок
        title = TextInput(text='AI Chatbot', size_hint=(1, 0.1), font_size='24sp', readonly=True)
        layout.add_widget(title)

        # создаем текстовое поле с границей
        self.input = TextInput(text='', multiline=True, size_hint=(1, 0.8), font_size='16sp')

        layout.add_widget(self.input)

        # создаем кнопку отправки сообщения
        button = Button(text='Send', size_hint=(1, 0.1), font_size='16sp', background_color=[0.1, 0.5, 0.9, 1],
                        color=[1, 1, 1, 1])
        button.bind(on_press=self.on_button_press)
        layout.add_widget(button)

        return layout

    def on_button_press(self, instance):
        # получаем текст из текстового поля и отправляем запрос на сервер
        query = self.input.text.strip()
        if not query:
            return  # игнорируем пустые запросы
        self.input.text = f'You: {query}\n'
        response = self.get_response(query)

        # выводим ответ на экран
        self.input.text += f'Bot: {response}\n'

    def get_response(self, query):
        # делаем запрос к OpenAI API и получаем ответ
        openai.api_key = "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"
        prompt = f'Q: {query}\nA:'
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=2500,
            top_p=1.0,
            frequency_penalty=0.1,
            presence_penalty=0.1,
        )

        # возвращаем ответ
        return response["choices"][0]["text"].strip()


if __name__ == '__main__':
    ChatApp().run()

