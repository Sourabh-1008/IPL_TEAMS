'''
We have used nested dictionary to store the data.
'''
iplTeamName = {
    "GT": {
        "points": 20,
        "matches": [1, 1, 0, 0, 1]},
    "LSG": {
        "points": 18,
        "matches": [1, 0, 0, 1, 1]},
    "RR": {
        "points": 16,
        "matches": [1, 0, 1, 0, 0]},
    "DC": {
        "points": 14,
        "matches": [1, 1, 0, 1, 0]},
    "RCB": {
        "points": 14,
        "matches": [0, 1, 1, 0, 0]},
    "KKR": {
        "points": 12,
        "matches": [0, 1, 1, 0, 1]},
    "PKBS": {
        "points": 12,
        "matches": [0, 1, 0, 1, 0]},
    "SRH": {
        "points": 12,
        "matches": [1, 0, 0, 0, 0]},
    "CSK": {
        "points": 8,
        "matches": [0, 0, 1, 0, 1]},
    "MI": {
        "points": 6,
        "matches": [0, 1, 0, 1, 1]}
}

# This function is used to get in consecutive element in the list with win and losses


def consecutiveData(data):
    s = ''.join(map(str, data))
    return max(map(len, s.split('1'))), max(map(len, s.split('0')))

# This function is used to get averages of points in the matches


def Average(lst):
    return sum(lst) / len(lst)


'''
To display the team names who have 2 consecutive losses by iterating each teams datas.
'''

# this lst is used to store all the poins of teams to get the average of the teams
lst = []
# iterating Ipl Team Name from the dictionary to get Name of T and Info - like status of win and Loss and matches points etc.
print('THIS DATA WILL PRINT 2 CONSECUTIVE LOSSES')
for teamName, info in iplTeamName.items():
    for key in info:  # iterating Ipl Team Name from the dictionary to featch points and matchs to get status of win and loss matches
        if 'matches' in key:  # In matches find out how much matches are win and loss
            # this consecutiveData functions will help us to get loss and win for each team
            loss, won = consecutiveData(info[key])
            if loss >= 2:  # this will show the 2 consecutive loss of the matches
                print("\nIPL Team Name:",  teamName)
                print(key + ':', info[key])
                print("Points: ", iplTeamName[teamName].get('points'))
                # the points of matches is add into the list
                lst.append(iplTeamName[teamName].get('points'))
                print("Consecutive Loss :", loss)

# this average function is used to calculate the average point for the filtered teams
average = Average(lst)
print("Average of the list =", round(average, 2))
print('------------------------------------------------------------------------------------------------------------------')

print('THIS DATA WILL PRINT N  CONSECUTIVE WIN AND LOSS')
n = 2  # user will put input how much consecutive match are filtereds
lst = []
# iterating Ipl Team Name from the dictionary to get Name of T and Info - like status of win and Loss and matches points etc.
for teamName, info in iplTeamName.items():
    for key in info:  # iterating Ipl Team Name from the dictionary to featch points and matchs to get status of win and loss matches
        if 'matches' in key:  # In matches find out how much matches are win and loss
            # the points of matches is add into the list
            loss, won = consecutiveData(info[key])
            if loss >= n:  # this will show the n consecutive loss of the matches
                print("\nIPL Team Name:",  teamName)
                print(key + ':', info[key])
                print("Points: ", iplTeamName[teamName].get('points'))
                lst.append(iplTeamName[teamName].get('points'))
                print("Consecutive Loss :", loss)
            elif won >= n:  # this will show the n consecutive win of the matches
                print("\nIPL Team Name:",  teamName)
                print(key + ':', info[key])
                print("Pointa: ", iplTeamName[teamName].get('points'))
                lst.append(iplTeamName[teamName].get('points'))
                print("Consecutive Win :", won)
# this average function is used to calculate the average point for the filtered teams
average = Average(lst)
print("Average of the list =", round(average, 2))
