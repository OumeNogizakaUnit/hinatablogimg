VENV    = .venv
POETRY  = poetry

.PHONY: usage
usage:
	@echo "Usage: ${MAKE} Target"
	@echo ""
	@echo "Targets:"
	@echo "  init		init directory"
	@echo "  clean		clean current directory"

.PHONY: init
init:
	${MAKE} -s ${VENV}

${VENV}:
	${POETRY} install

.PHONY: clean
clean:
	rm -rf ${VENV}
