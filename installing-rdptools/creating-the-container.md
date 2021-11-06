# Creating the Container

Start Docker, open a terminal and enter:  

```
docker pull rdpstaff/rdp_tools
```

Once download the docker rdp_tools image, the image will display on the docker desktop

Check if the image is download, run:

docker images
It will display all docker images

3. Create a container from the downloaded rdp_tools image with mapped local directory:
This step is to create a container and able to store all the data generated from the image to the local machine. So once the docker image is updated, you will not lose your data.

Command Structure (Do NOT run below command without modification):

docker run --name <container_name> -it -v {local directory path of your computer}:{rdp_tools directory path} rdpstaff/rdp_tools
Explanation of above commands:

The syntax inside < > is the name of container
The syntax inside { } is the directory path you want to map.
In the first { }, you should put your local machine directory where you want to save data to.
The second { } is the path of the directory in your docker container.
rdpstaff/rdp_tools is the name of the image.
The rest of commands such as --name, --it, -v are buit-in commands from docker, which should not be changed
Example:

docker run --name rdp_tools -it -v C:/Users/mycomputer/docker_data:/home/RDPuser rdpstaff/rdp_tools
In the above example: the local directory C:/Users/mycomputer/docker_data is mapped with docker entire user directory /home/RDPuser. the above directory path is suggested but is up to your preference.

Once you enter the above command with proper directory mapped, You will see something similar to RDPuser@33306a31b588:/
This indicates that you have logged in to the container

Check if the directory is properly mapped(Optional):

Open the local folder that you mapped: C:/Users/mycomputer/docker_data (example)
Open the directory yo mapped in docker: /home/RDPuser (example)
Create a folder in docker mapped director: mkdir test
Go back to the local folder and check if the test folder exists
4. Login to the container
This step shows how to login to the container, assuming you named container rdp_tools

First-time login:
Switch to root user:
sudo su -
In prompt, enter password (ignore if no prompt), which is the same as the username
RDPuser
Then download all the third party necessary::
/downloads/download_tools.py
Once completed, switch user back to default RPDuser
sudo su - RDPuser
In prompt, enter password (ignore if no prompt), which is the same as the username
RDPuser
Second-time login:
This step is for users who have exited the image and want to re-login and continue to use the docker container.

Run
docker container ls -l
This command will display all the docker containers.
Start the container:
docker start rdp_tools
This command will start the container. The rdp_tools is the name of the container, in case you have a different name, change it, accordingly.
Then run:
docker attach rdp_tools 
You will see something similar to RDPuser@33306a31b588:/ This indicates that you have logged in to the container
5. Use rdp_tools from the command line.