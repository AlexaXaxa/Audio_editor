"""
#угасание
awesome = do_it_over.fade_in(13000).fade_out(3000)
"""

from pydub import AudioSegment
from playsound import playsound
#progress bar
#from tqdm import tqdm

file = AudioSegment.from_mp3(input("Укажите путь к аудио в формате mp3: "))
dur = file.duration_seconds
print(dur)

def cut(aud, begi, endd):

    beg = aud[:int(begi)*1000]
    end = aud[(int(endd)*1000):]

    without = beg + end
    with_style = beg.append(end, crossfade=1500)
    return with_style

ursval = input("Что делать с аудио? Вырезать? Увеличить звук? Пропустить? (1/2/3) ")
if ursval== "1":
    result = cut(file, input("Начало: "), input("Конец: "))
elif ursval == "2":
    x = input("На сколько? ")
    result = file + x
elif ursval == "3":
    result = file

result.export("mashup.mp3", format="mp3")
print("Воспроизведение..")
playsound("mashup.mp3")
print("Complete")

