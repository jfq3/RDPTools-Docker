# Installing Docker for Windows

Before installing Docker Desktop in Windows, you must make sure that your computer and Windows version meet the minimum requirements outlined below. Refer to the Docker installation instructions at [https://docs.docker.com/docker-for-windows/install/](https://docs.docker.com/docker-for-windows/install/) if the instructions below still leave you wondering.

Minimum requirements:

* Processor: 64 bit processor with Second Level Address Translation \(SLAT\)
* RAM: A minimum of 4GB system RAM
* Windows 10 64-bit: Pro, Enterprise, or Education \(Build 16299 or later\)
* BIOS support for virtualization
  * Hyper-V and Containers Windows features must be enabled.

### Checking requirements

You can check for most of these requirements using the Windows System information app; just enter "system info" in to the Windows search box.

All modern processors support SLAT. AMD has supported this technology with what it calls Rapid Virtualization Indexing \(RVI\) technology since the introduction of its third-generation Opteron processors \(code name Barcelona\). Intel's implementation of SLAT, known as Extended Page Table \(EPT\), was first introduced in the Nehalem microarchitecture found in certain Core i7, Core i5, and Core i3 processors. If you want to check, make a web search for your processor's specifications. Alternatively, you can use a tool available at [https://www.howtogeek.com/73318/how-to-check-if-your-cpu-supports-second-level-address-translation-slat/](https://www.howtogeek.com/73318/how-to-check-if-your-cpu-supports-second-level-address-translation-slat/).

### Enabling virtualization

By default, virtualization is probably not enabled on your computer. You can check by opening Task Manager and clicking on the Performance tab. Enabling virtualization means making changes to the BIOS settings. Exactly how to do this depends on the make and model of your computer, so for instructions it is best to make a web search using that information.

### Installing Docker Desktop

Download the stable version of Docker for Windows from [https://hub.docker.com/editions/community/docker-ce-desktop-windows/](https://hub.docker.com/editions/community/docker-ce-desktop-windows/) and follow the installation instructions at [https://docs.docker.com/docker-for-windows/install/](https://docs.docker.com/docker-for-windows/install/).

### Configuring Docker Desktop

Start Docker. Click on the gear icon in the menu bar (upper right). Click on the General tab. To prevent Docker from starting automaticallly when you boot your computer, make sure the "Start Docker Desktop when you log in" is unchecked. If you have WSL 2 installed, check the box "Use the WSL 2 based engine." For convenience, make sure the box for "Open Doceker Dashboard at startup"is checked. Click **Apply & Restart**.  

Create a folder for storing your RDPTools results. This does not have to be on your C drive. 

You are now ready to install RDPTools.

