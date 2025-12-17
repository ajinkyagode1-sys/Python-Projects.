mi = ["Rohit Sharma","Ishan Kishan","Suryakumar Yadav","Tilak Verma","Hardik pandya",
      "Will jacks","Mitchell Santer","Jasprit Bumrah","Deepak Chahar","Trent Boult","Karn Sharma"]

pbks = ["Shreyas Iyer","Prabhsimran Singh","Nehal Wadhera","Glen Maxwell","Marcus Stoinis",
        "Shashank Singh","Harpreet Brar","Marco Jansen","Arshdeep Singh","Yuzvendra Chahal","Lockie Ferguson"]

rcb = ["Virat Kohli","Phil Salt","Rajat Patidar","Liam Livingstone","Tim David",
       "Krunal Pandya","Romario Shepherd","Josh Hazelwood","Bhuvneshwar Kumar","Yash Dayal","Suyash Sharma"]

gt = ["Shubman Gill","Jos Buttler","Sai Sudarsan","Shahrukh Khan","Rahul Tewatia",
      "Washington Sundar","Rashid Khan","Kagiso Rabada","Mohammed Siraj","Prasidh Krishna","R Sai Kishore"]

superfours = [mi, pbks, rcb, gt]


for i in range(len(superfours[0])):          # Iteration of MI Team 
    print(superfours[0][i])

for i in range(len(superfours[0])):          # Iteration of  Players
      player = superfours[0][i]
      print(player)
      for j in range(len(player)):           # Iteration of Characters
           print(player[j])





for i in range(len(superfours[1])):          # Iteration of PBKS  Team
     print(superfours[1][i])


for i in range(len(superfours[1])):          # Iteration of Players
    player = superfours[1][i]
    print(player)
    for j in range(len(player)):             # Iteration of Characters
        print(player[j])






for i in range(len(superfours[2])):         # Iteration of RCB Team 
     print(superfours[2][i])

for i in range(len(superfours[2])):         # Iteration of Players
     player = superfours[2][i]
     print(player)
     for j in range(len(player)):           # Iteration of Characters
          print(player[j])



for i in range(len(superfours[3])):         # Iteration of GT Team 
    print(superfours[3][i])


for i in range(len(superfours[3])):         # Iteration of Players 
        player = superfours[3][i]
        print(player)
        for j in range(len(player)):        # Iteration of Characters
            print(player[j])

