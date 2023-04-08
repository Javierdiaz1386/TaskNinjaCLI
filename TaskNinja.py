#!/bin/python3
import click
import requests
import json

token = ""


@click.group()
def cli():
    """TaskNinja CLI\n
Create tasks and save them in the cloud
    """
    pass


@cli.group()
def user():
    """
    Here you can register using the user register command
    """
    pass


@user.command()
@click.option("--username", prompt="Enter your username ")
@click.option("--full_name", prompt="Enter your full name ")
@click.option("--email", prompt="Enter your email ")
@click.option("--password", prompt="Enter your password ")
def register(username, password, email, full_name):
    try:
        user = requests.post("https://taskninja.onrender.com/user/create", data=json.dumps({
            "username": username,
            "full_name": full_name,
            "password": password,
            "email": email,
            "disable": "false"
        }))
        click.echo(json.loads(user.text))
    except:
        print("User already exists")


@cli.group(help="Create, Delete, Update or See your taks")
def task():
    pass


@task.command()
@click.option('--username', prompt='Usuario: ')
@click.option('--password', prompt='Password: ')
def create(username, password):
    try:
        affair = input("Write the subject of the task to create: ")
        login = requests.post('https://taskninja.onrender.com/user/login',
                              data={"username": username, "password": password})
        token = json.loads(login.text)["access_token"]
        crear = requests.post('https://taskninja.onrender.com/tasks/create', data=json.dumps(
            {"affair": affair}), headers={"Authorization": f'Bearer {token}'})
        click.echo(crear.text)
    except:
        print("Make sure you enter the login details correctly.")


@task.command()
@click.option('--username', prompt='Usuario: ', help="your username")
@click.option('--password', prompt='Password: ', help="your password")
def delete(username, password):
    try:
        login = requests.post('https://taskninja.onrender.com/user/login',
                              data={"username": username, "password": password})
        token = json.loads(login.text)["access_token"]
        task = requests.get('https://taskninja.onrender.com/tasks/all',
                            headers={"Authorization": f'Bearer {token}'})
        task = json.loads(task.text)["task"]
        for num, tasks in enumerate(task):
            click.echo(

                f' id: {num} \n Name: {tasks["name"]} \n Username: {tasks["username"]} \n Affair: {tasks["affair"]} \n {"-"*50}'
            )

    except:
        print("Invalid login")
        exit()

    try:
        borrar = int(input("Enter the id of the task to delete: "))
        req = requests.delete(f'https://taskninja.onrender.com/tasks/delete/{task[borrar]["id"]}', headers={
            "Authorization": f'Bearer {token}'})
        click.echo(req.text)
    except:
        print("Id invalid")


@task.command()
@click.option('--username', prompt='Usuario: ', help="Your username")
@click.option('--password', prompt='Password: ', help="Your Password")
def alltask(username, password):
    try:
        login = requests.post('https://taskninja.onrender.com/user/login',
                              data={"username": username, "password": password})
        token = json.loads(login.text)["access_token"]
        task = requests.get('https://taskninja.onrender.com/tasks/all',
                            headers={"Authorization": f'Bearer {token}'})
        task = json.loads(task.text)["task"]
        if len(task) > 0:
            for num, tasks in enumerate(task):
                click.echo(

                    f' id: {num} \n Name: {tasks["name"]} \n Username: {tasks["username"]} \n Affair: {tasks["affair"]} \n {"-"*50}'
                )
        else:
            click.echo("You have no saved task")

    except:
        print("Invalid Login")
        exit()


@task.command()
@click.option('--username', prompt='Usuario: ')
@click.option('--password', prompt='Password: ')
def update(username, password):
    try:
        login = requests.post('https://taskninja.onrender.com/user/login',
                              data={"username": username, "password": password})
        token = json.loads(login.text)["access_token"]
        task = requests.get('https://taskninja.onrender.com/tasks/all',
                            headers={"Authorization": f'Bearer {token}'})
        task = json.loads(task.text)["task"]
        for num, tasks in enumerate(task):
            click.echo(

                f' id: {num} \n Name: {tasks["name"]} \n Username: {tasks["username"]} \n Affair: {tasks["affair"]} \n {"-"*50}'
            )
    except:
        print("Invalid Login")
        exit()
    try:
        update = int(input("Enter the id of the task to update: "))
        affair = input("Enter the new subject for this area: ")
        req = requests.put(f'https://taskninja.onrender.com/tasks/update/{task[update]["id"]}', json.dumps({"affair": affair}), headers={
            "Authorization": f'Bearer {token}'})
        click.echo(req.text)
    except:
        print("Id invalido")


if __name__ == '__main__':
    cli()
