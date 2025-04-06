class Node:
    def __init__(self, vote, team):
        self.vote = vote
        self.team = team
    
    def __eq__(self, other):
        return self.vote == other.vote and self.team == other.team
    
    def __lt__(self, other):
        if self.vote > other.vote:
            return True
        elif self.vote < other.vote:
            return False
        else:
            return self.team < other.team


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        team_to_vote = {}
        for vote in votes:
            for i, team in enumerate(vote):
                if team not in team_to_vote:
                    team_to_vote[team] = [0] * n
                team_to_vote[team][i] += 1
        
        lst = [Node(tuple(vote), team) for team, vote in team_to_vote.items()]
        lst.sort()
        return ''.join([node.team for node in lst])
