test:
	cd app && .venv/bin/python -m pytest -s tests

check:
	cd app && .venv/bin/python -m py_compile server.py

server:
	cd app && .venv/bin/python server.py

production-server:
	cd app && .venv/bin/waitress-serve --call server:create_app

venv:
	cd app && python3 -m venv .venv
	cd app && .venv/bin/pip install -r requirements.txt