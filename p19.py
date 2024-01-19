team=int(input("Enter the Number of teams:\n"))
round=1
totalMatch=0
while(team!=1):
    if(team%2==0):
        Match=team/2
        teamAdv=team/2
        
        print(f"Round {round}: Teams ={team},Matches={Match},and {teamAdv} teams advances.")
        round+=1
        team=teamAdv
        totalMatch+=Match
        
    else:
        Match=(team-1)/2
        teamAdv=((team-1)/2)+1
        
        print(f"Round {round}: Teams ={team},Matches={Match},and {teamAdv} teams advances.")
        round+=1
        team=teamAdv
        totalMatch+=Match
print(f"Total number of the matches : {totalMatch}")