from slackbot.bot import respond_to, listen_to, default_reply
import random
import re
from utils.slackbok_utils import only_super_user

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
@only_super_user
def kawaii(message):
  message.react('kissing_heart')
  message.reply('ありがと:kissing_heart:')

@respond_to('好き|すき|love', re.IGNORECASE)
@only_super_user
def love(message):
  message.react('kissing_heart')
  message.reply('私もだよ！:kissing_heart:')

@listen_to('おはよう')
def hello(message):
  message.reply('おはよう！')

@listen_to('りも開|rimokai', re.IGNORECASE)
def rimo_kai(message):
  text = random.choice(['えらいぞ〜！:emo_heart: ', '今日も一日頑張ろう！:heartpulse:'],)
  message.reply(text)

@listen_to('何か面白いこと言って|なにか面白いこと言って', )
def oyaji_gag(message):
  text = random.choice(['この焼き肉は　焼きにくい', 'この鶏肉は　取りにくい', 'ウクライナは　もう暗いな'],)
  message.reply(text)

@listen_to('りも終|rimoshu', re.IGNORECASE)
def rimo_shu(message):
  text = random.choice(['今日も一日お疲れ様！', '頑張ったね:otsukarecosta:', 'また明日:wave:'],)
  message.react('otukaresamadesita')
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


