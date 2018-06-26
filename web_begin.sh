#source web_begin.sh # should run this code in terminal

. venv/bin/activate
export FLASK_APP=web_test
export FLASK_DEBUG=1
flask run

#deactivate
