import os
from os.path import join, dirname
from dotenv import load_dotenv
from slackbot.bot import Bot

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def only_super_user(func):
  super_user_list = [os.environ.get("SUPER_USER")]

  def wrapper(*args, **kwargs):
    if args[0]._body['user'] in super_user_list:
      return func(args[0], **kwargs)
    return None

  return wrapper
