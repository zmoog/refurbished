.PHONY:

sources = cli/* refurbished tests
line_length = 79
black_options = --line-length=${line_length} ${sources}
isort_options = --line-length=${line_length} --py 310 --profile black ${sources}

lint: lint-black lint-isort lint-flake8  ## Lint the project on the host

lint-black:
	black --diff --check ${black_options}

lint-isort:
	isort --diff --check ${isort_options}

lint-flake8:
	# stop the build if there are Python syntax errors or undefined names
	flake8 ${sources} --count --select=E9,F63,F7,F82 --show-source --statistics
	# exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
	flake8 ${sources} --count --exit-zero --max-complexity=10 --max-line-length=${line_length} --statistics

fix-lint: fix-black fix-isort  ## Fix linting

fix-black:
	@black ${black_options}

fix-isort:
	@isort ${isort_options}

test:
	pytest tests

ready: lint test ## Make sure we're ready to ship the code in a PR
