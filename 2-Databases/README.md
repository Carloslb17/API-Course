# Establish a connection between Database and FastAPI. 

This section contains a guide to how the main Python code interacts with the database created in PostgreSQL. 

## 1 - Setting Up.

To set up your environment for FastAPI development:

#### Install Psycopg in your virtual environment or Python interpreter location:

The documentation to set up the connection to your database in this case we used Postgres: <link>https://www.psycopg.org/docs/install.html</link>


    ```python
     pip install psycopg2

     import psycopg2

    
## 
In this section, we'll discuss the use of Database Management Systems (DBMS) in our project.

### DBMS

Is not usual to work with databases directly. Instead, we make use of software referred to as a Database Management System (DBMS). There are two main categories of DBMS that we may encounter:

#### Relational DBMS

Relational DBMS uses structured tables with rows and columns to store and manage data. Common examples include:

- MySQL
- PostgreSQL 
- Oracle
- SQL Server

#### NoSQL DBMS

NoSQL DBMS, as the name suggests, does not rely on a fixed schema and is more flexible in handling unstructured data. Common examples include:

- MongoDB
- DynamoDB
- Oracle (yes, it supports NoSQL as well)
- SQL Server (also supports NoSQL)

## Installation of PostgreSQL

The course uses PostgreSQL as the relational DBMS, follow these steps to install it:

### 1. **Windows:**

   - Visit the official PostgreSQL website: [PostgreSQL Downloads](https://www.postgresql.org/download/windows/)
   - Download the installer for Windows.
   - Run the installer and follow the on-screen instructions.
   - After installation, make sure to add the PostgreSQL `bin` directory to your system's PATH environment variable.

### 2. **macOS:**

   - You can use Homebrew to install PostgreSQL. If you don't have Homebrew, you can install it from [Homebrew's website](https://brew.sh/).
   - Open a terminal and run the following command to install PostgreSQL:

     ```
     brew install postgresql
     ```

   - Follow any additional instructions provided by Homebrew.

### 3. **Linux (Ubuntu/Debian):**

   - Open a terminal and run the following commands:

     ```
     sudo apt update
     sudo apt install postgresql postgresql-contrib
     ```

   - The second command installs both PostgreSQL and some additional utilities.

### 4. **Linux (CentOS/RedHat):**

   - Open a terminal and run the following commands:

     ```
     sudo yum install postgresql-server postgresql-contrib
     sudo postgresql-setup initdb
     sudo systemctl enable postgresql
     sudo systemctl start postgresql
     ```

   - These commands install PostgreSQL, initialize the database cluster, and start the PostgreSQL service.

After installing PostgreSQL, you can interact with it using the command-line tool `psql` or connect to it using various programming languages and frameworks.

For more detailed information on using PostgreSQL, refer to the [PostgreSQL Documentation](https://www.postgresql.org/docs/).

