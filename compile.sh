#!/bin/bash
set -e
apt-get update -qq
apt-get install -qq -y wget
wget -q https://raw.githubusercontent.com/icml/icml-latex/main/icml2024.sty -O icml2026.sty
pdflatex agentslabench_icml.tex
bibtex agentslabench_icml
pdflatex agentslabench_icml.tex
pdflatex agentslabench_icml.tex
