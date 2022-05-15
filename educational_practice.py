import csv
import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

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
    print("Write key for search")
    key = input()
    fined_elements_arr = []
    for i in  struct_list:
        if i["Name"] == key:
            fined_elements_arr.append(i)

    return fined_elements_arr

def parse_site():
    tmp_struct_list = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.79"}
    try:
        response = requests.get(url="https://coinmarketcap.com", headers=headers)
        print(response) # Response [200] - ответ: успешно полуили ответ с сервера и зашли на него
        soup = BeautifulSoup(response.text, "lxml")
        html_table = soup.find("tbody")
        name_arr = html_table.find_all("p", class_="sc-1eb5slv-0 iworPT")
        market_cap_arr = html_table.find_all("span", class_="sc-1ow4cwt-1 ieFnWP")
        price_arr = html_table.find_all("div", class_="sc-131di3y-0 cLgOOr")
        for i in range(len(name_arr)):
            item = {"Name": name_arr[i].text, "Market_cap": market_cap_arr[i].text, "Price": price_arr[i].text}
            tmp_struct_list.append(item)
    except(ConnectionError, Timeout, TooManyRedirects) as exp:
        print("Error", exp, sep=":")

    return tmp_struct_list

def main():
    print("Write programm mode:",
          "1 - Read from file.",
          "2 - Read from site.",
          "e - Exit", sep='\n')
    struct_list = []
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
                struct_list = parse_site()
                print_table(struct_list)
                print_table(search_table(struct_list))
        else:
            print("Unvalid input.")

if __name__ == "__main__":
    main()