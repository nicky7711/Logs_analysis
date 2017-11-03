# Logs_analysis
## Project Description
Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.
## Prerequisite
* Python 2 or 3, and psycopg2 module in Python
* Virtual Box
* Vagrant
### Setup
1. Install Python, Virtual Box, and Vagrant
2. Download the VM configuration from [here](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip), or clone or download Udacity repository from [here](https://github.com/udacity/fullstack-nanodegree-vm)
3. Download required data from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip it, and put it in VM configuration directory
### Start the Virtual Machine
1. Open your terminal and set directory to VM configuration directory
2. Setup Vagrant by running *vagrant up*
3. Login to VM by running *vagrant ssh*
4. Set the directory to where main python file is
### Running database
Simply use *psql* command
## Run the file
Execute main file by running *python logs_analysis_query.py*
## Note
Setting up Vagrant may take a lot of time, just because the file is big.
