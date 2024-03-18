#  -*- coding: UTF-8 -*-

# MindPlus
# Python
from pinpong.board import Board
from pinpong.libs.dfrobot_speech_synthesis import DFRobot_SpeechSynthesis_I2C


Board().begin()
p_gravitysynthesis = DFRobot_SpeechSynthesis_I2C()
p_gravitysynthesis.begin(p_gravitysynthesis.V1)
p_gravitysynthesis.set_voice(8)
p_gravitysynthesis.set_speed(5)
p_gravitysynthesis.set_tone(5)
p_gravitysynthesis.set_sound_type(p_gravitysynthesis.MALE)
p_gravitysynthesis.speak("你好")
