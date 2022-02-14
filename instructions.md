#PROJECT SETUP AND EXECUTION


There are couple of things to do before exectuing this project.  i have converted this projec into a 
project package so it would be easy to execute and navigate but before this we need to set up the 
project environment.

before stepping into the process we need to make sure we have installed `Python` on your system. 
all the commands are perforemed in  `terminal` in `linux` OS, for windows user it could be done in `Windows shell`.


# STEP 1
make sure python is installed and latest version. to confirm. type this command
        
    python -V

the output would be like: make sure python version is `3.X`.
    
    Python 3.9.7

if you see similar output you are good to move to step 2.

# STEP 2
Now we need to create an environemnt to setup our project. for that need need to perform following commands that will create a new environemt directory for our packages. 

    python -m venv env

`env` is the name of the directory. confirm if the new  directory `env` is created in your current directoru (project folder). 

#STEP 3
now we need to activate the environment. it will help use to install and use selenium in our project. 
for `linux` or `Mac OS` users:

    source env/bin/activate

OUTPUT:

    (env) jk@jk-ThinkPad-T470:~/CURENT_DIRECTORY$ 

for `windows`  users:

    .\env\Scripts\activate

output: (it could be as linux output as well.)

    PS jk@jk-ThinkPad-T470:~/CURENT_DIRECTORY$ 


if you reached upto this point you are good to install selenium and execute the project.


# STEP 3 (Selenium Installion)
We need to install all the dependent libraries we have used in the project for that we need to run this command. this will install `selenium` as well. `requirements.txt` file contains all the list of libraries and versions of libraries we have used.


    pip install -r requirements.text


OUTPUT:

    .... 
    Successfully installed async-generator-1.10 attrs-21.4.0 certifi-2021.10.8 cffi-1.15.0 cryptography-36.0.1 h11-0.13.0 idna-3.3 outcome-1.1.0 pyOpenSSL-22.0.0 pycparser-2.21 selenium-4.1.0 sniffio-1.2.0 sortedcontainers-2.4.0 trio-0.19.0 trio-websocket-0.9.2 urllib3-1.26.8 wsproto-1.0.0


# STEP 4
now it's time to execute our test cases. we need to run the `main.py` file it handles rest of the part.


    python main.py

OUTPUT:

    ----------------------------------------------------------------------
    Ran XX test in 2.441s

    OK

if you reached to this point. glad you done it successfully.

# THANKS
