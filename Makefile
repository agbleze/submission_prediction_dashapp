MODULE := dashapp

run:
	@python -m $(MODULE)

test:
	@pytest

.PHONY: clean test

clean:
		rm -rf .pytest_cache .coverage .pytest_cache coverage.xml

