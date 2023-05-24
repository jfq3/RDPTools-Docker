# Install Third Party Programs

RDPTools depends on several third party programs that, because of licensing restrictions, we are not allowed to include in the RDPTools image. You need to install these using the script that we do provide. You need to do this only once.  

In the terminal, change to root user by entering:  

```
sudo su -
```

If you are prompted for a password, enter RDPuser. Then enter:  

```
wget https://github.com/jfq3/RDPTools-Docker/raw/main/downloads/download_tools_jq.py
chmod 750 download_tools_jq.py
mv download_tools_jq.py /downloads
/downloads/download_tools_jq.py
```

Log out, exit the container and close the terminal by entering:  

```
exit
exit
exit