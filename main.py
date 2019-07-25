import ctypes
import random
import os
import pygame

pygame.mixer.init() 
class music_player():
    def load_music(self,music_path):
        music_list1=[]
        for p in os.listdir(music_path):
            p = p.split('.')
            music_list1.append(p[0])
        return music_list1

    def play(self,music_name):
        
        print("正在播放 %s\n" % music_name)
        # ctypes.windll.winmm.mciSendStringW(r"open music\%s.mp3 aline s" % music_name, None, 0, None)
        # ctypes.windll.winmm.mciSendStringW(r"play s replay" , None, 0, None)
        pygame.mixer.music.load(r"music\%s.mp3" % music_name)
        pygame.mixer.music.play()
    
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
        ms = input("1.停止 2.切歌 3.暂停 4.继续 0.退出(请输入序号)：")
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
       
       