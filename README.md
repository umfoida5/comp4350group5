CardioQuest
===========

Test Status:

[![Build Status](https://travis-ci.org/umfoida5/comp4350group5.png?branch=master)](https://travis-ci.org/umfoida5/comp4350group5)

Setup
-----
To install/update all Python dependencies:
<pre>
sudo pip install -U -r requirements.txt
</pre>

To create/update the database schema:
<pre>
cd src
alembic upgrade head
</pre>

Run the project
---------------
To run the project production (background):
<pre>
cd src
cherryd -d -i init
</pre>

Then to kill it:
<pre>
pkill cherryd
</pre>

To run the project development (foreground):
<pre>
cd src
./init.py
</pre>

Then to kill it:
<pre>
press ctrl c
</pre>

Tests
-----

To run the project's unittests:
<pre>
cd test
./test.py
</pre>
