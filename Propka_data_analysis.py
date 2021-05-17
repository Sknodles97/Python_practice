# Intending to increase one's efficiency to analyze pqr or other various pka output files and compare them to literature data.
# Primary purpose is to effectively extract and prepare the data for further analysis.
# variable y = calculated for given protein
# variable x = Average lit value to compare against
# values extracted from PDB2PQR calculation output (propka file, not my own)

import os
import numpy

# specify file location
calc_pka_file = os.path.abspath('homework_files/clcf_propka.txt')
pka_file = open(calc_pka_file, 'r')
data = pka_file.readlines()
data_type = type(data)
# split desired value from rest of line and redefine variable
# print result; repeat for other specific lists
temp_Pka1 = [];
Pka1 = []
temp_Pka3 = [];
Pka3 = []
temp_Pka5 = [];
Pka5 = []
temp_Pka7 = [];
Pka7 = []
temp_Pka9 = [];
Pka9 = []
tempy = []
tempx = []
Pka_all = []
Pkas = []

# ASP comparison of predicted('') and calculated by propka:
for i in range(0, 6):
    for line in data:
        if '3.80' in line:
            line_a = line
            AA_line_split = line_a.split()
            Pkas = AA_line_split[0]
            Pka_all.append(Pkas)
            temp_Pka1.append(Pkas)
        # GlU comparison of predicted('') and calculated by propka:
        if '4.5' in line:
            line_a = line
            AA_line_split = line_a.split()
            Pkas = AA_line_split[0]
            Pka_all.append(Pkas)
            temp_Pka3.append(Pkas)
        # HIS comparison of predicted('') and calculated by propka:
        if '6.5' in line:
            line_a = line
            AA_line_split = line_a.split()
            Pkas = AA_line_split[0]
            Pka_all.append(Pkas)
            temp_Pka5.append(Pkas)
        # TYR comparison of predicted('') and calculated by propka:
        if '10.00' in line:
            line_a = line
            AA_line_split = line_a.split()
            Pkas = AA_line_split[0]
            Pka_all.append(Pkas)
            temp_Pka7.append(Pkas)

        # ARG comparison of predicted('') and calculated by propka:
        if '12.50' in line:
            line_a = line
            AA_line_split = line_a.split()
            Pkas = AA_line_split[0]
            Pka_all.append(Pkas)
            temp_Pka9.append(Pkas)

y = Pka_all
x = [3.80, 4.5, 6.5, 10.00, 12.50]

# print(len(Pka_all))

x_string = str(x)
y_string = str(y)

print("There were 5 pKa values selected from the output file for analysis. They were:", x)
print("Calculated values for several different ASP residues were as follows", temp_Pka1[:5])
print("Calculated values for several different GLU residues were as follows", temp_Pka3[:5])
print("Calculated values for several different HIS residues were as follows", temp_Pka5[:5])
print("Calculated values for several different TYR residues were as follows", temp_Pka7[:5])
print("Calculated values for several different ARG residues were as follows", temp_Pka9[:5])

# Optional: statistics

import statistics

# find average(z) of all values for StdDev comparison
# z = ((sum(Pka_all))/(len(Pka_all))

# Calculate average and stddev with statistics features.
# averages = m, across all values.

# print("The mean Pka value is" % mean(Pka_all))

# print("The Standard deviation of the propka protein values was " % (statistics.stdev(tempy, xbar = m)))

# print("The Standard deviation of the standard values is % s" %(statistics.stdev(x, xbar = m)))
# stddev calculation,standard values from average
# var = sum(pow(x-z,2) for x in y)/(len(tempy))
# s = math.sqrt(var)
# stddev calculation,calculated protein values from average