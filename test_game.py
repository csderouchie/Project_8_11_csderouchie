import game
import pytest


def test_deal_cards():
    """Test that cards are properly being moved from the deck to a hand"""
    g = game.game(["A", "K", "Q", "J", "10"], chips=100)
    hand = []
    g.dealCards(hand, 2)
    assert hand == ["10", "J"]
    assert g.deck == ["A", "K", "Q"]
    g.dealCards(hand, 1)
    assert hand == ["10", "J", "Q"]
    assert g.deck == ["A", "K"]

def test_lose():
    """Test that chips and bet are correct after a loss"""
    g = game.game(["A", "K", "Q", "J", "10"], chips=100)
    g.bet = 100
    g.lose()
    assert g.chips == 100
    assert g.bet == 0

def test_win():
    g = game.game(["A", "K", "Q", "J", "10"], chips=100)
    """Test that chips and bet are correct after a win"""
    g.bet = 100
    g.win()
    assert g.chips == 300
    assert g.bet == 0

def test_splitPot():
    """Test that chips and bet are correct after a split"""
    g = game.game(["A", "K", "Q", "J", "10"], chips=100)
    g.bet = 100
    g.splitPot()
    assert g.chips == 200
    assert g.bet == 0

