VENV    = .venv
POETRY  = poetry

.PHONY: usage
usage:
	@echo "Usage: ${MAKE} Target"
	@echo ""
	@echo "Targets:"
	@echo "  init		init directory"
	@echo "  run            run script"
	@echo "  lint           run flake8"
	@echo "  clean		clean current directory"

.PHONY: init
init:
	${MAKE} -s ${VENV}

${VENV}:
	${POETRY} install

.PHONY: run
run: ${VENV}
	${POETRY} run hinatablogimg

.PHONY: lint
lint: ${VENV}
	${POETRY} run flake8 hinatablogimg/

requirements.txt:
	${VENV}/bin/python -m pip freeze > requirements.txt

.PHONY: clean
clean:
	rm -rf ${VENV}
