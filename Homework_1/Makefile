.PHONY: setup:
setup:
	python3 -m venv venv
	cd victests
	pip install -r requirements.txt
reports:
	mkdir "reports"

.PHONY: run test
run_test: setup
	pytest --junitxml=reports/"result.xml"

.PHONY: clean
clean:
	rm -rf venv
	rm -f result.xml













#
reports/junit-e2e.xml \
ifndef COMMENT
PHONY: install-ui-tests-deps
install-ui-tests-deps:
	cd ui-tests && \
	pip install -r requirements.txt

PHONY: run-ui-tests
run-ui-tests: install-ui-tests-deps
	@./ui-tests/run-ui-tests.sh

.PHONY: run-qa-ui-tests
run-qa-ui-tests:
	@if [ "$(DOCUMENT_AI_FE_USER_PASSWORD)" = "" ]; then echo "DOCUMENT_AI_FE_USER_PASSWORD must be set"; exit 1; fi
	@if [ "$(DOCUMENT_AI_FE_USER_NAME)" = "" ]; then echo "DOCUMENT_AI_FE_USER_NAME must be set"; exit 1; fi
	@$(MAKE) TEST_APP_URL=https://document-ai.cloud-qa.h2o.ai TEST_USERNAME=$(DOCUMENT_AI_FE_USER_NAME) TEST_PASSWORD=$(DOCUMENT_AI_FE_USER_PASSWORD) run-ui-tests
.PHONY: test-e2e
test-e2e: reports
	mkdir -p reports/allure reports
"""
endif # COMMENT







