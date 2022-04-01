import csv

#DEFAULT COMMAND: join C:\Coder\cvs_merger\csv_files\myFile0.csv C:\Coder\cvs_merger\csv_files\myFile1.csv id left
#DEFAULT COMMAND: join C:\Coder\cvs_merger\csv_files\file0.csv C:\Coder\cvs_merger\csv_files\file1.csv id left

def check_headers(ffile_header, sfile_header):
    result = []
    # SAME HEADERS
    for n in ffile_header:
        for m in sfile_header:
            if n == m:
                result.append(n)
    return result


print(
    "___________________________________________________________\n" +
    "   _____  _______      __  __  __                          \n" +
    "  / ____|/ ____\ \    / / |  \/  |                         \n" +
    " | |    | (___  \ \  / /  | \  / | ___ _ __ __ _  ___ _ __ \n" +
    " | |     \___ \  \ \/ /   | |\/| |/ _ \ '__/ _` |/ _ \ '__|\n" +
    " | |____ ____) |  \  /    | |  | |  __/ | | (_| |  __/ |   \n" +
    "  \_____|_____/    \/     |_|  |_|\___|_|  \__, |\___|_|   \n" +
    "                                            __/ |          \n" +
    "                                           |___/           \n" +
    "___________________________________________________________\n")
print("Welcome to CSV Merger!")
print("---------------------")
print("If no or wrong input is entered, default path are set to example files, column name is 'id' and join type is 'left")
print("---------------------")
while True:
    check = 0
    user_input = input("Use command: 'join file_path file_path column_name join_type': ")
    user_input_decision_list = user_input.split()
    try:
        if user_input_decision_list[0] != 'join':
            print("Wrong command. Use 'join' to merge CSV files")
            print("---------------------")
    except IndexError:
        print("Empty command. Use 'join' to merge CSV files")
        print("---------------------")


    try:
        if type(user_input_decision_list[1].lower()) == str:
            first_file_path = user_input_decision_list[1].lower()
    except IndexError:
        first_file_path = 'C:\Coder\cvs_merger\csv_files\myFile0.csv'

    try:
        if type(user_input_decision_list[2].lower()) == str:
            second_file_path = user_input_decision_list[2].lower()
    except IndexError:
        second_file_path = 'C:\Coder\cvs_merger\csv_files\myFile1.csv'
    try:
        with open(first_file_path) as file:
            ffile_list = file.readlines()
            for i in range(0, len(ffile_list)):
                if i <= len(ffile_list) - 2:
                    ffile_list[i] = [ffile_list[i][:-1]]
                else:
                    ffile_list[i] = [ffile_list[i]]
            ffile_header = ffile_list[0][0].split(',')
    except FileNotFoundError:
        print("Wrong file1 path")

    try:
        with open(second_file_path) as file:
            sfile_list = file.readlines()
            for i in range(0, len(sfile_list)):
                if i <= len(sfile_list) - 2:
                    sfile_list[i] = [sfile_list[i][:-1]]
                else:
                    sfile_list[i] = [sfile_list[i]]
            sfile_header = sfile_list[0][0].split(',')
    except FileNotFoundError:
        print("Wrong file2 path")

    try:
        if type(user_input_decision_list[3].lower()) == str and len(check_headers(ffile_header,sfile_header)) >= 1:
            column_name = user_input_decision_list[3].lower()
            check += 1
    except IndexError:
        column_name = 'id'
        check += 1
    except NameError:
        continue

    try:
        if type(user_input_decision_list[4].lower()) == str and user_input_decision_list[4].lower() in ['left','right','inner']:
            join_type = user_input_decision_list[4].lower()
        else:
            join_type = 'left'
        check += 1
    except IndexError:
            join_type = 'left'
            check += 1

    if check >=1:
        break


result_file_path = 'C:\Coder\cvs_merger\csv_files\\resultFile.csv'

#TODO writer bez csv

