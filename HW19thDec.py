Movies2025 = {}

d_cast = ["Ranveer Singh", "Akshay Khanna", "Sanjay Dutt","Sara Arjun"]
c_cast = ["Vicky Kaushal","Akshay Khanna","Diana Penty","Rashmika Mandanna"]
r_cast = ["Ajay Devgn","Vanni Kapoor","Riteish Deshmukh","Shruti Pandey"]
hf5_cast = ["Soundarya Sharma","Sonam Bajwa","Akshay Kumar","Chitrangada Singh"]


Movies2025["Dhurandar"] = d_cast
Movies2025["Chhava"] = c_cast
Movies2025["Raid 2"] = r_cast
Movies2025["HouseFull 5"] = hf5_cast




Movies2024 = {}

P_Cast = ["Allu Arjun","Rashmika Mandanna","Fahadh Faasil","Jagapathi Babu"]
K_Cast = ["Prabhas","Amitabh Bachchan","Kamal Haasan","Deepika Padukone"]
S_Cast = ["Rajkummar Rao","Shraddha Kapoor","Pankaj Tripathi","Abhishek Banerjee"]
TGoAT_Cast = ["Joseph Vijay","Prashanth","Prabhu Deva","Mohan"]

Movies2024["Pushpa: The Rule - Part 2"] = P_Cast
Movies2024["Kalki 2898 AD"] = K_Cast
Movies2024["Stree 2"] = S_Cast
Movies2024["The Greatest of All Time"] = TGoAT_Cast



Movies2023 = {}

SB_Cast = ["Vicky Kaushal","Fatima Sana Shaikh","Sanya Malhota","Sammy Jonas Heaney"]
A_Cast = ["Ranbeer Kapoor","Tripti Dimri","Rashmika Mandanna","Bobby Deol"]
PA_Cast = ["Shah Rukh Khan","Deepika Padukone","Salman Khan","John Abraham"]
F3_Cast = ["Richa Chadda","Varun Sharma","Manjot Singh","Ali Fazal"]

Movies2023["Sam Bahadur"] = SB_Cast
Movies2023["Animal"] = A_Cast
Movies2023["Pathaan"] = PA_Cast
Movies2023["Fukrey 3"] = F3_Cast



Movies2022 = {}


KGF_Cast = ["Yash","Sanjay Dutt","Raveena Tandon","Srinidhi Shetty"]
RRR_Cast = ["N.T. Rama Rao Jr.","Ram Charan","Ajay Devgn","Alia Bhatt"]
D2_Cast = ["Ajay Devgn","Akshay Khanna","Tabu","Shriya Saran"]
B_Cast = ["Ranbeer Kapoor","Alia Bhatt","Amitabh Bachchan","Shah Rukh Khan"]

Movies2022["KGF Chapter 2"] = KGF_Cast
Movies2022["RRR"] = RRR_Cast
Movies2022["Drishyam 2"] = D2_Cast
Movies2022["Brahmastra Part one : Shiva"] = B_Cast




All_Movies = {2025:Movies2025,2024:Movies2024,2023:Movies2023,2022:Movies2022}
# print(All_Movies)

actor = "Allu Arjun"

for year, movies in All_Movies.items():
    for movie, cast in movies.items():
        if actor in cast:
            print(year, "->", movie)


actor = "Rashmika Mandanna"

for year, movies in All_Movies.items():
    for movie, cast in movies.items():
        if actor in cast:
            print(year,"--->", movie)

actor = "Ranbeer Kapoor"

for year, movies in All_Movies.items():
    for movie, cast in movies.items():
        if actor in cast:
            print(year,"--->", movie)


actor = "Ajay Devgn"


for year, movies in All_Movies.items():
    for movie, cast in movies.items():
        if actor in cast:
            print(year, "->", movie)


actor = "Akshay Khanna"

for year, movies in All_Movies.items():
    for movie, cast in movies.items():
        if actor in cast:
            print(year, "->", movie)

actor = "Deepika Padukone"

for year, movies in All_Movies.items():
    for movie, cast in movies.items():
        if actor in cast:
            print(year, "->", movie)

actor = "Vicky Kaushal"

for year, movies in All_Movies.items():
    for movie, cast in movies.items():
        if actor in cast:
            print(year, "->", movie)

actor = "Shah Rukh Khan"

for year, movies in All_Movies.items():
    for movie, cast in movies.items():
        if actor in cast:
            print(year, "->", movie)

actor = "Akshay Kumar"

for year, movies in All_Movies.items():
    for movie, cast in movies.items():
        if actor in cast:
            print(year, "->", movie)

actor = "Sanjay Dutt"

for year, movies in All_Movies.items():
    for movie, cast in movies.items():
        if actor in cast:
            print(year, "->", movie)

actor = "Alia Bhatt"

for year, movies in All_Movies.items():
    for movie, cast in movies.items():
        if actor in cast:
            print(year, "->", movie)

actor = "Amitabh Bachchan"

for year, movies in All_Movies.items():
    for movie, cast in movies.items():
        if actor in cast:
            print(year, "->", movie)

actor = "Ranveer Singh"

for year, movies in All_Movies.items():
    for movie, cast in movies.items():
        if actor in cast:
            print(year, "->", movie)

actor = "Salman Khan"

for year, movies in All_Movies.items():
    for movie, cast in movies.items():
        if actor in cast:
            print(year, "->", movie)

actor = "Riteish Deshmukh"

for year, movies in All_Movies.items():
    for movie, cast in movies.items():
        if actor in cast:
            print(year, "->", movie)