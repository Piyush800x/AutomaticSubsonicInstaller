
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
Run the following commands
```bash
sudo ufw allow 4040/tcp
```
```bash
sudo ufw allow 4040/udp
```
```bash
sudo ufw reload
```

### 5th step
Download the script
```bash
wget https://raw.githubusercontent.com/Piyush800x/AutomaticSubsonicInstaller/main/main.py
```

### 6th step (Most Important)
I don't know which vps provider you are using, but `you must have inbound traffic to port 4040 enabled`, otherwise soubsonic will not work.

### 7th step (Final)
Run the script
```bash
sudo python3 main.py
```