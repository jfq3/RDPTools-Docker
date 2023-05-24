# Creating the Container

Start the Docker engine by clicking on its icon. Once it is running, open a terminal and enter:  

```
docker pull rdpstaff/rdp_tools
```

After the rdp_tools image is downloaded it will display on the Docker desktop. To check that it is downloaded, you can enter:  

```
docker images
```
This command will dispaly all docker images locally available.  

When you create a container from the Docker image, you need to map it to a directory on your computer, *i.e.* outside of the container. This makes the results accessable to other programs. Also, in the event you update RDPTools, any previous results will not be lost.  

Begin by creating or choosing a local directory. In the example command below, this is D:/RDPtools_data. Then enter the following command in the terminal, changing the name of the local directory and its path as necessary:   

```
docker run --name rdp_tools -it -v D:/RDPTools_data:/home/RDPuser rdpstaff/rdp_tools
```
After you enter the above command with the proper directory mapped, you will see something similar to ```RDPuser@216930f78851:~$``` as he prompt in the terminal. This indicates that you have logged into the container.  

## Optional
To check that the directories are properly mapped, enter the following in the terminal:  

```
touch test
```
Open the local directory, for example with File Explorer. It should contain an empty file named test.  

To test in the opposite directon, paste a small text file, *e.g.* one named report.txt, into the local directory. Back in the terminal, enter:

```
ls
```

This should list the name of the file you just pasted into the local directory. You may read the contents of the text file with:

```
less report.txt
```

(Assuming that report.txt is the file name.)


```
