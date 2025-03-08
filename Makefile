.PHONY: dist

install:
	python setup.py install

test:
	pipenv run pytest test.py

style:
	pipenv run pycodestyle textstat/
	pipenv run pycodestyle test.py

clean:
	rm -rf build/ dist/ textstat.egg-info/ __pycache__/ */__pycache__/
	rm -f *.pyc */*.pyc

dist:
	pipenv run python3 setup.py sdist bdist_wheel

upload:
	pipenv run twine upload dist/*

