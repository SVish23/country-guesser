import tkinter as tk
import pytest
from game import game_start

root = tk.Tk()
starting_window = tk.Frame(root,width=800,height=600)

def test_difficulty():
    assert game_start(root,"Easy",starting_window) == "Easy"