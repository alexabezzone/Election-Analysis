#The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who receieved votes
# 3. The percentage oc votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote. 

import csv
dir(csv)

file_to_load = 'Data_Bootcamp/Module_3/Election-Analysis/Resources/election_results.csv'

with open(file_to_load) as election_data:
    print(election_data)
