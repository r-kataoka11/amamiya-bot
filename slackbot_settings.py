# -*- coding:utf-8 -*-
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_TOKEN = os.environ.get("API_KEY")

default_reply = 'ちょっとよくわからなかったです＞＜'
