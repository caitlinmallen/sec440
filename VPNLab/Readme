# Using NoWire to tunnel to Minecraft Server
After installing NoWire on an AWS Ubuntu instance and a Windows 10 client, I decided to host a Minecraft server on the AWS host.\
Prerequisites:\
For the EC2 instance security groups, allow port 25565 through as a custom TCP rule for 0.0.0.0\0\
NoWire connection between Ubuntu server and Windows 10 client
## Installing Minecraft on Ubuntu:
On the Ubuntu VPN server, run the following command:\
`sudo apt update && sudo apt install openjdk-8-jre-headless screen -y && wget https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar && java -Xms1024M -Xmx1024M -jar server.jar nogui`\
After that, run this command:\
`java -Xms1024M -Xmx1024M -jar server.jar nogui`\
-Xms1024M configures to start the server with 1GB of memory, this can be adjusted for the server as needed. In my case, I used 300MB.\
-Xmx1024 configures the server to use 1GB of memory, this was also adjusted in my case for 300MB but can be adjusted up or down as needed.\
-jar specifies the server jar file to run.\
-nogui tells the server to not launch a GUI since this is an Ubuntu server.
## Accepting license 
From the current directory, open eula.txt and change it to equal true to accept the end user license agreement. If done correctly, the file will look like the following:\
`#By changing the setting below to TRUE you are indicating your agreement to our EULA (https://account.mojang.com/documents/minecraft_eula).
#Mon Mar 29 01:35:31 UTC 2021
eula=false`\
Once complete, rerun `java -Xms1024M -Xmx4G -jar minecraft_server_1.15.2.jar nogui` with needed memory adjustments and wait for the server to initialize. Once complete, you should get a similar message.\
`[21:15:37] [Server thread/INFO]: Done (30.762s)! For help, type "help"`\

## Loading into Minecraft
You will need to have a Minecraft account and download the Minecraft launcher. This can be downloaded from [here](https://www.minecraft.net/en-us/download/).\
Start the game as normal, in this case we have a vanilla server (no mod packs). You will then choose Multiplayer and add a server. Give it any name you want.\
For IP, choose to use the VPN server address at port 25565, this can be done like this <VPN_IP>:25565\
![](https://github.com/caitlinmallen/sec440/blob/main/VPNLab/minecraftsec440.png)\
Once this is done, click play and you should now load into your world to play in! 
