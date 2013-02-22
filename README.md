To install/update all Python dependencies:
  sudo pip install -U -r requirements.txt 

To create/update the database schema:
  cd src
  alembic upgrade head

How to run the project production (background):
  cd src
  cherryd -d -i init

  To kill it:  pkill cherryd

How to run the project development (foreground):
  cd src
  ./init.py

  To kill it:  press ctrl c

How to run the project's unittests:
  cd test
  ./test.py
