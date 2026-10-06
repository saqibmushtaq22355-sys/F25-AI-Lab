"""Assertions for boundaries, repeated percepts, transitions and empty-room priority."""
from lab2_percepts import ClassroomAgent

def run_checks():
    a = ClassroomAgent()
    assert a.act(29, True) == (None, "COOL", True)
    assert a.act(29, True) == ("COOL", "COOL", False)
    assert a.act(26, True) == ("COOL", "IDLE", True)
    assert a.act(26, True) == ("IDLE", "IDLE", False)
    assert a.act(19, True) == ("IDLE", "WARM", True)
    assert a.act(29, False) == ("WARM", "ECO", True)
    print("All Lab 2 checks passed.")

if __name__ == "__main__": run_checks()
