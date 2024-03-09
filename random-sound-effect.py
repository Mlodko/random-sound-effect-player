import random
import threading
import time
import vlc
from pytube import YouTube

class AudioPlayer(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.player = None
        self.loop = True
        self.daemon = True

    def run(self):
        print("run function ran")
        try:
            yt = YouTube(self.url)
            stream = yt.streams.filter(only_audio=True).first()
            audio_url = stream.url
            instance = vlc.Instance('--quiet')
            self.player = instance.media_player_new()
            media = instance.media_new(audio_url)
            self.player.set_media(media)
        except Exception as e:
            print(f'Error: {e}')
            return

        while self.loop:
            if not self.player.is_playing():
                self.player.play()
            time.sleep(1)

    def stop(self):
        self.loop = False
        if self.player:
            self.player.stop()

#        : 'Snapchat',
def main():
    video_urls = {
        'Duck':                                 'https://www.youtube.com/watch?v=53JB7ryHAMc',
        'Bazinga':                              'https://www.youtube.com/watch?v=i2fy_ve0Wpw',
        'Car crash':                            'https://www.youtube.com/watch?v=aFuPrXOy9c0',
        'Boowomp':                              'https://www.youtube.com/watch?v=b4HT4QJnhmU',
        'Gnome':                                'https://www.youtube.com/watch?v=Ms6YzGIQ7IM',
        'Gordon spooky sound':                  'https://www.youtube.com/watch?v=1Nkdl-jFpCw',
        'Hello mario':                          'https://www.youtube.com/watch?v=IFpd0hZxfAI',
        'Drip Goku':                            'https://www.youtube.com/watch?v=uUM7K2-OlUk',
        'FNAF 2 noise':                         'https://www.youtube.com/watch?v=ssS4-2Q4NnU',
        'Knock':                                'https://www.youtube.com/watch?v=iX14fEzas8s',
        'What the dog doin':                    'https://www.youtube.com/watch?v=bmDdHk_X864',
        'Bite of 87':                           'https://www.youtube.com/watch?v=53ChkkMu39c',
        'Miguel':                               'https://www.youtube.com/watch?v=mgPuMj8JgfY',
        'Wii Sports Aww':                       'https://www.youtube.com/watch?v=hIa0nm0uNkY',
        'Sicko mode sound':                     'https://www.youtube.com/watch?v=bNOj6kC6TyQ',
        'Glass bottle':                         'https://www.youtube.com/watch?v=UZoOUG8ytV8',
        'Hello there':                          'https://www.youtube.com/watch?v=CEXAvpACHf0',
        'Toad sound':                           'https://www.youtube.com/watch?v=otsq1EVLNf4',
        'Gordon \'WHERE\'S THE LAMB SAUCE\'':   'https://www.youtube.com/watch?v=dMdRTXMnQt4',
        'James May \'cheese.\'':                'https://www.youtube.com/watch?v=yWzYtoo8imk',
        'Lego Yoda death ':                     'https://www.youtube.com/watch?v=l88OZsBVA_I',
        'Bababooey':                            'https://www.youtube.com/watch?v=rfsXvOFv6Ow',
        'Vector \'OH YEAH\'':                   'https://www.youtube.com/watch?v=pUQknRQ65vE',
        'Waltuh':                               'https://www.youtube.com/watch?v=ukpO3-vzg-0',
        'Taco bell bong':                       'https://www.youtube.com/watch?v=Of9yvKINITg',
        'Hamburger':                            'https://www.youtube.com/watch?v=HfnmnY7iyXg',
        'Bad to the bone':                      'https://www.youtube.com/watch?v=q0H6ujtM5gw',
        'Michael Jackson grunts':               'https://www.youtube.com/watch?v=W58McrIMgo0',
        'Huh':                                  'https://www.youtube.com/watch?v=Y7YamgSqJtU',
        'Cave sounds':                          'https://www.youtube.com/watch?v=JabG22Zl02I',
        'Wah!':                                 'https://www.youtube.com/watch?v=n8foumUixN4',
        'Jerma sounds':                         'https://www.youtube.com/watch?v=UVE4StUbSzs',
        'Among Us':                             'https://www.youtube.com/watch?v=nJrTQuqaAcw',
        'Goose honks':                          'https://www.youtube.com/watch?v=rieynIv6xVs',
        'Bing Chillin\'':                       'https://www.youtube.com/watch?v=xFPOdkFn0L0',
        'MR BEAAAAST':                          'https://www.youtube.com/watch?v=JeNlUqcdR78',
        'McDonalds beeping':                    'https://www.youtube.com/watch?v=40GZ1nT8QbY',
        'bunger':                               'https://www.youtube.com/watch?v=h-AEt08H8tc',
        'Mario screaming':                      'https://www.youtube.com/watch?v=wKW42dl6Enk',
        'Metal pipe falling':                   'https://www.youtube.com/watch?v=oZAGNaLrTd0',
        'Megalovania':                          'https://www.youtube.com/watch?v=y3utR7pge-A',
        'Goat scream':                          'https://www.youtube.com/watch?v=yuE5AxKoDy4',
    }
    must_haves = [
        'Metal pipe falling',
        'Goose honks',
        'Bad to the bone',
        'James May \'cheese.\'',
        'Miguel',
        'Bite of 87',
        'Knock',
        'Duck',
        'Car crash',
    ]

    # the lower bound of interval between videos in seconds
    LOWER_BOUND_BETWEEN = 30 * 60
    # the higher bound
    HIGHER_BOUND_BETWEEN = 60 * 60

    players = []

    # Firstly play snapchat
    player = AudioPlayer('https://www.youtube.com/watch?v=yuE5AxKoDy4')
    player.start()
    players.append(player)
    current_time = time.strftime("%Y/%m/%d %H:%M:%S")
    print(f'f"[{current_time}] Now playing:    Snapchat"')
    time.sleep(random.randint(LOWER_BOUND_BETWEEN, HIGHER_BOUND_BETWEEN))

    try:
        while True:
            if must_haves:
                title_index = random.randint(0, len(must_haves) - 1)
                title = must_haves[title_index]
                print(f'Chosen from must_haves: {title}')
                must_haves.pop(title_index)
            else:
                title = random.choice(video_urls.keys())
                print(f'Chosen from regular list: {title}')

            random_url = video_urls[title]
            video_urls.pop(title)

            player = AudioPlayer(random_url)
            player.start()
            players.append(player)

            current_time = time.strftime("%Y/%m/%d %H:%M:%S")
            print(f"[{current_time}] Now playing:    {title}")
            time.sleep(random.randint(LOWER_BOUND_BETWEEN, HIGHER_BOUND_BETWEEN))
   
    except KeyboardInterrupt:
        print("Program terminated")
        for player in players:
            player.stop()
        print(players)

if __name__ == '__main__':
    main()
