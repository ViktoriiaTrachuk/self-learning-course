.PHONY: setup
setup:
	python3 -m venv venv
	cd victests
	pip install -r requirements.txt
reports:
	mkdir "reports"

.PHONY: run_test
run_test:
	pytest --junitxml=reports/"result.xml"

.PHONY: clean
clean:
	rm -rf venv
	rm -f result.xml





