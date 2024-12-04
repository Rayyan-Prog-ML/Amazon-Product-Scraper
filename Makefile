install:
	pip install -r requirements.txt

extract:
	python scripts/extracting_amazon.py

clean:
	python scripts/collect_Amazon.py

run-all: install extract clean
