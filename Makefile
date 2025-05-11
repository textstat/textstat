.PHONY: dist

install:
	python setup.py install

test:
	pipenv run pytest tests/

style:
	pipenv run flake8 . --exclude=build/,.venv --max-line-length=88

clean:
	rm -rf build/ dist/ textstat.egg-info/ __pycache__/ **/__pycache__/
	rm -f **/*.pyc **/*.pyc

dist:
	pipenv run python3 setup.py sdist bdist_wheel

upload:
	pipenv run twine upload dist/*

