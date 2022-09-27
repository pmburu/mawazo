#!/usr/bin/env bash

if [ -n "$DEBUG" ]; then
	set -x
fi

set -o errexit
set -o nounset
set -o pipefail

POETRY_HOME="${POETRY_HOME:=${HOME}/.local/share/pypoetry}"
POETRY_BINARY="${POETRY_BINARY:=${POETRY_HOME}/venv/bin/poetry}"
echo "[metrics] Run mawazo PEP 8 checks."
"$POETRY_BINARY" run flake8 --select=E,W,I --max-line-length 80 --import-order-style pep8 --statistics --count mawazo
echo "[metrics] Run mawazo PEP 257 checks."
"$POETRY_BINARY" run flake8 --select=D --ignore D301 --statistics --count mawazo
echo "[metrics] Run mawazo pyflakes checks."
"$POETRY_BINARY" run flake8 --select=F --statistics --count mawazo
echo "[metrics] Run mawazo code complexity checks."
"$POETRY_BINARY" run flake8 --select=C901 --statistics --count mawazo
echo "[metrics] Run mawazo open TODO checks."
"$POETRY_BINARY" run flake8 --select=T --statistics --count mawazo tests
echo "[metrics] Run mawazo black checks."
"$POETRY_BINARY" run black -l 80 --check mawazo
