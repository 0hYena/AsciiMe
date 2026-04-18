# Setup Guide

## (1) Discord Dev Portal
### Go to https://discord.com/developers/applications and signin then create a bot
### On the left side head to OAuth2 and select "Bot" then "Administrator" then scroll to the bottom and copy the invite link and paste it to your server
<img width="1124" height="838" alt="image" src="https://github.com/user-attachments/assets/6449377c-adec-4f6a-a09e-9088b3e83b4f" />

### Then head to the "Bot" section in the dev portal and reset your token, this will give you an API key to your bot so COPY IT AND KEEP IT SAFE

<img width="1322" height="593" alt="image" src="https://github.com/user-attachments/assets/3323bfee-e6e6-4491-9d65-054c877c434c" />

## (2) Python & tools Setup
### Install the latest version of python and you want to get the tools in the terminal that the bot uses.
### Pyfiglet
```bash
pip install pyfiglet
```
### Discord.py
```bash
pip install discord.py
```
### Discord
```bash
pip install discord
```

## (3) The Code
### Go on discord head to settings and scroll to developer, then enable "Developer Mode"

<img width="1025" height="858" alt="image" src="https://github.com/user-attachments/assets/f59938c8-2d81-42aa-b872-aa96c66d89de" />

### Then right click the server you want the bot on and copy the server ID, and write it down.

<img width="313" height="625" alt="image" src="https://github.com/user-attachments/assets/e55ed7cc-8120-4ccf-88ca-b2eb6b7256be" />

### Download asciibot.py from the repository and open the file with any IDE and change these things.

### Line 11 and 21 replace "SERVER-ID" with your discord servers ID that you coppied

### Line 67 Replace TOKEN with the token you got from the Discord Developer Portal

### If you wanta custom font, create a new directory, download a new font (FLF File) I recomend DeltaCorpsPriest1 --> https://github.com/xero/figlet-fonts/blob/main/Delta%20Corps%20Priest%201.flf and put it in the directory, then go to line 56, and replace "CUSTOM-FONT-DIRECTORY" with the directory path of where you keep the flf file, then on line 58 change "CUSTOM-FONT-NAME" to the file name of the flf file just dont write "filename.flf" keep .flf out. Then Save it

<img width="801" height="1296" alt="tut2" src="https://github.com/user-attachments/assets/1840ae54-1018-486f-8215-692105499f27" />

## (4) Run It
### On the discord Server click the invite link you pasted in earlier and you can invite the bot. Then go on the asciibot.py file and run it, now you should be able to use the bot so yea have fun!!
