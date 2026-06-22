import pytest
from logic_utils import check_guess


class TestCheckGuess:
    """Test suite for check_guess function."""

    # Win cases
    def test_winning_guess(self):
        outcome, message = check_guess(50, 50, "Normal")
        assert outcome == "Win"
        assert message == "🎉 Correct!"

    def test_winning_guess_easy_mode(self):
        outcome, message = check_guess(10, 10, "Easy")
        assert outcome == "Win"
        assert message == "🎉 Correct!"

    def test_winning_guess_hard_mode(self):
        outcome, message = check_guess(25, 25, "Hard")
        assert outcome == "Win"
        assert message == "🎉 Correct!"

    def test_winning_guess_edge_case_one(self):
        outcome, message = check_guess(1, 1, "Normal")
        assert outcome == "Win"
        assert message == "🎉 Correct!"

    # Too High cases
    def test_guess_too_high(self):
        outcome, message = check_guess(60, 50, "Normal")
        assert outcome == "Too High"
        assert message == "📈 Go LOWER!"

    def test_guess_much_higher(self):
        outcome, message = check_guess(100, 10, "Normal")
        assert outcome == "Too High"
        assert message == "📈 Go LOWER!"

    def test_guess_too_high_hard_mode(self):
        outcome, message = check_guess(40, 25, "Hard")
        assert outcome == "Too High"
        assert message == "📈 Go LOWER!"

    # Too Low cases
    def test_guess_too_low(self):
        outcome, message = check_guess(40, 50, "Normal")
        assert outcome == "Too Low"
        assert message == "📉 Go HIGHER!"

    def test_guess_much_lower(self):
        outcome, message = check_guess(10, 100, "Normal")
        assert outcome == "Too Low"
        assert message == "📉 Go HIGHER!"

    def test_guess_too_low_hard_mode(self):
        outcome, message = check_guess(10, 25, "Hard")
        assert outcome == "Too Low"
        assert message == "📉 Go HIGHER!"

    # Out of bounds tests (difficulty-based validation)
    def test_guess_out_of_bounds_too_high_normal(self):
        outcome, message = check_guess(101, 50, "Normal")
        assert outcome == "Invalid"
        assert "must be between" in message

    def test_guess_out_of_bounds_too_low_normal(self):
        outcome, message = check_guess(0, 50, "Normal")
        assert outcome == "Invalid"
        assert "must be between" in message

    def test_guess_out_of_bounds_easy_mode_high(self):
        outcome, message = check_guess(21, 15, "Easy")
        assert outcome == "Invalid"
        assert "must be between" in message

    def test_guess_out_of_bounds_hard_mode_low(self):
        outcome, message = check_guess(0, 25, "Hard")
        assert outcome == "Invalid"
        assert "must be between" in message

    # Decimal rejection tests
    def test_decimal_guess_rejected(self):
        outcome, message = check_guess(50.5, 50, "Normal")
        assert outcome == "Invalid"
        assert "Decimals not allowed" in message

    def test_decimal_guess_point_one(self):
        outcome, message = check_guess(50.1, 50, "Normal")
        assert outcome == "Invalid"
        assert "Decimals not allowed" in message

    def test_decimal_guess_point_nine(self):
        outcome, message = check_guess(49.9, 50, "Normal")
        assert outcome == "Invalid"
        assert "Decimals not allowed" in message

    def test_float_whole_number_allowed(self):
        outcome, message = check_guess(50.0, 50, "Normal")
        assert outcome == "Win"
        assert message == "🎉 Correct!"

    def test_float_whole_number_too_high(self):
        outcome, message = check_guess(60.0, 50, "Normal")
        assert outcome == "Too High"
        assert message == "📈 Go LOWER!"

    # Parameterized test for multiple scenarios with difficulty
    @pytest.mark.parametrize("guess,secret,difficulty,expected_outcome", [
        (15, 15, "Easy", "Win"),
        (50, 50, "Normal", "Win"),
        (25, 25, "Hard", "Win"),
        (1, 1, "Normal", "Win"),
        (20, 15, "Easy", "Too High"),
        (100, 50, "Normal", "Too High"),
        (30, 40, "Hard", "Too Low"),
        (1, 50, "Normal", "Too Low"),
    ])
    def test_check_guess_parametrized(self, guess, secret, difficulty, expected_outcome):
        outcome, _ = check_guess(guess, secret, difficulty)
        assert outcome == expected_outcome

    # Boundary tests for each difficulty
    def test_easy_lower_boundary(self):
        outcome, _ = check_guess(1, 15, "Easy")
        assert outcome == "Too Low"

    def test_easy_upper_boundary(self):
        outcome, _ = check_guess(20, 15, "Easy")
        assert outcome == "Too High"

    def test_normal_lower_boundary(self):
        outcome, _ = check_guess(1, 50, "Normal")
        assert outcome == "Too Low"

    def test_normal_upper_boundary(self):
        outcome, _ = check_guess(100, 50, "Normal")
        assert outcome == "Too High"

    def test_hard_lower_boundary(self):
        outcome, _ = check_guess(1, 25, "Hard")
        assert outcome == "Too Low"

    def test_hard_upper_boundary(self):
        outcome, _ = check_guess(50, 25, "Hard")
        assert outcome == "Too High"
