import requests
from time import sleep
from os import system, name
banner = '''
   ____  _____ _____ ____  _____ _____ 
  |    \|     |     |    \|   __| __  |
  |  |  |  |  |  |  |  |  |__   |    -|
  |____/|_____|_____|____/|_____|__|__|
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠛⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣉⠉⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⢄⠀⠈⠂⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣶⣤⡉⢻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣀⠀⠀⠀⠀⠦⠈⢂⡀⠀⠈⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣦⢻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠠⢏⠀⠀⠀⠀⠀⠀⠈⢻⣿⡄⠀⠀⠀⣀⠁⣀⠈⠂⠀⠀⠀⠀⠀⠈⠉⠩⢬⣭⡛⢿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⠀⠀⠀⠀⠀⠑⢦⣄⣀⣤⣦⣤⡾⠋⠘⠛⢿⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣎⣿
⣿⣿⡉⢩⣭⣴⣿⣿⣿⠀⠀⠀⠀⠀⠀⢠⣀⠔⠈⢉⣴⣿⣿⣧⠀⠀⢸⣦⠀⣿⣷⣤⡀⠀⠀⠀⠀⠈⢦⡀⠈⣿
⡿⢛⣠⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⢁⠀⠀⡈⣿⣿⣿⣿⣶⣶⣾⣿⡄⡟⠛⠿⣿⠓⠀⠀⠀⠀⢸⣿⡆⢸
⣿⡆⣻⣿⣿⢰⣶⡝⣿⣿⠀⠀⠀⠀⠀⠀⠌⠳⢵⣶⣿⣿⣿⣿⡿⠏⢻⣿⢁⣷⣦⣤⣄⠀⣥⣈⠀⡀⢸⣿⣷⣾
⣯⣤⡛⢿⣿⡎⣿⠿⢘⡻⡄⡄⠀⠀⠀⠀⠀⠀⠀⠉⠻⣉⣱⣶⣚⣴⡿⢃⣾⣿⡉⢍⣛⣃⠈⠙⠷⣶⢈⣿⣿⣿
⣿⣿⣷⣾⡟⣡⣶⣿⣿⣿⠄⠀⠀⠀⠀⠀⠀⠀⠈⠓⠦⠈⠻⢿⡿⠋⠀⠀⠀⠨⣁⢀⠙⠿⣷⢸⣷⣶⣾⣿⣿⣿
⣿⣿⣿⣿⣧⢹⣿⣿⣶⣶⡦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠲⠀⠀⠀⠀⠀⠀⢹⣷⣿⣷⣶⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣷⡸⣿⣟⣫⣭⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠤⡀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡕⢿⣿⣟⣫⣵⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡟⠈⠿⣿⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡈⠛⠿⣿⣿⣿
⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣶⣧⣠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣄⣀⣀⣘⣿⣿⣿⣿⣿'''
# Function to read API key from file
def read_api_key(filename):
    with open(filename, "r") as file:
        api_key = file.read().strip()
    return api_key

# Function to read links from file
def read_links(filename):
    with open(filename, "r") as file:
        links = file.readlines()
    return [link.strip() for link in links]

# Function to clear the screen
def clear_screen():
    # For Windows
    if name == 'nt':
        _ = system('cls')
    # For UNIX based systems
    else:
        _ = system('clear')

# Function to get account info
def get_account_info(api_key):
    url = "https://doodapi.com/api/account/info"
    params = {"key": api_key}
    response = requests.get(url, params=params)
    data = response.json()
    if response.status_code == 200:
        return data["result"]
    else:
        print("\x1b[31mFailed to fetch account info:", data["msg"], "\x1b[0m")
        return None

# Function to display account info
def display_account_info(account_info):
    print("\n\x1b[36mAccount Information:\x1b[0m")
    print("\x1b[32mEmail:\x1b[0m", account_info["email"])
    print("\x1b[32mBalance:\x1b[0m", account_info["balance"])
    print("\x1b[32mStorage Used:\x1b[0m", account_info["storage_used"])
    print("\x1b[32mStorage Left:\x1b[0m", account_info["storage_left"])
    print("\x1b[32mPremium Expire:\x1b[0m", account_info["premim_expire"])

# Function to upload file using URL
def upload_file(api_key, upload_url):
    url = "https://doodapi.com/api/upload/url"
    params = {
        "key": api_key,
        "url": upload_url
    }
    response = requests.get(url, params=params)
    data = response.json()
    if response.status_code == 200:
        file_code = data["result"]["filecode"]
        print("\n\x1b[32mFile successfully uploaded.\x1b[0m")
        print("\x1b[32mFile code:\x1b[0m", file_code)
        print("\x1b[32mLink URL:\x1b[0m", "https://doods.pro/d" + "/" + file_code) # Menampilkan URL jarak jauh beserta kode file
    else:
        print("\x1b[31mFailed to upload file:", data["msg"], "\x1b[0m")

# Function to grab links from specified file and upload
def grab_links_from_file(api_key, filename):
    clear_screen()
    print("\n\x1b[36mGrabbing links from", filename, "and uploading...\x1b[0m")
    links = read_links(filename)
    for link in links:
        print("\n\x1b[36mUploading file from link:\x1b[0m", link)
        upload_file(api_key, link)
        sleep(1)  # Optional delay between uploads

# Main function
def main():
    clear_screen()
    api_key = read_api_key("apikey.txt")
    account_info = get_account_info(api_key)
    if account_info:
        print(banner)
        display_account_info(account_info)
        while True:
            print("\n\x1b[36mMenu:\x1b[0m")
            print("\x1b[33m[1]\x1b[0m Upload File from URL")
            print("\x1b[33m[2]\x1b[0m List Folders & Files")
            print("\x1b[33m[3]\x1b[0m Search File")
            print("\x1b[33m[4]\x1b[0m Grab Link from specified file")
            print("\x1b[33m[5]\x1b[0m Exit")
            choice = input("\x1b[33mEnter your choice:\x1b[0m ")
            if choice == "1":
                upload_url = input("\x1b[33mEnter upload URL:\x1b[0m ")
                print("\x1b[36mUploading file from URL...\x1b[0m")
                upload_file(api_key, upload_url)
            elif choice == "2":
                print("\x1b[36mListing folders and files...\x1b[0m")
                # Function to list folders and files
            elif choice == "3":
                search_term = input("\x1b[33mEnter search term:\x1b[0m ")
                print("\x1b[36mSearching files...\x1b[0m")
                # Function to search files
            elif choice == "4":
                filename = input("\x1b[33mEnter filename (e.g., file.txt):\x1b[0m ")
                grab_links_from_file(api_key, filename)
            elif choice == "5":
                print("\x1b[36mExiting program...\x1b[0m")
                break
            else:
                print("\x1b[31mInvalid choice. Please try again.\x1b[0m")

# Run the program
if __name__ == "__main__":
    main()

