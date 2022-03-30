import csv

"""
user_input = input("Use command: 'join file_path file_path column_name join_type'")

user_input_decision_list = user_input.split()

first_file_path = user_input_decision_list[1]
second_file_path = user_input_decision_list[2]
column_name = user_input_decision_list[3].lower()
join_type = user_input_decision_list[4].lower()
"""
first_file_path = 'C:\Coder\cvs_merger\csv_files\myFile0.csv'
second_file_path = 'C:\Coder\cvs_merger\csv_files\myFile1.csv'
join_type = "inner"
column_name = 'id'

result_file_path = 'C:\Coder\cvs_merger\csv_files\\resultFile.csv'

with open(first_file_path, newline='') as csv_file:
    ffile_list = list(csv.reader(csv_file, delimiter='_', quotechar='|'))

with open(second_file_path, newline='') as csv_file:
    sfile_list = list(csv.reader(csv_file, delimiter='_', quotechar='|'))

with open(result_file_path, 'w', newline='') as csvfile:
    result_writter = csv.writer(csvfile, delimiter=',',
                                quotechar=',', quoting=csv.QUOTE_MINIMAL)
    """if len(ffile_list) >= len(sfile_list):
        first_file_list = ffile_list
        second_file_list = sfile_list
    else:
        first_file_list = sfile_list
        second_file_list = ffile_list"""

    index = 0
    result = []

    ffile_header = ffile_list[0][0].split(',')
    sfile_header = sfile_list[0][0].split(',')

    # TODO możliwe że usuwanie kolumny w left i right nie bęzie potrzebne. Wtedy usunać
    # TODO zrobić zbieranie kolumn zamiast wierszy. Będzie łatwiej je wyświetlać wtedy

    temp = []
    ffile_column_list = []
    for n in range(0, len(ffile_header)):
        for row in ffile_list:
            temp.append(row[0].split(',')[index])
        index += 1
        ffile_column_list.append(temp)
        temp = []
        if index > 3:
            index = 0

    temp = []
    sfile_column_list = []
    for n in range(len(sfile_header)):
        for row in sfile_list:
            temp.append(row[0].split(',')[index])
        index += 1
        sfile_column_list.append(temp)
        temp = []
        if index > 3:
            index = 0

#print(ffile_column_list)
#print(sfile_column_list)

def print_by_column(column_list, list_of_valid_headers):
    index = 0
    result = [[]]
    for column in column_list:
        for elem in column:
            if elem in list_of_valid_headers:
                break
            else:
                result[index].append(elem)
        if result[-1] == []:
            continue
        else:
            result.append([])
        index += 1
    return result

def check_headers(ffile_header, sfile_header):
    result = []
    #SAME HEADERS
    for n in ffile_header:
        for m in sfile_header:
            if n == m:
                result.append(n)
    return result

print(print_by_column(ffile_column_list, ['lastname']))
print(check_headers(ffile_header,sfile_header))

# LEFT
if join_type == 'left':

    for row in ffile_list:
        result.append([elem for elem in row[0].split(',')])
    for row in sfile_list:
        try:
            result[index] += row[0].split(',')
        except IndexError:
            result.append([""] * len(ffile_list[0][0].split(',')) + row[0].split(','))
        index += 1

    index = 0
    for row in result[0]:
        check = 0
        for elem in result[0]:
            if elem == row:
                check += 1
            if check > 1:
                rmv_column = index
        index += 1

    index = 0
    for row in result[::]:
        try:
            result[::][index].pop(rmv_column)
        except IndexError:
            break
        index += 1

    for row in result:
        result_writter.writerow(row)

# RIGHT
if join_type == 'right':
    for row in sfile_list:
        result.append([elem for elem in row[0].split(',')])
    for row in ffile_list:
        try:
            result[index] += row[0].split(',')
        except IndexError:
            result.append([""] * len(sfile_list[0][0].split(',')) + row[0].split(','))
        index += 1

    index = 0
    for row in result[0]:
        check = 0
        for elem in result[0]:
            if elem == row:
                check += 1
        if check > 1:
            rmv_column = index

    index = 0
    for row in result[::]:
        try:
            result[::][index].pop(rmv_column)
        except IndexError:
            break
        index += 1

    for row in result:
        result_writter.writerow(row)

# INNER

if join_type == 'inner':
    same_headers = []
    for elem_f in ffile_header:
        check = 0
        for elem_s in sfile_header:
            if elem_f == elem_s:
                check += 1
            if check > 0:
                same_headers.append(elem_f)
    print(list(set(same_headers)))
