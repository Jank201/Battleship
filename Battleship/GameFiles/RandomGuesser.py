from Graph import plot
from random import randint
import numpy as np
from MainGameMath import BattleshipAI
from MainGameMath import BOARDSQUARES

def guesser():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 9
    game = BattleshipAI()
    games = 0
    while True:
        Rarray = np.array([0,0])
        x = randint(0,BOARDSQUARES-1)
        y = randint(0,BOARDSQUARES-1)
        Rarray[0] = x
        Rarray[1] = y
        reward, done, score, hit = game.Gamer(Rarray)

        if done:
            games += 1
            game.reset()

            if score < record:
                record = score

            print('Game', games, 'Score', score, 'Record:', record)

            plot_scores.append(score)
            total_score += score
            mean_score = total_score / games
            plot_mean_scores.append(mean_score)
            plot(plot_scores, plot_mean_scores)

if __name__ == '__main__':
    guesser()