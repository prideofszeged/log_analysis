# Udacity Log Analysis Project
This project's goal is to create an internal reporting tool that uses Python and SQL to extract information from a database and draw conclusions from that information.

__Note__: This project is part of the Udacity Full Stack Web Developer Nanodegree program. 

## Introduction
The provided database contains newspaper articles, as well as the web server logs for a fictitious newspater site. The database has three tables:
* The __authors__ table includes information about the authors of articles.
* The __articles__ table includes the articles themselves.
* The __log__ table includes one entry for each time a user has accessed the site.

#### So what are we reporting, anyway?
* Most popular three articles of all time. Present this as a sorted list with the most popular arcticle at the top.
* Most popular article authors of all time. When you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
* Days on which more than 1% of requests lead to errors. Derived from the date and HTTP status code the news site sent to the users's brower.

## Instructions
* [Download and install Vagrant](https://www.vagrantup.com/). This may require a reboot of your workstation.

* [Download and install Virtualbox](https://www.virtualbox.org/wiki/Downloads") virtual machine manager.

* Clone this Github repository to your local machine:
  <pre>git clone https://github.com/prideofszeged/log_analysis</pre>

* Start the virtual machine by following these steps:
  1. From your terminal, inside the project 'vagrant' directory, run the command `vagrant up`. This command will download, install, and do some basic configuration of an Ubuntu 16.04 virtual machine. This may take several minutes.
  2. When the previous step has finished, run 'vagrant ssh' so connect to your new virtual machine. Be sure you are in the 'vagrant' folder when you run this command. 

* Download the database zip file, which contains the sql file needed to create the database. [Data provided by Udacity](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it and put it in your vagrant folder.

* Import Data
  To load the database use the following command:
  <pre>psql -d news -f newsdata.sql;</pre>

* Run the python program to extract the required data.
  <pre>python log.py</pre>

### Functions in log.py:
* __connect():__ Connects to the PostgreSQL database and returns a connection.
* __pop_art():__ Displays the most popular three articles of all time.
* __pop_auth():__ Prints most popular article authors of all time.
* __log_err():__ Shows the days where more than 1% of requests lead to errors.
