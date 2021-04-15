import os, re
from os.path import join, dirname
from dotenv import load_dotenv
from slackbot.bot import respond_to
import requests

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.environ.get("WEATHER_API_KEY")
TODAY_API_ENDPOINT = f"http://api.weatherstack.com/current?access_key={API_KEY}"
FORECAST_API_ENDPOINT = f"http://api.weatherstack.com/forecast?access_key={API_KEY}"

WEATHER_CODE = {
  113: "快晴",
  116: "所により曇り",
  119: "曇り",
  122: "本曇り",
  143: "もや",
  176: "近くで所により雨",
  179: "近くで所により雪",
  182: "近くで所によりみぞれ",
  185: "近くで所により着氷性の霧雨",
  200: "近くで雷の発生",
  227: "吹雪",
  230: "猛吹雪",
  248: "霧",
  260: "着氷性の霧",
  263: "所により霧雨",
  266: "霧雨",
  281: "着氷性の霧雨",
  284: "強い着氷性の霧雨",
  293: "所により弱い雨",
  296: "弱い雨",
  299: "時々穏やかな雨",
  302: "穏やかな雨",
  305: "時々大雨",
  308: "大雨",
  311: "着氷性の弱い雨",
}

# 天気による一言
def weather_comment_maker(code):
  if code == 113:
    return "天気がいいので一緒にお出かけしませんか？"
  elif code == 200:
    return "わたし雷きらいだなぁ＞＜"
  elif code in [116, 119, 122]:
    return "曇りの日はアロマキャンドルを炊くといいよ！"
  elif code in [179, 227,230]:
    return "雪を見に行きたいな！"
  elif code in [143, 248, 260]:
    return "交通事故に気をつけてね・・・！"
  return "傘を忘れないようにね！"

# UV指数による一言
def uv_index_comment_maker(index):
  if index in [0, 1]:
    return "弱い"
  elif index in [2, 3, 4]:
    return "中程度"
  elif index in [5, 6]:
    return "強い"
  elif index in [7, 8, 9]:
    return "非常に強い"
  return "極端に強い"

# 日付に関する一言
def date_maker(match):
  if len(match) == 2:
    return "今日"
  elif len(match) == 3:
    return match[0] if match[0] != "明日" else "今日"

# 今日の天気情報を取得する
def get_today_weather(capital):
  return requests.get(f"{TODAY_API_ENDPOINT}&query={capital}").json()

# 明日の天気情報を取得する
def get_tomorrow_weather(match):
  if match[0].startswith("明日"):
    return requests.get(f"{FORECAST_API_ENDPOINT}&query={match[1]}&forecast_days=1&hourly=0").json()

  # 条件に当てはまらないものは今日の天気を返す
  return get_today_weather(match[1])

@respond_to('の天気を教えて')
def weather(message):
  mes = message.body["text"]
  match = re.findall('[^の]+', mes)

  # 都市名が空の場合
  if len(match) == 1:
    message.reply("英語で都市名を教えてね＞＜")
    return None

  # 天気APIから指定した都市の現在の天気を取得
  weather_data = []
  if len(match) == 2:
    weather_data = get_today_weather(match[0])
  elif len(match) == 3:
    weather_data = get_tomorrow_weather(match)

  # APIがエラーの場合
  if "success" in weather_data:
    message.reply("都市名が間違っているかも＞＜")
    return None

  # APIから取得した内容
  city = weather_data["request"]["query"]
  weather_code = weather_data["current"]["weather_code"]
  weather_status = WEATHER_CODE[weather_code]
  temp = weather_data["current"]["temperature"]
  uv_index = weather_data["current"]["uv_index"]

  # 天気に関するひとこと
  weather_comment = weather_comment_maker(weather_code)

  # UV指数に関するコメント
  uv_index_comment = uv_index_comment_maker(uv_index)

  # 日付に関するコメント
  date_comment = date_maker(match)

  message.reply(f"{date_comment}の{city}の天気は、{weather_status}です！\n気温は{temp}で、UV指数は{uv_index_comment}です！\n{weather_comment}")
