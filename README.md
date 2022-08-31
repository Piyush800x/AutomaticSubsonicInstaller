
# Automatic Subsonic Installer and Spotify Music Downloader
## About
This is a automatic subsonic installer in ubuntu server and also can download music from your favourite playlist of Spotify.

####
## Subsonic Official Website
Link -> http://www.subsonic.org/pages/index.jsp#learnmore

## Installation Guide
### 1st step
Update repositories
```bash
sudo apt-get update -y
```
### 2nd step
Install wget
```bash
sudo apt-get install wget -y
```
### 3rd step
If you don't have ufw enabled run this command or if you have ufw enabled then follow `4th step`
```bash
sudo ufw enable
```
Press `y` and `enter` Done.
Or


### 4th step
Download the script
```bash
wget https://raw.githubusercontent.com/Piyush800x/AutomaticSubsonicInstaller/main/main.py
```

### 5th step (Most Important)
I don't know which vps provider you are using, but `you must have inbound traffic to port 4040 enabled`, otherwise soubsonic will not work.

### 6th step (Final)
Run the script
```bash
sudo python3 main.py
```
Here select option 1
####
![Image 1](https://github.com/Piyush800x/AutomaticSubsonicInstaller/blob/main/img/subsonic_1.PNG)
####
Now you need to create a user for subsonic, Here i use username `subsonic` 
####
![Image 1](https://github.com/Piyush800x/AutomaticSubsonicInstaller/blob/main/img/subsonic_2.PNG)
####
Now here the script is creating a folder where your downloaded musics will stored.
####
![Image 1](https://github.com/Piyush800x/AutomaticSubsonicInstaller/blob/main/img/subsonic_3.PNG)
####
When the script is completed, it will show a path of your music folder that you created, copy that path and save for later use.
####
![Image 1](https://github.com/Piyush800x/AutomaticSubsonicInstaller/blob/main/img/subsonic_4.PNG)
####
Now open any web browser and open subsinic -> `yourpublicip:4040` and login.
The default username and password is `admin`.
####
![Image 1](https://github.com/Piyush800x/AutomaticSubsonicInstaller/blob/main/img/subsonic_5.PNG)
#### 
After login chnage the admin password and then click on setup media folders.
####
![Image 1](https://github.com/Piyush800x/AutomaticSubsonicInstaller/blob/main/img/subsonic_6.PNG)
####
Paste the path that you copied and click the save button.
#### 
![Image 1](https://github.com/Piyush800x/AutomaticSubsonicInstaller/blob/main/img/subsonic_7.PNG)
#### 
Run the script again
```bash
sudo python3 main.py
```
Now select option 2
Enter your favourite spotify playlist url, then the path that you copied and press enter you will see the downloading process.When the downloading finished go back to the browser. Click `scan media folders now` inside settings menu.
Go to index menu and you can find all your musics.
