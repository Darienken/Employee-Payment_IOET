# EMPLOYEE-PAYMENT_IOET

## About
Hi there!  
My name is Diego, I'm a python developer and I created this program for IOET, inside this GitHub repository is the code of the program that I develop for them,   
right now I will give you a quickly overview about the code, the problem that I solve, how to install the program, how to use the program and a nice conclusion telling you about how was my experience working on the code and my POVs, so let's move on the nutshell

## Problem to solve
The company ACME offers their employees the flexibility to work the hours they want.   
They will pay for the hours worked based on the day of the week and time of day,  
according to the following table:    

|Monday to Friday | Payment |
| -------------   | -------------:
| 00:01  -  09:00 | 25 USD  |
| 09:01  -  18:00 | 15 USD  |
| 18:01  -  00:00 | 20 USD  |

|Saturday and Sunday | Payment |
| -------------   | -------------:
| 00:01  -  09:00 | 30 USD  |
| 09:01  -  18:00 | 20 USD  |
| 18:01  -  00:00 | 25 USD  |

The goal of this exercise is to calculate the total that the company has to pay an employee,     
based on the hours they worked and the times during which they worked.     
The following abbreviations will be used for entering data:      

|Day        | Abbreviation
|-----------|---------:
|Monday     | MO
|Tuesday    | TU
|Wednesday  | WE
|Thursday   | TH
|Friday     | FR
|Saturday   | SA
|Sunday     | SU

Input: the name of an employee and the schedule they worked, indicating the time and hours.     
This should be a .txt file with at least five sets of data.     
You can include the data from our two examples below.    

Output: indicate how much the employee has to be paid    

For example:    

Case 1:    

INPUT   

RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

OUTPUT:

The amount to pay RENE is: 215 USD

Case 2:

INPUT

ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

OUTPUT:

The amount to pay ASTRID is: 85 USD

