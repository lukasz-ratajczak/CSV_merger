import csv

with open('C:\Coder\cvs_merger\csv_files\myFile0.csv', newline='') as csv_file:
    ffile_list = list(csv.reader(csv_file, delimiter=' ', quotechar='|'))

with open('C:\Coder\cvs_merger\csv_files\myFile1.csv', newline='') as csv_file:
    sfile_list = list(csv.reader(csv_file, delimiter=' ', quotechar='|'))

print(ffile_list)

"""
user_input = input("Use command: 'join file_path file_path column_name join_type'")

user_input_decision_list = user_input.split()

first_file_path = user_input_decision_list[1]
second_file_path = user_input_decision_list[2]
column_name = user_input_decision_list[3].lower()
join_type = user_input_decision_list[4].lower()
"""

with open('C:\Coder\cvs_merger\csv_files\\resultFile.csv', 'w', newline='') as csvfile:
    result_writter = csv.writer(csvfile, delimiter=',',
                                quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    if len(ffile_list) >= len(sfile_list):
        first_file_list = sfile_list
        second_file_list = ffile_list
    else:
        first_file_list = ffile_list
        second_file_list = sfile_list

    index = 0
    result = []
    """
    # LEFT
    #if join_type = 'left':
    for row in first_file_list:
        #result.append(row + '#'+second_file_list[index])
        result_writter.writerow(row + second_file_list[index])
        index += 1
    """
    """
    # RIGHT
    # if join_type = 'right':
    for row in first_file_list:
        #result.append(row + '#'+second_file_list[index])
        result_writter.writerow(second_file_list[index] + row)
        index += 1
    """

    # if join_type = 'inner':
    for row in first_file_list:
        for elem in row:
            # result.append(row + '#'+second_file_list[index])
            result_writter.writerow(elem.split(',')[:3]+second_file_list[index]+elem.split(',')[3:])
            # print(row + second_file_list[index] + row)
            #print()
            print(elem.split(',')[:3]+second_file_list[index]+elem.split(',')[3:])
            index += 1
