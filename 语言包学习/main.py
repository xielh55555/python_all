# import pyttsx3
# say1=pyttsx3.init()
# say1.say('''书愤

# 陆游〔宋代〕

# 早岁那知世事艰，中原北望气如山。
# 楼船夜雪瓜洲渡，铁马秋风大散关。
# 塞上长城空自许，镜中衰鬓已先斑。
# 出师一表真名世，千载谁堪伯仲间！''')
# say1.runAndWait()
# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[3].id) 
# engine.say('name')
# engine.runAndWait()
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
speaker.Speak('''书愤

''')


# for i in range(int(m)):
#         t = threading.Thread(target=tkkd)
#         threads.append(t)
#         time.sleep(.3)
#         threads[i].start()
