from MainGameAI import BattleshipAI
from Graph import plot
from random import randint

def train():
    plot_scores = []
    plot_mean_scores = []
    total_score = 0
    record = 9
    game = BattleshipAI()
    games = 0
    while True:
        Rarray = [0 for x in range(9)]
        x = randint(0,8)
        Rarray[x] = 1
        reward, done, score = game.Gamer(Rarray)

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
    train()