## Projects manager for Nginx

This pack of scripts allow you to manage new or existing Nginx virtual host configuration files and its root directories.

### Prerequisites

* [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* [HomeBrew](https://brew.sh)
* [Installed Nginx using HomeBrew](https://formulae.brew.sh/formula/nginx#default)

<br>

#### Clone project

```shell
$ git clone https://github.com/sergey-gr/pmfn.git $HOME/custom_scripts
```

<br>

#### Set project path to your PATH variable to make script accessible globally.

* After this quit terminal.app and open it again

```shell
$ echo -e "export PATH=$PATH:$HOME/custom_scripts" >> ~/.zshrc
```

<br>

#### Usage:

Run command `project` in your terminal

```shell
$ project
Usage: project create|delete|list <project_name>
```