with open(result_file_path, 'w', newline='') as csvfile:
    result_writter = csv.writer(csvfile, delimiter=',',
                                quotechar=' ', quoting=csv.QUOTE_MINIMAL)

    index = 0
    result = []

    def list_by_column(file_list, file_header):
        temp = []
        column_list = []
        index = 0
        for n in range(0, len(file_header)):
            for row in file_list:
                temp.append(row[0].split(',')[index])
            index += 1
            column_list.append(temp)
            temp = []
            if index > 3:
                index = 0
        return column_list


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





    def print_to_rows(fcolumn_list, scolumn_list):
        temp = ''
        result = []
        index = 0

        for n in range(0, len(fcolumn_list[0]) - 1):
            for m in range(0, len(fcolumn_list) - 1):
                temp += (f"{fcolumn_list[m][n]},")
            result.append(temp)
            temp = ''
        temp = ''
        for n in range(0, len(scolumn_list[0]) - 1):
            for m in range(0, len(scolumn_list) - 1):
                temp += (f"{scolumn_list[m][n]},")
            temp = temp[:-1]
            try:
                result[index] = result[index] + temp
            except IndexError:
                result.append("," * (len(fcolumn_list) - 1) + temp)
            index += 1
            temp = ''

        if len(result[0].split(',')) != len(result[-1].split(',')):
            for i in range(len(result)):

                if len(result[i].split(',')) != len(result[0].split(',')):
                    result[i] = result[i] + "," * (len(scolumn_list) - 2)
        return result


    # LEFT
    if join_type == 'left':
        result = []
        index = 0
        for elem in ffile_list[0][0].split(','):
            if elem == column_name:
                ffile_column_index = index
                break
            else:
                ffile_column_index = -1
            index += 1
        index = 0
        for elem in sfile_list[0][0].split(','):
            if elem == column_name:
                sfile_column_index = index
                break
            else:
                sfile_column_index = -1
            index += 1

        for elem in ffile_list:
            result.append(elem)
        result[0][0] = result[0][0] + ',' + ",".join(sfile_header)
        index = 1
        for i in range(1, len(ffile_list)):
            for j in range(1, len(sfile_list)):
                if result[i][0].split(',')[ffile_column_index] == sfile_list[j][0].split(',')[sfile_column_index]:
                    try:
                        result[index][0] = result[index][0] + ',' + sfile_list[j][0]
                    except IndexError:
                        result[index][0] = result[index][0] + ',' * (len(sfile_list[0][0].split(',')))
                    finally:
                        break
            index += 1

        index = 0
        temp = result[0]
        for row in result:
            if len(row[0].split(',')) != len(temp[0].split(',')):
                result[index][0] = result[index][0] + "," * (len(sfile_list[0][0].split(',')))
            index += 1

        with open('C:\Coder\cvs_merger\csv_files\\resultFile.csv', 'w') as file:

            for row in result:
                for i in range(0, len(result[0])):
                    file.write(str(row[i]))
                file.write('\n')

    # RIGHT
    if join_type == 'right':
        result = []
        index = 0
        for elem in sfile_list[0][0].split(','):
            if elem == column_name:
                sfile_column_index = index
                break
            index += 1
        index = 0
        for elem in ffile_list[0][0].split(','):
            if elem == column_name:
                ffile_column_index = index
                break
            index += 1

        for elem in sfile_list:
            result.append(elem)
        result[0][0] = result[0][0] + ',' + ",".join(ffile_header)
        index = 1
        for i in range(1, len(sfile_list)):
            for j in range(1, len(ffile_list)):

                if result[i][0].split(',')[sfile_column_index] == ffile_list[j][0].split(',')[ffile_column_index]:
                    try:
                        result[index][0] = result[index][0] + ',' + ffile_list[j][0]
                    except IndexError:
                        result[index][0] = result[index][0] + ',' * (len(ffile_list[0][0].split(',')))
                    finally:
                        break
            index += 1

        index = 0
        temp = result[0]
        for row in result:
            if len(row[0].split(',')) != len(temp[0].split(',')):
                result[index][0] = result[index][0] + "," * (len(ffile_list[0][0].split(',')))
            index += 1

        with open('C:\Coder\cvs_merger\csv_files\\resultFile.csv', 'w') as file:

            for row in result:
                for i in range(0, len(result[0])):
                    file.write(str(row[i]))
                file.write('\n')

    # INNER

    if join_type == 'inner':
        result = [[""]]
        index = 0
        for elem in sfile_list[0][0].split(','):
            if elem == column_name:
                sfile_column_index = index
                break
            index += 1
        index = 0
        for elem in ffile_list[0][0].split(','):
            if elem == column_name:
                ffile_column_index = index
                break
            index += 1
        result[0][0] = ",".join(ffile_header) + ',' + ",".join(sfile_header)
        for i in range(1, len(ffile_list)):
            for j in range(1, len(sfile_list)):

                if ffile_list[i][0].split(',')[sfile_column_index] == sfile_list[j][0].split(',')[sfile_column_index]:
                    try:
                        result.append([ffile_list[i][0] + ',' + sfile_list[j][0]])
                    except IndexError:
                        continue
                    finally:
                        break
            index += 1

        with open('C:\Coder\cvs_merger\csv_files\\resultFile.csv', 'w') as file:

            for row in result:
                for i in range(0, len(result[0])):
                    file.write(str(row[i]))
                file.write('\n')


with open('C:\Coder\cvs_merger\csv_files\\resultFile.csv') as file:
    rfile_list = file.readlines()
    for i in range(0, len(rfile_list)):
        if i <= len(rfile_list) - 2:
            rfile_list[i] = [rfile_list[i][:-1]]
        else:
            rfile_list[i] = [rfile_list[i]]
    rfile_header = rfile_list[0][0].split(',')

    print("--------------------------")
    for row in rfile_list:
        print(row[0])
    print("--------------------------")

input("Press to Exit")
