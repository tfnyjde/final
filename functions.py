"""A collection of function for doing my project."""

from my_module.classes import Ninja 

"""Method to displays rank for ninja"""    
def nin_profile(self):
    profile = self.name + " is a " + self.rank + " from the " + self.clan
    return profile
"""Method to 'participate' in the chunin exams, return results and update ninja rank"""
def chunin_exam(self):
    results = random.choice(["passed", "failed"])
      

    if results == "passed":
        self.rank = self.rank.replace("genin", "chunin") 
        return self.name, "Promoted to :", self.rank 

    elif results == "failed":
        return self.name, " did not pass the chunin exam."

"""Method that randomly ninja instance to a team"""
def join_team(self):
    team_number = random.choice(["Team 7", "Team 8", "Team 10", "Team Guy"]) 
    self.team = self.team + team_number
    return self.name + " has joined " + self.team 

"""Method returns updated info after chunin exam is passed and ninja has joined team"""    
def update(self):
    if self.team != "":
        print(self.nin_profile(), "on", self.team)
    else:
        print(self.nin_profile())



   