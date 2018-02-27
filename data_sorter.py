import csv

#read in the data
#col1 = time
#col2 = output
#col3 = input
file = input('File name?\n')
with open(file) as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    time = []
    inputs = []
    outputs = []
    for row in readCSV:
        try:
            t = float(row[0])
            
            i = float(row[2])
            o = float(row[1])
            time.append(t)
            inputs.append(i)
            outputs.append(o)
        except:
            row1 = row
    csvfile.close()
#finding separate step responses
indices = []
for i in range(1,len(inputs)):
    cur_step = inputs[i]
    if inputs[i] != inputs[i-1]:
        indices.append(i)


#TODO split the data into separate CSVs
print('New files: ' + str(len(indices)))

for j in range(len(indices)):

    try:
        timeset = time[indices[j]:indices[j+1]]
        inset = inputs[indices[j]:indices[j + 1]]
        prev_input = inputs[indices[j]-1]
        outset = outputs[indices[j]:indices[j + 1]]
        prev_output = outputs[indices[j]-1]
    except IndexError:
        timeset = time[indices[j]:len(time)]
        inset = inputs[indices[j]:len(inputs)]
        prev_input = inputs[indices[j] - 1]
        outset = outputs[indices[j]:len(outputs)]
        prev_output = outputs[indices[j] - 1]

    init_time = timeset[0]
    for t in range(len(timeset)):
        timeset[t] = round(timeset[t] - init_time, 3)
        inset[t] = inset[t] - prev_input
        outset[t] = round(outset[t] - prev_output, 3)



    print(file[:-4] + '_' + str(j) + '_'+ 'Step' + '_'+ str(inset[0]) + '.CSV')
    with open(file[:-4] + '_' + str(j) + '_'+ 'Step' + '_'+ str(inset[0]) + '.CSV', 'w', newline='') as writefile:
        writeCSV = csv.writer(writefile, delimiter = ',')
        for index in range(len(timeset)):
            row = [timeset[index], outset[index], inset[index]]
            writeCSV.writerow(row)

    writefile.close()


