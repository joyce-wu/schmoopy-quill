pull: pull.py
	nohup python pull.py &

clean:
	rm 1.json
	rm 26.json
	rm 16.json
	rm 21.json
	rm 2.json
	rm 31.json
	rm 36.json
	rm 51.json
	rm nohup.out

data:
	rm data.db
