import src.constants as const
import src.Match as Match
import utility_MakeBoards as BoardMaker

def test_Match_construction():
    match_default = Match.Match()
    assert(match_default.column_selection == 0)
    assert(match_default.state == const.MatchState.PLAYING)
    assert(match_default.player_turn == const.PlayerTurn.RED)

    match_other_player = Match.Match(const.PlayerTurn.YELLOW)
    assert(match_other_player.player_turn == const.PlayerTurn.YELLOW)


def test_column_changes_match_playing():
    match = Match.Match()
    match.board = BoardMaker.make_board_playing_with_full_columns()
    assert(match.column_selection == 0)

    match.column_next()
    assert(match.column_selection == 2)

    match.column_next()
    assert(match.column_selection == 3)

    match.column_next()
    assert(match.column_selection == 5)

    match.column_next()
    assert(match.column_selection == 6)

    match.column_next()
    assert(match.column_selection == 0)

    match.column_next()
    assert(match.column_selection == 2)

    match.column_previous()
    assert(match.column_selection == 0)
    
    match.column_previous()
    assert(match.column_selection == 6)
    
    match.column_previous()
    assert(match.column_selection == 5)
    
    match.column_previous()
    assert(match.column_selection == 3)
    
    match.column_previous()
    assert(match.column_selection == 2)
    
    match.column_previous()
    assert(match.column_selection == 0)