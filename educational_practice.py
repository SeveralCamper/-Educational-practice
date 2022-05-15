import csv
from prettytable import PrettyTable

def fill_struct_list():
    tmp_struct_list = []
    try:
        file_path = open("currencies22.csv", "r")
        table = csv.reader(file_path, delimiter=';')
        for i in table:
            item = {"Name": i[0], "Market_cap": i[1], "Price": i[2]}
            tmp_struct_list.append(item)
        file_path.close()
    except FileNotFoundError:
        print("No file")

    return tmp_struct_list

def print_table(struct_list):
    table = PrettyTable()
    table.field_names = ["Name", "Market_cap", "Price"]
    for i in struct_list:
        table.add_row([i["Name"], i["Market_cap"], i["Price"]])
    print(table)

def search_table(struct_list):
    key = input()
    fined_elements_arr = []
    for i in  struct_list:
        if i["Name"] == key:
            fined_elements_arr.append(i)

    return fined_elements_arr

def parse_site():
    tmp_struct_list = []

def main():
    print("Write programm mode:",
          "1 - Read from file.",
          "2 - Read from site.",
          "e - Exit", sep='\n')
    while True:
        input_key = input()
        if input_key in ['1', '2', 'e']:
            if input_key == 'e':
                break;
            elif input_key == '1':
                exit_flag = 0
                struct_list = fill_struct_list()
                print_table(struct_list)
                print_table(search_table(struct_list))
            elif input_key == '2':
                pass
        else:
            print("Unvalid input.")

if __name__ == "__main__":
    main()