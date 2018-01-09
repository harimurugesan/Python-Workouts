import webbrowser
import random
import time
break_count = 0
total_breaks = 3
while (break_count < total_breaks):
    print("this program started in", time.ctime())
    time.sleep(10)
    print("take a break bro.chill out!!!")
    time.sleep(2)
    print("i'm playing a song for you")
    time.sleep(2)
    web = ["https://www.youtube.com/watch?v=5za6Rroz3bI","https://www.youtube.com/watch?v=3rPEWcY6Oww&t=50s","https://www.youtube.com/watch?v=k4yXQkG2s1E","https://www.youtube.com/watch?v=wTgrZE9RWNY","https://www.youtube.com/watch?v=RunYl3Q0SYI","https://www.youtube.com/watch?v=MubpNJAMu6c","https://www.youtube.com/watch?v=nCD2hj6zJEc"]
    webbrowser.open(random.choice(web))
    break_count += 1
