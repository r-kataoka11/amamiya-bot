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

@respond_to('可愛い|かわいい')
def kawaii(message):
  message.react('kissing_heart')
  message.reply('ありがと:kissing_heart:')

@listen_to('おはよう')
def hello(message):
  message.reply('おはよう！')

@listen_to('LINE', re.IGNORECASE)
def line(message):
  message.reply('既読スルーしてごめんね！')

@listen_to('筋肉')
def muscle(message):
  message.reply('素敵な大胸筋！！')

@default_reply
def default_handler(message):
  message.reply('ちょっとよくわからなかったです＞＜!')


