from ast import arg
from ntpath import join
import os
from queue import Empty
from sys import argv
import tarfile 



print("Python module to enable metasploit console to pentest host with multiple exploits/attacks:")
print("Loading .... ")



#Define the path and write it to the file 
expl_path = ''
cfg_path = ''
persistent = ''
res_name = ''
if len(argv)!= 1:
    cfg_path = argv[1] 

#use a custom config file
if cfg_path == "":
    while (persistent != 'Y' and  persistent!= 'y') and ( persistent != 'N' and  persistent != 'n'): 
        persistent = input("Use an already existent config file ? Y/N ....")
        if persistent == 'Y' or persistent == 'y' :
            # get the path to the config file 
            cfg_path = input('Custom config file path ...')
        elif persistent == 'N' or persistent == 'n': 
                cfg_path = 'NIL'
        else:  print("Please select an option :  ")  

#Create a new folder to store the resource files 

if cfg_path == 'NIL':
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, r'Resource-files')
    if not os.path.exists(final_directory):
        os.makedirs(final_directory)

    res_name = input("Name for resource file ..." + '\n')
    os.chdir(final_directory)
    #print('the pwd is '+ os.getcwd())
    file = open(res_name+'.rc',"w")

    print("Specify the full path to the exploit/exploits  .......... When finish press ENTER  " + '\n')


    file.writelines("""<ruby>
    help = %Q|
        Description:
        This Metasploit RC file can be used to automate the exploitation process.
            Settin the host we want to target and then set the multiple exploits that we'll
            test on the target . 
            You can see the output in of the script in 'console.log' file available in the working folder . 


        Author:
        sdogaru - Bitdefender 
        |

        print_line(help)
        Rex::sleep(1.5)
        </ruby>""")

        
    
    file.write('\n')
    file.write('\n')
    file.write('\n')
    
    exploits = []
 


   #save the output into a log file 
    dir  = os.getcwd()
    final_dir = os.path.join(dir, r'Logs')
    print(final_dir+'\n')
    if not os.path.exists(final_dir):
        os.makedirs(final_dir)

    file.write('spool' +' '+ final_dir+'/' + 'console'+'_'+res_name+'.log' + '\n')
    cnt = 1 
    expl_path = input("Path:"+  '(' + str(cnt) + ')')
    while expl_path: 
        
        
        if expl_path !=Empty:
            cnt= cnt+1
            exploits.append(expl_path)
        expl_path = input("Path:"+  '(' + str(cnt) + ')')
    #set the option globally 'setg'
    options = {}  
    #file.write("set THREADS 15 " + '\n')
    rhost  = input('Set the RHOSTS ip : ')
    #file.write("setg RHOSTS " +" " + rhost+'\n')
    options['RHOSTS'] = rhost
    rport  = input('Set the default  RPORT : ')
    #file.write("set RPORT " + rport +'\n')
    options['RPORT'] = rport 
    lhost  = input('Set the LHOST ip: ')
    #file.write("set LHOST " + lhost+'\n')
    options['LHOST'] = lhost
    lport  = input('Set the LPORT  : ')
    #file.write("set LPORT  " + lport+'\n')
    options['LPORT'] = lport
    targeturi = input("Set the TARGETURI: ")
    options["TARGETURI"] = targeturi


#TODO add more options to set e.g passwd , admin , pwd etc  

    
    #loop through all the exploits in the list  and run each one of them     
    for exploit in exploits : 
        if exploit!= "":
           
            file.write('use' + ' ' + exploit + '\n')
            #set the options 
            
            for k ,v in options.items():
                file.write('set' + ' '+ k  + ' ' + v  +'\n')


            file.write('exploit' +'\n')




    file.write('exit'+'\n')
    file.close()
    cfg_path = os.getcwd() +'/' + res_name + '.rc'
    #print(cfg_path)

# ---- run the script with msfconsole as a resource file ----
os.system('msfconsole -r' + ' ' + cfg_path )