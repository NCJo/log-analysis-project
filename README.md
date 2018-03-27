# Log Analysis

This is a reporting tools designed to potentially provide comprehensive answers to many business questions, which derived from gathered database of a certain website logs.

### Tech

Log Analysis relies on several packages to be able to successfully run :

* Python3
* Virtual Box - VM environment
* Vagrant - Configuration program

### Installation

1.) Install VirtualBox from this [website](https://www.virtualbox.org/wiki/Downloads)
2.) Install Vagrant from this [website](https://www.vagrantup.com/downloads.html)
3.) Vagrant takes a configuration file called *Vagrantfile* that tells it how to start your Linux VM. Download the Vagrantfile [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f73b_vagrantfile/vagrantfile)

### How to run
1.) Download the code or clone a repository from GitHub (To clone a repo, type the code below in the terminal)
```sh
$ git clone https://github.com/NCJo/log-analysis-project
```
2.) Navigate to the repository folder
3.) Start virtual machine by run the following command in the directory
```sh
$ vagrant up
```
follow by
```sh
$ vagrant ssh
```
4.) Download the database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
5.) Set up database by running this command
```sh
$ psql -d news -f newsdata.sql
```
6.) Get results by running
```sh
$ python3 newsdata.py
```
