import telebot, wikipedia, re

bot = telebot.TeleBot('5395052998:AAGM0ad5I_CmLACrK1h1vH2-h9pVKaG4q3c')

wikipedia.set_lang('en')

def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                    wikitext2=wikitext2 + x + '.'
            else:
                break
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)

        return wikitext2

    except Exception as e:
        return 'Can\'t find it'


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Send me any word, I will find it from Wikipedia')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))

bot.polling(none_stop=True, interval=0)
