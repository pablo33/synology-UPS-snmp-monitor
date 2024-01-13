## Installing pysmnp in your system
You can install pysnmp as a normal reposytory with PIP.  
python3 -m pip install pysnmp  
python3 -m pip install pysnmp-pysmi  

... or install them on your virtual environment for python.   


## Compiling MIBs.txt in py-MIBs
In order to work with snmp, you have to compile MIBs files for Synology.  
Once downloaded, you need to convert them with **mibdump.py** utility. This utility it is bundled with your pysnmp installation. Just call it from the prompt.  

Compiling command:  
mibdump.py --generate-mib-texts  --destination-format pysnmp --mib-source=./ SYNOLOGY-UPS-MIB  

You can see that --mib-source is pointing at your current directory, so run this command from your MIB repository folder or tweak the source folder..  
As you start to compile synology MIBs, they start to call dependent MIB files, you can find this files in Internet and add them beside your Synology MIBs files. Most of files already are in this repo.  

Compiled py-mibs goes to ~/.pysnmp/mibs/  which is one of the mib-path folders in wich pysnmp goes to find py-compiled MIBs files.  


## Setting up your system
For testing purposes, you can launch the script withing your user, the pysnmplibrary searchs pycompiled files at your user directory:  

 ~/.pysnmp/mibs/

Place your py-compiled MIB files there.  

For production environment, you should run this script as root. For convenience, the script added a folder at the same place from it is run to facilitate things. So, add a new folder called 'pysnmp_mibs.PY' besides your script and put in there py-compiled MIB files.  

Install your python dependencies with root.  
Put your script at the /opt/synology-UPS-monitor/.... for example.
And place there:  
  * The script "synoUPSmonitor.py"  
  * Your settigs "settings.py"  
  * Your py-compiled MIBs folder with MIBs**.py "pysnmp_mibs.PY" (remember this place is added in pysnmp path by the script)  

Launch your script with root and see that it works.  
You will see a 



