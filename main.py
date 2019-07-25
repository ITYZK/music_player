import ctypes
import random
import os
import pygame
from mutagen import File
from mutagen.mp3 import MP3

pygame.mixer.init() 
class music_player():
    def load_music(self,music_path):
        music_list1=[]
        for p in os.listdir(music_path):
            p = p.split('.')
            if p[1] == 'mp3':
                 music_list1.append(p[0])
        #print(music_list1)
        return music_list1

    def play(self,music_name):
        play_path = "music\%s.mp3" % music_name
        
        print("正在播放 %s" % music_name)
        # ctypes.windll.winmm.mciSendStringW(r"open music\%s.mp3 aline s" % music_name, None, 0, None)
        # ctypes.windll.winmm.mciSendStringW(r"play s replay" , None, 0, None)
        pygame.mixer.music.load(play_path)
        pygame.mixer.music.play()
        #提取歌曲信息
        afile = File(play_path)
        
        if 'TPE1' in afile.tags.keys():
            author = afile.tags['TPE1'].text[0]  #作者
            title = afile.tags['TIT2'].text[0]   #标题
            print('作者：{}\n标题:{}'.format(author,title))
            lentime = MP3(play_path)
            print("歌曲时长：%.3f 分钟"%(lentime.info.length/60)) #获取歌曲时长
        else :
            print("暂无歌曲信息！")
    
    def pause(self):
        print("已暂停\n")
        pygame.mixer.music.pause()

    def unpause(self):
        print("继续播放\n")
        pygame.mixer.music.unpause()

    def stop(self):
        print("已停止播放\n")
        #ctypes.windll.winmm.mciSendStringW(r"stop s replay" , None, 0, None)
        pygame.mixer.music.stop()

if __name__ == "__main__":
    music_path='.\music'
    m = music_player()
    m_list = m.load_music(music_path)
    music_name = random.choice(m_list)
    m.play(music_name)
    while(True):
        ms = input("\n1.停止 2.切歌 3.暂停 4.继续 0.退出(请输入序号)：")
        if ms == '1':
            m.stop()
        elif ms == '2':
            music_name = random.choice(m_list)
            m.play(music_name)
        elif ms == '3':
            m.pause()
        elif ms == '4':
            m.unpause()
        elif ms == '0':
            break
       
       