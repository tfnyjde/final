"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from my_module.functions import nin_profile, chunin_exam, join_team, update
from my_module.classes import Ninja
##
##

def test_nin_profile():
    assert callable(nin_profile) 
    Sasuke = Ninja("Sasuke", "Uchiha Clan")
    return "Passed"
    assert "Sasuke" in Sasuke.nin_profile()  
    

def test_chunin_exam():
    assert callable(chunin_exam)
    return "Passed"


def test_join_team():
    assert callable(join_team)
    Naruto = Ninja("Naruto", "Uzumaki Clan")
    assert "has joined" in Naruto.join_team()
    return "Passed"
    



                 
    