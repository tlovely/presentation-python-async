build:
	python3 -m venv env
	./env/bin/pip install -r requirements.txt

server:
	./env/bin/adev runserver server.py 

ipython:
	./env/bin/ipython

mr-server:
	./env/bin/python part_17.py

mr-client:
	nc localhost 1337

part_01:
	./env/bin/python part_01.py

part_02:
	./env/bin/python part_02.py

part_03:
	./env/bin/python part_03.py

part_04:
	./env/bin/python part_04.py

part_05:
	./env/bin/python part_05.py

part_06:
	./env/bin/python part_06.py

part_07:
	./env/bin/python part_07.py

part_08:
	./env/bin/python part_08.py

part_09:
	./env/bin/python part_09.py

part_10:
	./env/bin/python part_10.py

part_11:
	./env/bin/python part_11.py

part_12:
	./env/bin/python part_12.py

part_13:
	./env/bin/python part_13.py

part_14:
	./env/bin/python part_14.py

part_15:
	./env/bin/python part_15.py

part_16:
	./env/bin/python part_16.py

part_17: mr-server