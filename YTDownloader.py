import os
try:
  import pytube, youtube_dl, colorama
except:
  os.system("pip install pytube youtube_dl colorama")
import subprocess , sys , time , string, os
from pytube import YouTube
from colorama import *

print('[+] Checking For Requirement . . .')
BA = ("""

╔══════╗  ╔════════╗      ╔═╗
╚════╗ ║  ║ ╔════╗ ║     ╔  ║
    ╔╝╔╝  ║ ║ ╔╗ ║ ║   ╔═╝  ║
   ╔╝╔╝   ╚╗  ╔╗  ╔╝   ╚═╝  ║  
  ╔╝╔╝     ╚═╗  ╔═╝         ╚═╗
  ╚═╝        ╚══╝     ╚══════╝\n""")
#EXIT Function To exit after finishing.
def EXIT():
  os.system("cls")
  exit()

username = os.getlogin()
#Intro.
while 1:
  print('YOUTUBE DOWNLOADER BY:')
  print(Fore.BLUE+BA+Fore.RESET)
  print(f'[{Fore.BLUE}+{Fore.RESET}] This is a Script to Download Video, And Mp3 From Any URL at Youtube.')
  url = input(f'[{Fore.RED}>{Fore.RESET}] Enter a URL: ')

  #URL Info.
  vid = YouTube(url)
  print()
  print(f'[{Fore.BLUE}+{Fore.RESET}] Video Title   > '+vid.title)
  print(f'\n[{Fore.BLUE}+{Fore.RESET}] Select Number:')
  print(f'[{Fore.GREEN}-{Fore.RESET}] 0 - Download Video().')
  print(f'[{Fore.GREEN}-{Fore.RESET}] 1 - Download Audio().')
  print(f'[{Fore.GREEN}-{Fore.RESET}] 2 - EXIT()')
  down = (input(f'[{Fore.RED}>{Fore.RESET}] '))

  #Thumbnail Download command for CMD + Display DIR After downloading.
  title = vid.title
  newtitle = title.replace(' ', '_')
  desktop = (f"C:\\Users\\{username}\\Desktop\\{newtitle}.{vid.thumbnail_url[-3:]}")
  thumb = (f"curl {vid.thumbnail_url} --output {desktop}")

  #To input Only [0], [1], [2].
  while down != '0' and down != '1' and down != '2':
    print(f'[{Fore.YELLOW}?{Fore.RESET}] Please input [0], [1], [2] Only.')
    down = (input(f'[{Fore.RED}>{Fore.RESET}] '))

  # 0 = Download Video.
  try:
    if down == '0':
      ydl_opts = {
        'outtmpl' : f'C:\\Users\\{username}\\Desktop\\{vid.title}',
        'noplaylist' : True,
      }
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
      print(f'[{Fore.BLUE}+{Fore.RESET}] Video has been saved in Desktop')


    # 1 = Download Audio AS MP3.
    elif down == '1':
      ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'outtmpl': f"C:\\Users\\{username}\\Desktop\\{vid.title}.mp3",
        'postprocessors':
        [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
      }
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
      print(f'[{Fore.BLUE}+{Fore.RESET}] Video has been saved in Desktop')
    elif down == '2':
      EXIT()
  except youtube_dl.utils.DownloadError:
    print("Unable To Download This Video Data.")
  time.sleep(3)
  os.system("cls")
# <!-- Null -->
