test:
	cd app && python -m pytest -s tests

check:
	cd app && python -m py_compile server.py

server:
	cd app && python server.py