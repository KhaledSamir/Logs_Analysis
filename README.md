#Logs-Analysis Project

### Project Overview
>  In this project , am running some queries on Python DB API to generate reports about three main questions :
  ###### 1. What are the most popular three articles of all time?
  ###### 2. Who are the most popular article authors of all time?
  ###### 3. On which days did more than 1% of requests lead to errors?

### How to Run?

#### PreRequisites:  
  * [Python3](https://www.python.org/)
  * [Vagrant](https://www.vagrantup.com/)
  * [VirtualBox](https://www.virtualbox.org/)

#### Setup Project:
  1. Install Vagrant and VirtualBox
  2. Download or Clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository.
  3. Download the [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) from here
     and copy to local folder.
  4. Unzip this file after downloading it. The file inside is called newsdata.sql.

#### Launching the Virtual Machine:
  1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command:

  ```
    $ vagrant up
  ```
  2. Then Log into this using command:

  ```
    $ vagrant ssh
  ```
  3. Change directory to /vagrant and look around with ls.

#### Setting up the database and Creating Views:

  1. Load the data in local database using the command:

   - ```psql -d news -f newsdata.sql ```

  The database includes three tables:
  * Authors
  * Articles
  * Log

  2. Start psql by using ``` > psql ``` and then hit Enter.

  3. Use `\c news` to connect to database.

  4. You'll need to create a view by running following script:
  ```
          CREATE view articleView as
          Select ar.title , ar.slug , count(path) as Views , ar.author from log
          Join articles ar
          ON log.path like concat('%' , ar.slug)
          Group by ar.title , ar.slug , ar.author
          Order by count(path) desc
  ```

#### Running the queries:
  1. From the vagrant directory inside the virtual machine
  2. ``` cd LogsApp ```
  3. ``` $ python Logs.py ```
