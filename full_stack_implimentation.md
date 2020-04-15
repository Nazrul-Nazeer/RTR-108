# FULL STACk
A **Full stack** devoloper is a programmer who can handel and code the **back end** and **front end** and also get accuainted with version control and project management.\
In all the can completely handel a website and set it up on a server by themself.\
A full stack programmer has knowledge of the following languages...\
1) **HTML**, **CSS** (or any other relevent web designing tools)\
2) **Python** or **ruby** for program scripiting and implimenting function and handeling them in your website.\
3) **SQL** Databse knowledge to crete and manage data.\
4) Knowledge of version control systems like **GIT**.\
5) Also is proficient with one or more server OS mostly **LINUX**.\

## My Full Stack
The aim of this project is to create a website completely from the begining which allows users to type a pre defined coding language that allows them to represent a circuit textually. 
Later on the user can run simulation on these circuit and find the intermidiate values and results.\
\
Steps or Goals to achive this result!

### Website
Programming the website using HTML and styling it using CSS to create a interactive website where the usere is greeted with a login page and later when the username and password is entered\
 is redirected to a page where a text-editor is present. This text editor is a special text editior which understands a specific syntax and language.

#### User Language
This is the languange that the user has to type to replicate a circuit.\
This is a simple languge with a few pre defined syntax.\
**DEFINE**, **END_DEFINITION**, **BEGIN**, **END_BEGIN**, **GND**, **PVCC**, **NVCC**, **CONNECT**, **REQUEST**, **VOLTAGE**, **CURRENT**, **RES**, **CAP**, **IND**, **DIO**, **Place** etc.\
\
An example of of this language used to represent a voltage divider circuit would be :\
\
DEFINE voltage_divider_1()\
	place PVCC(vcc_1, 5V).\
	Place NVCC(vcc_1_N, 5V).\
	place RES(res_1, 1k).\
	place RES(res_2, 1k).\
	CONNECT(net_0, vcc_1, res_1).\
	CONNECT(net_1, res_1, res_2).\
	CONNECT(net_2, res_2, vcc_1_N)\
END_DEFINITION\

BEGIN voltage_divider()\
	/#The script which handels the circuit is placed here.#/
	REQUEST VOLTAGE(res_2)
	REQUEST CURRENT(res_1)
END_BEGIN
\
Very simple code and intial phase of language the language has to be complimented with diffrent functionality for better and wider range of circuit representation and simulation.\

### Website functions handler.
Using python language to handel login task and simulation tasks. python scripts will be set up to run as users would interact with the website and this is sent back to the website displaying the results.\

### Server
The website is set up and run on a linux server using pi clusters to create the server, since this is the begining phase only a few users are allowed to use the website at a 
time so that it does not crashes.\

### Version Control
All revisions made to the website and background scripts are stored in a repo so that proper troubleshooting and maintenance of the website can be done.




