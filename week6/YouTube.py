import pafy
import vlc
import time

url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
video = pafy.new(url)
best = video.getbest()
playurl = best.url

Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.play()

#timeout = time.time() + 3   # 3 seconds from now
#while True:
#    if time.time() > timeout:
#        player.stop()