## How do I solve this problem? (solution overview)
**I divide the problem...**      
First that I did was to think, ¿What is the main problem? ,¿What do I need to solve?,   
after thinking I read again the problem and I started getting details, requirements and thinks that I need, so the program must to **calculate the payment** of an employee based on **hours worked** but there are things that we need to take care, the **day** and **time**, I started dividing the problem based on this details... 
I set the following questions:   
**¿How can I get the hours worked of an employee?**    
I developed an algorithm for this problem.   
**¿How can I get the days worked of an employee?**   
I developed an algorithm for this problem.       
I used programming oriented objects and data structures to develop each algorithm.   
After I end with algorithms, I started working with results (each result is an object),   
I created a new .py file where I created a function, inside this function I put results together,  
**while I was coding I was testing** so after I did some tests and I comprobe that my program is working correct I did a second and third revision of my work,   
and finally I publish it here.
## What were you thinking when you wrote this code?
Modularizing, reutilizing and team work, I created classes and I develop the code in this way because
I believe this is a good way to work in team and in the future easily can add upgrades to the program,
you know... I was thinking of having a nice and clean code that everybody can understand.
## Explanation of my architecture
My architecture consist of 2 layers, **One layer has the algorithms** (Server) and **the other layer gives the structure** (Customer),   
both layers works together, when the user sends a request, the **customer** sends the information to the **server** and the server sends objects to the customer, when the customer receives the objects, in that moment the information what the user needs is displayed, so this is a work between two layers **server and customer**.    
now I will tell you what requirements I set for this software.    
**Functional Requirements**    
Descriptions of the data to be entered into the system:     
The data must to be write in a .txt file following the next format:     
EMPLOYEE_NAME=MO10:00-02:00,TU11:00-01:00   
The output must to be:   
The amount to pay EMPLOYEE_NAME is: VALUE USD   
The main file what is going to be execute must to be: Employee-Payment_IOET.py   
The algorithms must to be defined inside classes and using POO    
**No Functional Requirements**   
The code must to be clean   
You must to follow good practices  
You must to document the code  
**Design**    
One class    
Two methods    
**Documentation**     
![image](https://user-images.githubusercontent.com/82778294/144784617-27f5100b-d7f3-42fd-8ef3-4b21d3e6cc44.png)
### Explanation of my approach   
My approachs for this software were the next:      
-Meet customer needs    
-Give the customer a product that is scalable, with excellent design and well optimized   
-That the program can withstand future updates and is not going to deteriorate or present bugs and errors   
-Obtain well-documented and readable code that other programmers can maintain and understand what the code is about and how the algorithms work  
-Create a good software following good practices, because while I was developing this software I was thinking in how in the future this software can be improve and how can I help other programmer to understand my code, you know **I was developing a solution** but this solution was not only for the customer, this solution was for everyone in the world, because **we are programmers so we create solutions** and that is what I was thinking while I was coding.   
-Develop a reautilizable code   
## Explanation of my methodology   
I called this methodology **THINK-DIVIDE-TEST-CODE** so for created this methodology, I based on an AGILE methodology,   
so I work developing, testing, thinking and doing the same again and again like in iterative-block, I based on AGILE because I believe that this is a great methodology for working at the same time with the customer, you know develop and show product to the client, then if the client wants to change something I can do it because I'm writing a code for one functionality, also I use the divide-and-conquer method, I love using this method because you can develop software part-by-part and that's great specially when you are working with teams, so my methodology approach to develop a software what can be supported, improved and entendible for programmers and also the best software that a customer could image.
## How to execute the program? STEP-BY-STEP    
So easy...   
This program was created using python programming language, so first you need to install python in your operative system
### How to install python on Windows?    
### Step 1: Select Version of Python to download Full Installer and install    
The most stable Windows downloads are available from the [Python for Windows page](https://www.python.org/downloads/windows/).   
On Windows, you have a choice between 32-bit (labeled x86) and 64-bit (labeled x86–64) versions, and several flavors of the installer for each.   
Underneath the Python Releases for Windows find the Latest Python 3 Release — Python 3.10.0   
![image](https://user-images.githubusercontent.com/82778294/144758129-5d12e632-bcf8-4114-a486-7144487f5d4a.png)         
Python release for Windows | Official Website
![image](https://user-images.githubusercontent.com/82778294/144758162-7e1c4dc6-0fc4-4dc3-9d45-6cbba485038c.png)    
Python files to download for 32 bit and 64 bit system
### Step 2: Download Python Executable Installer and install it   
Double-click the executable file, which is downloaded.   
Select Customize installation and proceed.    
Click on the Add Path check box, it will set the Python path automatically.    
Run the Python Installer once downloaded. (In this example, we have downloaded Python 3.10.0)   
Make sure you select the “Install launcher for all users” and “Add Python 3.10 to PATH” checkboxes.   
Select Install Now — the recommended installation options.    
### Step 3: Wait for it to complete the installation process   
The next dialog will prompt you to select whether to Disable the path length limit. Choosing this option will allow Python to bypass the 260-character MAX_PATH limit. Effectively, it will enable Python to use long path names.   
The Disable path length limit option will not affect any other system settings. Turning it on will resolve potential name length issues that may arise with Python projects developed in Linux.   
### Step 4: Verification of installation of python in Windows   
To check if Python 3.10.0 has been successfully installed in our system,    
open a command-line in your system and execute the next command   
**“python --version”**   
### Step 5: Download and execute the program  
Now that we already have python installed, it's the moment to download the main actor, the payment program.    
First go to the top of this repository and click on code, and then download zip, check where your zip is located and extract it,    
after that you're going to have 2 .py scripts, open a command-line inside that folder and execute the next command   
**"python Employee-Payment_IOET.py"**   
if you follow all the steps you are going to get the result of this problem, the pourpose of the program, **the payment of your employees**    
### How to use the program?
Open the .txt file and insert data this way --> **<EMPLOYEE_NAME>=DAYSTARTIME-ENDTIME,DAYSTARTTIME-ENDTIME**,    
Then just execute the python programm, following the steps that I gave you on the previous guide STEP-BY-STEP.
### Conclusion
I hope that you understand the meaning of this program, how to use it, my mentality, my way of work and things that I can do, so I hope that yo really **learn something with this**
