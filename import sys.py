import sys
import time

import pygame as pg

class Player:

    def change_state(self, state: str, hyper_time: int):
        """
        棒人間の状態（normal or hyper）を切り替えるメソッド
        引数1 state：棒人間の状態 normal or hyper
        引数2 hyper_time：無敵時間
        """
        self.state = state
        self.hyper_life = hyper_time

    def update(self):
        

        if event.key == pg.K_RSHIFT: #右shiftを押したとき
            if score.score > 100: #scoreが100よりも大きいとき
                Player.change_state("hyper",500) #hyperモードに切り替える
                score.score -= 100 #scoreを-100

if Player.state == "hyper":
    score.score_up(1)  # 1点アップ

else: #normalのとき 
    Player.change_img(3, screen) # 棒人間がやられるエフェクト
    score.update(screen)
    pg.display.update()
    time.sleep(2)
    return

