#!/usr/bin/python3

import wget
import os

#download hmmer
print("\n ***** downloading hmmer ***** \n")
os.system('echo RDPuser | sudo -S apt-get install -y hmmer')
print("\n ***** download hmmer completed ***** \n")

#update working directory:
# os.chdir("/downloads")

# download usearch8.1
print("\n ***** downloading usearch ***** \n")
os.system("sudo wget https://drive5.com/downloads/usearch8.1.1861_i86linux32.gz")
os.system('sudo gzip -d usearch8.1.1861_i86linux32.gz')
os.system("sudo chmod 777 usearch8.1.1861_i86linux32")
os.system('sudo mv usearch8.1.1861_i86linux32 /usr/local/bin/usearch8.1')
print("\n ***** download usearch completed *****\n")

# download uchime
print("\n ***** downloading uchime ***** \n")
os.system("sudo mkdir /usr/local/uchime")
os.system("sudo wget http://drive5.com/uchime/uchime4.2.40_i86linux32")
os.system("sudo chmod 777 uchime4.2.40_i86linux32")
os.system("sudo mv uchime4.2.40_i86linux32 /usr/local/uchime/uchime")
print("\n ***** download uchime completed *****\n")

# install infernal
print("\n ***** downloading infernal ***** \n")
os.system('sudo apt-get install infernal -y')
print("\n ***** download infernal completed *****\n")

# install fasttree 
print("\n ***** downloading fasttree ***** \n")
os.system('sudo apt-get install fasttree -y')
print("\n ***** download infernal completed *****\n")

# installblast2
print("\n ***** downloading installblast2 ***** \n")
os.system('sudo apt-get install blast2 -y')
print("\n ***** download infernal completed *****\n")

# install FunGene pipeline
print("\n ***** downloading FunGene pipeline ***** \n")
os.system("sudo git clone https://github.com/rdpstaff/fungene_pipeline.git")
os.system("sudo mv fungene_pipeline /usr/local")
print("\n ***** download FunGene pipeline completed ***** \n")

# install RDP_Assembler
print("\n ***** downloading RDP_Assembler ***** \n")
os.system("sudo apt-get update -y")
os.system("sudo apt-get install libltdl-dev -y")
os.system("sudo apt-get install libbz2-dev -y")
os.chdir("/usr/local/")
# os.system("sudo wget http://rdp.cme.msu.edu/download/RDP_Assembler.tgz"
os.system("sudo wget "https://github.com/jfq3/RDPTools-Docker/raw/main/downloads/RDP_Assembler.tgz"
os.system("sudo tar xzf RDP_Assembler.tgz")
os.system("sudo rm RDP_Assembler.tgz")
os.chdir("/usr/local/RDP_Assembler/pandaseq/")
os.system("sudo ./configure LDFLAGS=-L/usr/local/lib CPPFLAGS=-I/usr/local/include")
os.system("sudo make clean")
os.system("sudo make")
os.system("sudo chown -R RDPuser:RDPuser /usr/local/RDP_Assembler/")
print("\n ***** download RDP_Assembler completed ***** \n")

# add gold.fa to /home/RDPuser/resources
os.chdir("/downloads/")
os.system("wget https://drive5.com/uchime/rdp_gold.fa")
os.system("mkdir /home/RDPuser/resources")
os.system("mv rdp_gold.fa /home/RDPuser/resources")

# Make Xander python scripts executable.
os.chdir("/usr/local/RDPTools/Xander_assembler/pythonscripts")
os.system("sudo chmod 777 *.py")

# Edit Xander bash scripts
os.chdir("/usr/local/RDPTools/Xander_assembler/bin")
os.system("sudo sed -i 's/python/python2/' run_xander_findStarts.sh")
os.system("sudo sed -i 's/python/python2/' prepare_gene_ref.sh")

# Ensure that RDPuser can write to /home/RDPuser
os.system("sudo chown RDPuser:RDPuser /home/RDPuser -R")
