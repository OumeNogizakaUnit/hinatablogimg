VENV    = .venv
POETRY  = poetry

.PHONY: usage
usage:
	@echo "Usage: ${MAKE} Target"
	@echo ""
	@echo "Targets:"
	@echo "  init		init directory"
	@echo "  run            run script"
	@echo "  clean		clean current directory"

.PHONY: init
init:
	${MAKE} -s ${VENV}

${VENV}:
	${POETRY} install

.PHONY: run
run: ${VENV}
	${POETRY} run main

.PHONY: clean
clean:
	rm -rf ${VENV}
