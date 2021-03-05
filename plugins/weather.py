import os
from os.path import join, dirname
from dotenv import load_dotenv
from slackbot.bot import respond_to
import requests

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY = os.environ.get("WEATHER_API_KEY")
API_ENDPOINT = f"http://api.weatherstack.com/current?access_key={API_KEY}"

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

@respond_to('(.*)の天気を教えて')
def weather(message, capital=""):
  # 都市名が空の場合
  if capital == "":
    message.reply("英語で都市名を教えてね＞＜")
    return None

  # 天気APIから指定した都市の現在の天気を取得
  weather_data = requests.get(f"{API_ENDPOINT}&query={capital}").json()

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
  weather_comment = ""
  if weather_code == 113:
    weather_comment = "天気がいいので一緒にお出かけしませんか？"
  elif weather_code == 200:
    weather_comment = "わたし雷きらいだなぁ＞＜"
  elif weather_code in [116, 119, 122]:
    weather_comment = "曇りの日はアロマキャンドルを炊くといいよ！"
  elif weather_code in [179, 227,230]:
    weather_comment = "雪を見に行きたいな！"
  elif weather_code in [143, 248, 260]:
    weather_comment = "交通事故に気をつけてね・・・！"
  else:
    weather_comment = "傘を忘れないようにね！"

  # UV指数に関するコメント
  uv_index_comment = ""
  if uv_index in [0, 1]:
    uv_index_comment = "弱い"
  elif uv_index in [2, 3, 4]:
    uv_index_comment = "中程度"
  elif uv_index in [5, 6]:
    uv_index_comment = "強い"
  elif uv_index in [7, 8, 9]:
    uv_index_comment = "非常に強い"
  else:
    uv_index_comment = "極端に強い"

  message.reply(f"{city}の天気は、{weather_status}です！\n気温は{temp}で、UV指数は{uv_index_comment}です！\n{weather_comment}")
