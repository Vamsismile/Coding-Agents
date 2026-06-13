import pytest
from app import main
from io import StringIO
import sys


def test_main_runs_without_error(capsys):
    """Test that main() runs without raising an exception."""
    main()
    captured = capsys.readouterr()
    assert "Hello from dummy project!" in captured.out
