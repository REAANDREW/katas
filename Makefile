.PHONY: python
python:
	nosetests ./python/

.PHONY: test
test: python
