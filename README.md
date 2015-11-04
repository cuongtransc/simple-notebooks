# simple-notebooks

Develop from project https://github.com/coleifer/peewee/tree/master/examples/blog.

## Install dev tools on ubuntu 14.04
**Step 1:** Install `git`
```
sudo apt-get install -y git
```

**Step 2:** Install `pip`, `virtualenv`
```
sudo apt-get install -y python3-pip

sudo pip3 install virtualenv
```

**Step 3:** Install `bower`
```sh
sudo apt-get install -y nodejs npm

cd /usr/bin
sudo ln -s nodejs node

sudo npm install -g bower
```

## Setup simple-notebooks
**Step 1:** Clone git repo
```sh
# clone via https
git clone https://github.com/tranhuucuong91/simple-notebooks.git

# or clone via ssh
git clone git@github.com:tranhuucuong91/simple-notebooks.git
```

**Step 2:** Create virtualenv
```sh
cd simple-notebooks

virtualenv -p python3 venv

source venv/bin/activate
```

**Step 3:** Install packages
```sh
# install python packages
pip3 install -r requirements.txt

# install web packages
bower install
```

**Step 4:** Copy default config and modify
```sh
cp config_default.py config.py
```

**Step 5:** Create database if don't exist
```sh
./db_create.py
```

**Step 6:** Run app
```sh
./run.py
```


## Use simple-notebooks
Login: http://127.0.0.1:5000/login/

Password: `admin@secret`

## License - MIT

