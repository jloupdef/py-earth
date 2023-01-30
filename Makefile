PYTHON ?= python
CYTHON ?= cython
PYTEST ?= pytest
CYTHONSRC=$(wildcard pyearth/*.pyx)
CSRC=$(CYTHONSRC:.pyx=.c)

inplace: cython
	$(PYTHON) setup.py build_ext -i --cythonize

all: inplace

cython: $(CSRC)

clean:
	rm -f pyearth/*.c pyearth/*.so pyearth/*.pyc pyearth/test/*.pyc pyearth/test/basis/*.pyc pyearth/test/record/*.pyc

%.c: %.pyx
	$(CYTHON) $<

test: inplace
	$(PYTEST) -s pyearth

test-coverage: inplace
	$(PYTEST) -s --with-coverage --cover-html --cover-html-dir=coverage --cover-package=pyearth pyearth

verbose-test: inplace
	$(PYTEST) -sv pyearth

conda:
	conda-build conda-recipe
