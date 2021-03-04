from slackbot.bot import respond_to
import random

@respond_to('じゃんけんしよ|ジャンケンしよ')
def janken_start(message):
  message.reply('いいよ！わたし強いからね:wink:')

@respond_to('ぐー|グー|ちょき|チョキ|ちー|チー|ぱー|パー')
def janken(message):
  hands = {
    'ぐー': 0,
    'グー': 0,
    'ちょき': 1,
    'チョキ': 1,
    'ちー': 1,
    'チー': 1,
    'ぱー': 2,
    'パー': 2
  }
  text = message._body['text']

  you = None
  match_count= 0

  # 0:グー 1:チョキ 2:パー
  for hand, value in hands.items():
    if hand in text:
      you = value
      match_count += 1

  if match_count > 1:
    message.reply('いっぱい出すのずるい！！！:rage:')
    return None

  me = random.randrange(3)
  hand_list = {
    0: ':punch:',
    1: ':v:',
    2: ':raised_hand:'
  }
  message.reply(hand_list[me])


  result = (you - me) % 3
  result_text = {
    0: 'あいこだね！',
    1: 'なんで負けたか明日までに考えといてください:wink:',
    2: 'くやしい！！！:rage:'
  }
  message.reply(result_text[result])
