# DEFAULT COMMAND: join C:\Coder\cvs_merger\csv_files\myFile0.csv C:\Coder\cvs_merger\csv_files\myFile1.csv id left
# DEFAULT COMMAND: join C:\Coder\cvs_merger\csv_files\file0.csv C:\Coder\cvs_merger\csv_files\file1.csv id left

# Method that returns same header columns in both files
def check_headers(ffile_header, sfile_header):
    result = []
    # SAME HEADERS
    for n in ffile_header:
        for m in sfile_header:
            if n == m:
                result.append(n)
    return result

# Method to make a list of each column with header and values
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

# Method to print by column. OBSOLETE
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

# Method to print columns to rows. OBSOLETE
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

# Print startup
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
print(
    "If no or wrong input is entered, default path are set to example files, column name is 'id' and join type is 'left")
print("---------------------")

# loop for user to input correct data
while True:
    # check - ends loop after all of criteria is met
    check = 0

    # User enter values to app. It's splited for checking all one by one
    user_input = input("Use command: 'join file_path file_path column_name join_type': ")
    user_input_decision_list = user_input.split()

    # check if command is valid
    try:
        if user_input_decision_list[0] != 'join':
            print("Wrong command. Use 'join' to merge CSV files")
            print("---------------------")
    except IndexError:
        print("Empty command. Use 'join' to merge CSV files")
        print("---------------------")

    # check first file path entered. default set to existing file
    try:
        if type(user_input_decision_list[1].lower()) == str:
            first_file_path = user_input_decision_list[1].lower()
    except IndexError:
        first_file_path = 'C:\Coder\cvs_merger\csv_files\myFile0.csv'

    # check second file path entered. default set to existing file
    try:
        if type(user_input_decision_list[2].lower()) == str:
            second_file_path = user_input_decision_list[2].lower()
    except IndexError:
        second_file_path = 'C:\Coder\cvs_merger\csv_files\myFile1.csv'

    # opens first file and set it to LIST of LISTS of STRINGS. if no file founded, return to beginning
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

    # opens second file and set it to LIST of LISTS of STRINGS. if no file founded, return to input
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

    # sets column name if headers present in both of files. default for empty command, return to input if there is no matching ones
    try:
        if type(user_input_decision_list[3].lower()) == str and len(check_headers(ffile_header, sfile_header)) >= 1:
            column_name = user_input_decision_list[3].lower()
            check += 1
    except IndexError:
        column_name = 'id'
        check += 1
    except NameError:
        continue

    # sets join type if input is set correctly. Else sets to left
    try:
        if type(user_input_decision_list[4].lower()) == str and user_input_decision_list[4].lower() in ['left', 'right',
                                                                                                        'inner']:
            join_type = user_input_decision_list[4].lower()
        else:
            join_type = 'left'
        check += 1
    except IndexError:
        join_type = 'left'
        check += 1

    # breaks the loop if conditions are met
    if check >= 1:
        break

# Location of result file TODO set to default
result_file_path = 'C:\Coder\cvs_merger\csv_files\\resultFile.csv'

# LEFT merge
if join_type == 'left':
    result = []
    index = 0

    # checks which column is to be merged
    for elem in ffile_list[0][0].split(','):
        if elem == column_name:
            ffile_column_index = index
            break
        else:
            ffile_column_index = -1
        index += 1
    index = 0

    # checks which column is to be merged
    for elem in sfile_list[0][0].split(','):
        if elem == column_name:
            sfile_column_index = index
            break
        else:
            sfile_column_index = -1
        index += 1

    # merge the files
    for elem in ffile_list:
        result.append(elem)
    result[0][0] = result[0][0] + ',' + ",".join(sfile_header)
    index = 1
    for i in range(1, len(ffile_list)):
        for j in range(1, len(sfile_list)):

            # if in first and second column has the same value it merges
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

    # adds column if files column number is not equal
    for row in result:
        if len(row[0].split(',')) != len(temp[0].split(',')):
            result[index][0] = result[index][0] + "," * (len(sfile_list[0][0].split(',')))
        index += 1

    # Saves result to files
    with open('C:\Coder\cvs_merger\csv_files\\resultFile.csv', 'w') as file:

        for row in result:
            for i in range(0, len(result[0])):
                file.write(str(row[i]))
            file.write('\n')

# RIGHT
if join_type == 'right':
    result = []
    index = 0

    # checks which column is to be merged
    for elem in sfile_list[0][0].split(','):
        if elem == column_name:
            sfile_column_index = index
            break
        index += 1
    index = 0

    # checks which column is to be merged
    for elem in ffile_list[0][0].split(','):
        if elem == column_name:
            ffile_column_index = index
            break
        index += 1

    # merge the files
    for elem in sfile_list:
        result.append(elem)
    result[0][0] = result[0][0] + ',' + ",".join(ffile_header)
    index = 1
    for i in range(1, len(sfile_list)):
        for j in range(1, len(ffile_list)):

            # if in first and second column has the same value it merges
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

    # adds column if files column number is not equal
    for row in result:
        if len(row[0].split(',')) != len(temp[0].split(',')):
            result[index][0] = result[index][0] + "," * (len(ffile_list[0][0].split(',')))
        index += 1

    # Saves result to files
    with open('C:\Coder\cvs_merger\csv_files\\resultFile.csv', 'w') as file:

        for row in result:
            for i in range(0, len(result[0])):
                file.write(str(row[i]))
            file.write('\n')

# INNER
if join_type == 'inner':
    result = [[""]]
    index = 0

    # checks which column is to be merged
    for elem in sfile_list[0][0].split(','):
        if elem == column_name:
            sfile_column_index = index
            break
        index += 1
    index = 0

    # checks which column is to be merged
    for elem in ffile_list[0][0].split(','):
        if elem == column_name:
            ffile_column_index = index
            break
        index += 1

    # Combines headers
    result[0][0] = ",".join(ffile_header) + ',' + ",".join(sfile_header)

    # merges files
    for i in range(1, len(ffile_list)):
        for j in range(1, len(sfile_list)):

            # if in first and second column has the same value it merges
            if ffile_list[i][0].split(',')[sfile_column_index] == sfile_list[j][0].split(',')[sfile_column_index]:
                try:
                    result.append([ffile_list[i][0] + ',' + sfile_list[j][0]])
                except IndexError:
                    continue
                finally:
                    break
        index += 1

    # Saves result to files
    with open('C:\Coder\cvs_merger\csv_files\\resultFile.csv', 'w') as file:

        for row in result:
            for i in range(0, len(result[0])):
                file.write(str(row[i]))
            file.write('\n')

# Print result for user
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

# Exit - could be loop for new files but not specified by PO
input("Press to Exit")
