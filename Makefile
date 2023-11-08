init: ## Initialize Project
	@python3.10 -m venv venv
	@./venv/bin/python3 -m pip install pip==22.3
	@./venv/bin/python3 -m pip install -U pip setuptools wheel pip-tools
	@./venv/bin/python3 -m pip install -r requirements/requirements.txt
	@./venv/bin/python3 -m pip install -r requirements/requirements-dev.txt
	@./venv/bin/python3 -m pip install -e . --no-deps
	@./venv/bin/python3 -m pre_commit install --install-hooks --overwrite

clean:  ## remove build artifacts
	rm -rf build dist venv pip-wheel-metadata htmlcov docs/_build
	find . -name .tox -exec rm -rf {} +
	find . -name __pycache__ -exec rm -rf {} +
	find . -name .pytest_cache -exec rm -rf {} +
	find . -name *.egg-info -exec rm -rf {} +
	find . -name setup-py-dev-links -exec rm -rf {} +
	find docs -name generated -exec rm -rf {} +
	find docs -type f ! -name 'conf.py' ! -name 'index.rst' ! -name 'Makefile' -exec rm -rf {} +

update: clean init

lint: ## Run linters
	@./venv/bin/isort semantic_engine_dev scripts tests
	@./venv/bin/python3 -m black --config=pyproject.toml --check .
	@./venv/bin/python3 -m flake8 --config=.flake8 --per-file-ignores="tests/*.py:D" .

test: lint ## Run tests
	@./venv/bin/pytest -vv --durations=10 --cov-fail-under=90 --cov=semantic_engine_dev --cov-report html tests/

update-requirements: # Update requirements files from setup.py and requirements/requirements-dev.in
	./venv/bin/pip-compile setup.py --extra all requirements/constraints.in --strip-extras \
	--output-file=./requirements/requirements.txt --resolver=backtracking --verbose
	./venv/bin/pip-compile ./requirements/requirements-dev.in \
	--output-file=./requirements/requirements-dev.txt --resolver=backtracking --verbose

upgrade-requirements: # Upgrade requirements files from setup.py and requirements/requirements-dev.in
	./venv/bin/pip-compile setup.py --extra all requirements/constraints.in --upgrade --strip-extras \
	--output-file=./requirements/requirements.txt --upgrade --resolver=backtracking --verbose
	./venv/bin/pip-compile --upgrade ./requirements/requirements-dev.in \
	--output-file=./requirementsr/requirements-dev.txt --resolver=backtracking --verbose

sync-venv: update-requirements ## Sync python environment deletes doc deps
	./venv/bin/pip-sync ./requirements/requirements.txt ./requirements/requirements-dev.txt
	./venv/bin/pip install -e . --no-deps

generate-rst: ## Auto-generate module documentation
	./venv/bin/sphinx-apidoc -o docs/ .

rebuild-notebooks: ## Re-run notebooks for latest outputs
	./venv/bin/python3 src/docs/run-notebooks.py; \
	username=`whoami`; \
	date; \
	for f in $(shell find notebooks/ -type f -name "*.ipynb" | sort); do \
		echo "Scrub username from '$${f}'"; \
		sed -i"" "s/$${username}/jdoe/g" $${f}; \
		date; \
	done

docs-build: generate-rst ## Build docs
	# run sphinx to build docs
	./venv/bin/sphinx-build -c docs/ -w docs.log docs/ docs/_build/html/
	mkdir -p docs/_build/html/_static/notebooks
	cp notebooks/*.ipynb docs/_build/html/_static/notebooks

docs: rebuild-notebooks docs-build ## Build documentation and API docs

serve-docs: docs ## Serve docs in web-browser
	firefox docs/_build/html/index.html
