from slackbot.bot import respond_to, listen_to, default_reply
import random
import re

@listen_to('疲れた|つかれた')
def tukareta(message):
  rand = random.randrange(2)
  if rand == 0:
    message.reply('どうしたの？頑張って！')
  else:
    message.reply('頑張り屋さんだね！')

@listen_to('頑張った|がんばった')
def ganbatta(message):
  message.reply('お疲れさま！')

@listen_to('スマブラ')
def smash_bro(message):
  message.react('smashbros')
  message.react('wa-i2')
  text = random.choice(['リングに上がってください:kissing_heart:', 'おみごとメテオ！'],)
  message.reply(text)

@respond_to('可愛い|かわいい')
def kawaii(message):
  message.react('kissing_heart')
  message.reply('ありがと:kissing_heart:')

@listen_to('おはよう')
def hello(message):
  message.reply('おはよう！')

@listen_to('りも開|rimokai', re.IGNORECASE)
def rimo_kai(message):
  text = random.choice(['労働してえらいぞ〜！:emo_heart: ', '今日も一日頑張ろう！:heartpulse:'],)
  message.reply(text)

@listen_to('LINE', re.IGNORECASE)
def line(message):
  message.reply('既読スルーしてごめんね！')

@listen_to('筋肉')
def muscle(message):
  text = random.choice(['素敵な大胸筋！！', 'はちきれそうな大胸筋、山みたいな僧帽筋、鎧みたいな大腿四頭筋'])
  message.reply(text)

@default_reply
def default_handler(message):
  message.reply('ちょっとよくわからなかったです＞＜!')


