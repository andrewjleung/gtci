make:
	python3 -m venv .venv; \
	source .venv/bin/activate; \
	pip install -r requirements.txt \
	pip install -e .

clean:
	rm -rf .venv __pycache__ src.egg-info .pytest_cache && rm -f pyvenv.cfg .cache
	