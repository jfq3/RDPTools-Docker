# Install Third Party Programs

RDPTools depends on several third party programs that, because of licensing restrictions, we are not allowed to include in the RDPTools image. You need to install these using the script that we do provide. You need to do this only once.  

In the terminal, change to root user by entering:  

```
sudo su -
```

If you are prompted for a password, enter RDPuser. Then enter:  

```
/downloads/download_tools.py
```

Log out, exit the container and close the terminal by entering:  

```
exit
exit
exit