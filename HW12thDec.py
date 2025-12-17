mi = ["Rohit Sharma","Ishan Kishan","Suryakumar Yadav","Tilak Verma","Hardik pandya",
"Will jacks","Mitchell Santer","Jasprit Bumrah","Deepak Chahar","Trent Boult","Karn Sharma"]

pbks = ["Shreyas Iyer","Prabhsimran Singh","Nehal Wadhera","Glen Maxwell","Marcus Stoinis",
" Shashank Singh","Harpreet Brar","Marco Jansen","Arshdeep Singh","Yuzvendra Chahal","Lockie Ferguson"]

rcb = ["Virat Kohli","Phil Salt","Rajat Patidar","Liam Livingstone","Tim David","Krunal Pandya","Romario Shepherd",
"Josh Hazelwood","Bhuvneshwar Kumar","Yash Dayal","Suyash Sharma"]

gt = ["Shubman Gill","Jos Buttler","Sai Sudarsan","Shahrukh Khan","Rahul Tewatia","Washington Sundar",
"Rashid Khan","Kagiso Rabada","Mohammed Siraj","Prasidh Krishna","R Sai Kishore"]

superfours = [mi,pbks,rcb,gt]

print(superfours)  # All 4 teams

print(superfours[3])  # GT team
print(superfours[:2])  # MI + PBKS
print(superfours[2:3])  # RCB only

print(superfours[1][1][2])  # 'a' from 'Prabhsimran Singh'

print(superfours[1][1])  # 'Prabhsimran Singh'
print(superfours[3][0])  # 'Shubman Gill'
print(superfours[2][5])  # 'Krunal Pandya'
print(superfours[2][0][0:5])  # 'Virat'
print(superfours[2][0].split()[0])  # 'Virat'
print(superfours[2][0][6:11])  # 'Kohli'
print(superfours[2][0].split()[1])  # 'Kohli'

for team in superfours:
    first_names = [player.split()[0] for player in team]
    print(first_names)  # First names of team

    for team in superfours:
        last_names = [player.split()[1] for player in team]
        print(last_names)  # Last names of team

mi.append("Ajinkya Gode")  # Add new player to MI
mi[0] =  "Ajinkya Gode"  # Replace first player with Ajinkya Gode
print(mi)  # Updated MI

superfours[0].append("Ajinkya Gode")  # Append via superfours reference
print(superfours[0])  # MI updated via superfours

for player in mi:
    count_a = player.count('a')
    print(f"{player}: {count_a} 'a's")  # Count 'a' in each MI player

for player in rcb:
    count_a = player.count('a')
    print(f"{player}: {count_a} 'a's")  # Count 'a' in each RCB player

for team in superfours:
    print(team)  # Print entire team

for team in superfours:
    for player in team:
        print(player)  # Print each player

print(superfours[3])  # GT before removal
superfours[3] = superfours[3][:-1]  # Remove last player from GT
print(superfours[3])  # GT after removal



# Count 'a' in each player of MI
for player in mi:
    count_a = player.count('a')
    print(f"{player}: {count_a} 'a's")  # prints player name + number of small 'a'

print()  # blank line to separate outputs

# Count 'a' in each player of RCB
for player in rcb:
    count_a = player.count('a')
    print(f"{player}: {count_a} 'a's")  # prints player name + number of small 'a' 