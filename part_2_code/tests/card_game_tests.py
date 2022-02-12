import unittest
from unittest import result
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("clubs", 3)
        self.card2 = Card("diamonds", 2)
        self.card3 = Card("hearts", 1)
        self.cardgame = CardGame()
        self.cards = [self.card1, self.card2, self.card3]


    def test_card_has_suit(self):
        self.assertEqual("clubs", self.card1.suit)
    
    def test_card_has_value(self):
        self.assertEqual(2, self.card2.value)

    def test_check_for_ace_True(self):
        result = True
        expected = self.cardgame.check_for_ace(self.card3)
        self.assertEqual(result, expected)

    def test_check_for_ace_False(self):
        result = False
        expected = self.cardgame.check_for_ace(self.card2)
        self.assertEqual(result, expected)

    def test_highest_card(self):
        result = self.card1
        expected = self.cardgame.highest_card(self.card1, self.card2)
        self.assertEqual(result, expected)

    def test_cards_total(self):
        result = "You have a total of 1"
        expected = self.cardgame.cards_total(self.cards)
        self.assertEqual(result, expected)
    

    

    