import src.constants as const
import src.Match as Match

def test_Match_construction():
    match_default = Match.Match()
    assert(match_default.column_selection == 0)
    assert(match_default.state == const.MatchState.PLAYING)
    assert(match_default.player_turn == const.PlayerTurn.RED)

    match_other_player = Match.Match(const.PlayerTurn.YELLOW)
    assert(match_other_player.player_turn == const.PlayerTurn.YELLOW)
