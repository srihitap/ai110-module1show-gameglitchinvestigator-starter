from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# Tests targeting the swapped-message fix: "Too High" must say go LOWER,
# "Too Low" must say go HIGHER.
def test_too_high_message_says_lower():
    _, message = check_guess(80, 50)
    assert "LOWER" in message
    assert "HIGHER" not in message

def test_too_low_message_says_higher():
    _, message = check_guess(20, 50)
    assert "HIGHER" in message
    assert "LOWER" not in message


# Test targeting the new game fix: after a win, check_guess must work
# correctly with a fresh secret (game logic is stateless across restarts).
def test_new_game_check_guess_works_after_win():
    outcome, _ = check_guess(42, 42)
    assert outcome == "Win"

    outcome, message = check_guess(10, 80)
    assert outcome == "Too Low"
    assert "HIGHER" in message
