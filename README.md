# **TaskNinja CLI**
This is a CLI created exclusively to superficially demonstrate how the [Task Ninja API](https://github.com/Javierdiaz1386/TaskNinja) works.

## **Use**

To test its operation, I designed a simple terminal application with which you can make use of TASKNINJA APIs.

## **Requirements before installing TASKNINJA CLI**

To use TaskNinja CLI you must have python installed and you must install its "CLICK" library.

#### **Instalation CLICK:**

To install CLICK we will use the "PIP" python package installer.

```shell
$ pip install click
```
# **Instalation TaskNinja CLI**

First of all you have to clone the repository

It's just a .py file.

```shell
$ git clone https://github.com/Javierdiaz1386/TaskNinjaCLI.git
```
## **How to use TaskNinja CLI**
### **Linux**
Tutorials on how TaskNinja CLI works.

### **Sign In**
First we will start by registering with the API using the **user register** command as shown in the following example.

When using the user register command, it will ask you for some data which you must provide for the creation of your user.


```shell
$ ./TaskNinja.py user register
> Enter your username: "You will enter the desired username"
> Enter your full name: "Your full name"
> Enter your email: "Your email adress"
> Enter your password: "Make your password"
>> "If no error occurs, the data of the created user will be displayed on the screen."
```
### **Create Task**
Having a registered user now you can create your tasks and immediately they will be saved in the database, you will be able to access them at any time.

Creating a task is done using the **task create** command as shown below.

When using the **task create** command, it will ask you for some data which you must provide for the creation of your task.

```shell
$ ./TaskNinja.py task create
> Username "Your username"
> Password "Your Pasword"
> Write the subject of the task to create "This is the affair"
>> "If there is no error, the created task will be displayed on the screen."
```

### **List all tasks**
To list the tasks we use the task alltask command, this command will ask us for our username and password to list all the tasks that belong to us.

```shell
$ ./TaskNinja.py task alltask
> Usuario: "Your username"
> Password: "Your Password"
> "It will list all our tasks" 
```

### **Update Task**
To update the information of a task we use the **task update** command.

When executing it, it will ask you for information which you must provide so that there is no error.

First this command will show you all your tasks and you must choose the task you want to delete with its respective id.

```shell
$ ./TaskNinja.py task update
> Username: "Your username"
> Password: "Your password"
>> "The CLI will show all your tasks giving you the option to choose one to update."
> Enter the new subject for this area: "This new affair"
>> "If there are no errors, a message will be displayed on the screen confirming the operation."
```
### **Delete Task**
To delete the tasks we must use the **task delete** command, when executing the command it will show us our tasks and we must select the task to delete according to its id.

```shell
$ ./TaskNinja.py task delete
> Username: "Your username"
> Password: "Your password"
>> "The CLI will show all your tasks giving you the option to choose one to delete."
>> "If there are no errors, a message will be displayed on the screen confirming the operation."
```

### ***on windows coming soon***

