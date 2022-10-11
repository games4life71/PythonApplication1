	This script is designed to automate Metasploit console (msfconsole)  attacks over a targer with multiple exploits . 
It takes use of metasploit's Resource Files (.rc) in which we can automate attacks by setting commands such as : set RHOSTS  , info , show options , exploit etc .. 
The script creates a Resource File with this commands and launches msfconsole automatically with the given resource file . It also generate into 'Logs' folder 
a file containing all the logs of the given attack . 

   author : sdogaru 

Use :  

python3/python  metasploit_automate.py [path/to/custom/resource] - optional 

  
