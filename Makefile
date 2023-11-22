create-env:
	virtualenv -p `which python3.7` env

install-dependencies:
	pip install -r requirements.txt

