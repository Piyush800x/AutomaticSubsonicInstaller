import os
from subprocess import getoutput

path = []
# Installing all the base packages for subsonic
def get_subsonic():
    print("Updating Repositories")
    os.system("sudo apt-get update -y")
    os.system("sudo apt-get install wget -y")
    os.system("sudo apt install python3-pip -y")
    os.system("sudo apt-get install openjdk-8-jre -y")
    os.system("pip3 install spotdl")
    os.system("sudo apt-get install figlet -y")
    os.system("pip3 install --upgrade requests")
    os.system("sudo apt install ffmpeg -y")
    os.system("wget https://s3-eu-west-1.amazonaws.com/subsonic-public/download/subsonic-6.1.6.deb")
    os.system("sudo dpkg -i subsonic-6.1.6.deb")
    os.system("pip3 install spotipy --upgrade")

# Creating a non root user
def create_user(username):
    os.system(f"sudo useradd --system {username}")
    os.system(f"sudo gpasswd -a subsonic {username}")
    os.system(f"sudo sed -i 's/SUBSONIC_USER=root/SUBSONIC_USER={username}/g' /etc/default/subsonic")

# Setting up a music folder
def music_folder(name):
    os.system(f"sudo mkdir {name}")
    os.system(f"sudo chmod +x {name}")
    pwd = getoutput("pwd")
    music_path = str(pwd) + f"/{name}"
    path.append(music_path)

# To download spotify musics
def spotdl():
    path = input("Enter path for downloading music: ")
    url = input("Enter spotify playlist url: ")
    try:
        if url == "" or path == "":
            print("Url can't be empty\nTry again")
            return spotdl()
        else:
            os.system(f"spotdl {url} -o {path}")
    except Exception as e:
        print("Error downloading music\nRepeat your download process again!")
        return spotdl()

# Allows subsonic through firewall
def firewall():
    os.system("sudo ufw allow 4040/tcp")
    os.system("sudo ufw allow 4040/udp")
    os.system("sudo ufw reload")


def main():
    print("-----------------------------------------------------")
    print("1. Automatic installation of SUBSONIC\n2. Download spotify music")
    answer = input("==> ")
    if answer == "" or any(map(str.isalpha, answer)) == True:
        print("Input incorrect!\nTry again")
        return main()
    elif answer == "1":
        print("------------------------------CREATING USER FOR SUBSONIC------------------------------")
        username = input("Enter username: ")
        name = input("Enter folder name you want to create: ")
        user = any(map(str.isdigit, username))
        if user == True or username == "":
            print("A username can't contain numbers\nTry again")
            return main()
        else:
            get_subsonic()
            create_user(username)
            music_folder(name)
            firewall()
            print("--------------COPY THIS PATH---------------")
            print("OPEN <your-public-ip>:4040 ON YOUR BROWSER")
            print(path[0])
            print("-------------------------------------------")
    elif answer == "2":
        spotdl()


if __name__ == "__main__":
    os.system("sudo apt-get install figlet -y")
    main()
