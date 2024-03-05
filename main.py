import discord
from discord import Intents
from googletrans import Translator
import os
import time

TOKEN = ''
intents = discord.Intents.all()
client = discord.Client(intents=intents)

translator = Translator()


@client.event
async def on_ready():
  print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
  print(message.content)
  if message.author == client.user:
    return
  elif message.content.startswith('!help'):
    help_message = (
        "**English:** !translate [source lang] [destination lang] [message] \n"
        "!autotranslate [destination lang] [message]\n\n"
        "**French:** !translate [langue source] [langue destination] [message] \n"
        "!autotranslate [langue destination] [message]\n\n"
        "**Spanish:** !translate [idioma de origen] [idioma de destino] [mensaje] \n"
        "!autotranslate [idioma de destino] [mensaje]\n\n"
        "**Russian:** !translate [исходный язык] [целевой язык] [сообщение] \n"
        "!autotranslate [целевой язык] [сообщение]\n\n"
        "**Mandarin Chinese:** !translate [源语言] [目标语言] [消息] \n"
        "!autotranslate [目标语言] [消息]\n\n"
        "**Korean:** !translate [원본 언어] [대상 언어] [메시지] \n"
        "!autotranslate [대상 언어] [메시지]\n\n"
        "**German:** !translate [Ausgangssprache] [Zielsprache] [Nachricht] \n"
        "!autotranslate [Zielsprache] [Nachricht]\n!languages to see all supported languages."
    )

    await message.channel.send(help_message)
  elif message.content.startswith('!languages'):
    await message.channel.send({
        'af': 'afrikaans',
        'sq': 'albanian',
        'am': 'amharic',
        'ar': 'arabic',
        'hy': 'armenian',
        'az': 'azerbaijani',
        'eu': 'basque',
        'be': 'belarusian',
        'bn': 'bengali',
        'bs': 'bosnian',
        'bg': 'bulgarian',
        'ca': 'catalan',
        'ceb': 'cebuano',
        'ny': 'chichewa',
        'zh-cn': 'chinese (simplified)',
        'zh-tw': 'chinese (traditional)',
        'co': 'corsican',
        'hr': 'croatian',
        'cs': 'czech',
        'da': 'danish',
        'nl': 'dutch',
        'en': 'english',
        'eo': 'esperanto',
        'et': 'estonian',
        'tl': 'filipino',
        'fi': 'finnish',
        'fr': 'french',
        'fy': 'frisian',
        'gl': 'galician',
        'ka': 'georgian',
        'de': 'german',
        'el': 'greek',
        'gu': 'gujarati',
        'ht': 'haitian creole',
        'ha': 'hausa',
        'haw': 'hawaiian',
        'iw': 'hebrew',
        'he': 'hebrew',
        'hi': 'hindi',
        'hmn': 'hmong',
        'hu': 'hungarian',
        'is': 'icelandic',
        'ig': 'igbo',
        'id': 'indonesian',
        'ga': 'irish',
        'it': 'italian',
        'ja': 'japanese',
        'jw': 'javanese',
        'kn': 'kannada',
        'kk': 'kazakh',
        'km': 'khmer',
        'ko': 'korean',
        'ku': 'kurdish (kurmanji)',
        'ky': 'kyrgyz',
        'lo': 'lao',
        'la': 'latin',
        'lv': 'latvian',
        'lt': 'lithuanian',
        'lb': 'luxembourgish',
        'mk': 'macedonian',
        'mg': 'malagasy',
        'ms': 'malay',
        'ml': 'malayalam',
        'mt': 'maltese',
        'mi': 'maori',
        'mr': 'marathi',
        'mn': 'mongolian',
        'my': 'myanmar (burmese)',
        'ne': 'nepali',
        'no': 'norwegian',
        'or': 'odia',
        'ps': 'pashto',
        'fa': 'persian',
        'pl': 'polish',
        'pt': 'portuguese',
        'pa': 'punjabi',
        'ro': 'romanian',
        'ru': 'russian',
        'sm': 'samoan',
        'gd': 'scots gaelic',
        'sr': 'serbian',
        'st': 'sesotho',
        'sn': 'shona',
        'sd': 'sindhi',
        'si': 'sinhala',
        'sk': 'slovak',
        'sl': 'slovenian',
        'so': 'somali',
        'es': 'spanish',
        'su': 'sundanese',
        'sw': 'swahili',
        'sv': 'swedish',
        'tg': 'tajik',
        'ta': 'tamil',
        'te': 'telugu',
        'th': 'thai',
        'tr': 'turkish',
        'uk': 'ukrainian',
        'ur': 'urdu',
        'ug': 'uyghur',
        'uz': 'uzbek',
        'vi': 'vietnamese',
        'cy': 'welsh',
        'xh': 'xhosa',
        'yi': 'yiddish',
        'yo': 'yoruba',
        'zu': 'zulu',
    })
  if message.content.startswith('!translate'):
    _, source_lang, target_lang, *text = message.content.split()

    try:

      translation = translator.translate(' '.join(text),
                                         src=source_lang,
                                         dest=target_lang)

      await message.channel.send(
          f'Translation from {source_lang} to {target_lang}:\n{translation.text}'
      )

    except Exception as e:
      print(f'Error during translation: {e}')
      await message.channel.send(
          f'Error during translation. Please check your input and try again. Error: {e}'
      )

  elif message.content.startswith('!autotranslate'):
    _, target_lang, *text = message.content.split()

    try:
      detection = translator.detect(' '.join(text))
      translation = translator.translate(' '.join(text), dest=target_lang)

      await message.channel.send(
          f'Translation from {detection.lang} to {target_lang}:\n{translation.text}'
      )

    except Exception as e:
      print(f'Error during auto-translation: {e}')
      await message.channel.send(
          f'Error during auto-translation. Please check your input and try again. Error: {e}'
      )


client.run(TOKEN)
