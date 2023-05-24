# Installing RDPTools using Singularity

Log into the HPCC with your user name and password.  

```
ssh dev-intel18
```

While in you home directory, create a singularitiy image of RDPTools named RDPTools using the command:  

```
singularity build RDPTools docker://rdpstaff/rdp_tools
```

Once the image is successfully built, run the image shell to start RDPTools by entering the command:

```
singularity shell RDPTools
```

The terminal prompt will change ato ```Singularity>``` indicating that ou are logged into RDPTools.  

## Install Third Party Programs
**NOTE: It is not possible to download the third party programs to RDPTools on Singularity because sudo privledges are disabled in Singularity. Also, it is not pssible to edit the installation script because the directory is not writable.**  

RDPTools depends on several third party programs that, because of licensing restrictions, we are not allowed to include in the RDPTools image. You need to install these using the script that we do provide. You need to do this only once.  Enter:  

```
wget https://github.com/jfq3/RDPTools-Docker/raw/main/downloads/download_tools_jq.py
chmod 750 download_tools_jq.py
mv download_tools_jq.py /downloads
/downloads/download_tools_jq.py
```

To end your Singularity session, enter:  

```
exit
```
RDPTools is now installed in your home directory. Close your connection to the HPCC. You must start a new connection before you can use RDPTools. 