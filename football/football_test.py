import unittest
from players import Player, Quarterback
from possible_values import *
from game import Game
from random import randint, uniform, sample
from season import *

# TODO - some things you can add...


class FootballGameTest(unittest.TestCase):
    '''test the class'''
    def test_field_goal_made(self):
        teams = sample(team_names, k=2)
        game = Game(teams=teams)

        team_prev_points = game.score[teams[0]]
        game.field_goal(teams[0])
        team_post_points = game.score[teams[0]]
        self.assertEqual(team_post_points, team_prev_points + 3)

    def test_get_winner(self):
        teams = sample(team_names, k=2)
        game = Game(teams=teams)
        game.field_goal(teams[0])

        t1_points = game.score[teams[0]]
        t2_points = game.score[teams[1]]

        if t1_points >= t2_points:
            win, lose = teams
        else:
            lose, win = teams

        self.assertEqual((win,lose), game.get_winning_team())


class FootballPlayerTest(unittest.TestCase):
    '''Check the default values for Player and Quarterback
    yards=120, touchdowns=5, safety=1,
                 interceptions=0
    '''
    def test_default_player_yards(self):
        player = Player(name='Dude')
        self.assertEqual(player.yards, 120)

    def test_player_yards_set_to(self):
        player = Player(name='OtherDude', yards=150)
        self.assertEqual(player.yards, 150)

    def test_default_qb_interceptions(self):
        qb = Quarterback(name='FancyDude')
        self.assertEqual(qb.interceptions, 4)

    def test_default_qb_completed_passes(self):
        qb = Quarterback()
        self.assertEqual(qb.completed_passes, 20)

    def test_passing_score(self):
        qb = Quarterback()
        self.assertEqual((20 - (2 * 4)), qb.passing_score())


if __name__ == '__main__':
    unittest.main()
