# simple-notebooks

# setup
**step 1:** clone git repo
```sh
git clone git@github.com:tranhuucuong91/simple-notebooks.git
```

**step 2:** create virtualenv
```sh
cd simple-notebooks

virtualenv venv

source venv/bin/activate
```

**step 3:** install packages
```sh
# install python packages
pip3 install -r requirements.txt

# install web packages
bower install
```

**step 4:** copy default config and modify
```sh
cp config_default.py config.py
```

**step 5:** create database if don’t exist
```sh
./db_create.py
```

**step 6:** run app
```sh
./run.py
```

