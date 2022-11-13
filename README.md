# IPL_TEAMS
## Problem Statement:-
In analyzing a team's performance, one of the methods used is to look at their past
Performance. In the image on your left you could see performance of the past 5
Matches for all IPL teams.<br>

![image](https://user-images.githubusercontent.com/69086016/201520023-b9100595-c68b-45c1-b5fa-50660f986d73.png)

### Objectives:-
1. Create a small data structure that holds details - Name of the team, points they have
earned and result of last 5 matches as per above image
2. Programmatically retrieve the teams that have 2 consecutive losses.
3. Generalize the same solution, so that we could get teams that have n consecutive
losses/wins.
4. Once the above is done, Calculate the average points of these filtered teams

### Implementation:-

**Step 1:** I have created the data structure to hold the each team data which includes teams name, points and the history of matches i.e. win and loss.<br>
**Step 2:** I have created the consecutive function to get data for teams which have exactly 2 consecutive losses by the creating iterative method of n teams. <br>
**Step 3:** I have now optimized consecutive function to get data for n consecutive wins or losses for each team by iterating.<br>
**Step 4:** After getting filtered teams. We will calculate the average point for same. <br>

### Result:-

#### THIS DATA WILL PRINT 2 CONSECUTIVE LOSSES

IPL Team Name: GT       
matches: [1, 1, 0, 0, 1]
Points:  20
Consecutive Loss : 2    

IPL Team Name: LSG      
matches: [1, 0, 0, 1, 1]
Points:  18
Consecutive Loss : 2

IPL Team Name: RR
matches: [1, 0, 1, 0, 0]
Points:  16
Consecutive Loss : 2

IPL Team Name: RCB
matches: [0, 1, 1, 0, 0]
Points:  14
Consecutive Loss : 2

IPL Team Name: SRH
matches: [1, 0, 0, 0, 0]
Points:  12
Consecutive Loss : 4

IPL Team Name: CSK
matches: [0, 0, 1, 0, 1]
Points:  8
Consecutive Loss : 2<br>
**Average of the list = 14.67**

#### THIS DATA WILL PRINT N  CONSECUTIVE WIN AND LOSS

IPL Team Name: GT
matches: [1, 1, 0, 0, 1]
Points:  20
Consecutive Loss : 2

IPL Team Name: LSG
matches: [1, 0, 0, 1, 1]
Points:  18
Consecutive Loss : 2

IPL Team Name: RR
matches: [1, 0, 1, 0, 0]
Points:  16
Consecutive Loss : 2

IPL Team Name: DC
matches: [1, 1, 0, 1, 0]
Pointa:  14
Consecutive Win : 2

IPL Team Name: RCB
matches: [0, 1, 1, 0, 0]
Points:  14
Consecutive Loss : 2

IPL Team Name: KKR
matches: [0, 1, 1, 0, 1]
Pointa:  12
Consecutive Win : 2

IPL Team Name: SRH
matches: [1, 0, 0, 0, 0]
Points:  12
Consecutive Loss : 4

IPL Team Name: CSK
matches: [0, 0, 1, 0, 1]
Points:  8
Consecutive Loss : 2

IPL Team Name: MI
matches: [0, 1, 0, 1, 1]
Pointa:  6
Consecutive Win : 2 <br>
**Average of the list = 13.33**

### Conclusion:-
We have successfully completed the problem statement by the preventing more time and space complexity. 

