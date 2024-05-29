print('Automatic Lyric Script')
print('By Mieko Hikari')

import syncedlyrics
import os
import glob
import cutlet;
import time;
import re;

directory = r'C:\Users\Aria\OneDrive\Music'
print ('Directory set to ' + directory)

os.chdir(directory);

mp3s = glob.glob('*.mp3')

print('Found ' + str(len(mp3s)) + ' mp3 files.')

katsu = cutlet.Cutlet()
katsu.use_foreign_spelling = True

for mp3 in mp3s:
    songName = os.path.splitext(mp3)[0]
    print('Checking if lyrics exist for "' + songName + '"...')
    
    if os.path.isfile(songName + '.lrc'):
        print('Lyrics already exist for "' + songName + '". Skipping...')
        continue
    else:
        lyrics = syncedlyrics.search(songName, save_path=directory + "\\" + songName + ".lrc")
        time.sleep(5)
        if lyrics is None:
            print('No lyrics found for "' + songName + '".')
        else:
            lines = lyrics.split('\n')
            romanized = []

            for line in lines:
                match = re.match(r'(\[\d{2}:\d{2}\.\d{2}\])\s*(.*)', line)

                if match:
                    timestamp, lyric = match.groups()
                    romanized_lyric = katsu.romaji(lyric)
                    romanized_line = timestamp + ' ' + romanized_lyric
                    romanized.append(romanized_line)
                else:
                    romanized.append(line)

            with open(directory + "\\" + songName + ".lrc", 'w', encoding='utf-8') as f:
                f.write('\n'.join(romanized))
                print('Lyrics saved for "' + songName + '".')
        print('')

print('Processed ' + str(len(mp3s)) + ' mp3 files.')