# AgentLabBench

A benchmark for profiling AI agent capabilities across diverse real-world tasks.

## Overview

AgentLabBench evaluates AI agents on 16 sealed tasks spanning:
- **Web Shopping** - Product finding and comparison
- **Travel Planning** - Multi-constraint itinerary planning  
- **Retail Operations** - Inventory and substitution management
- **Fact QA** - Multi-hop question answering
- **Code Generation** - API usage and implementation
- **Code Review** - Bug detection and suggestion
- **Data Analysis** - Pandas-based analysis tasks
- **Debugging** - Error identification and fixing
- **Entity Extraction** - Named entity recognition
- **Question Answering** - Reading comprehension
- **Sentiment Analysis** - Text classification
- **SQL Generation** - Query writing
- **Summarization** - Text condensation
- **Text Generation** - Creative writing
- **Translation** - Multi-language translation
- **API Integration** - REST API interaction

## Structure

```
agentslabench/
├── code/                    # Benchmark implementation
│   ├── tasks/              # 16 task environments (Docker-based)
│   ├── sealed_tests/       # Sealed test sets with SHA256 verification
│   ├── runner.py           # Evaluation runner
│   ├── run_docker_eval.py  # Docker-based evaluation
│   ├── baselines.py        # Baseline agents (ReAct, CoT, Plan-and-Solve, Reflexion)
│   ├── judge_calibration.py # Human-LLM judge calibration
│   ├── pyproject.toml      # Python dependencies
│   ├── requirements.txt    # Minimal requirements
│   └── results/            # Key evaluation results
├── paper/                  # ICML 2026 paper
│   ├── agentslabench_icml.tex
│   ├── agentslabench_icml.pdf
│   ├── references.bib
│   ├── icml2026.sty/.bst   # ICML style files
│   └── figures/            # Paper figures
└── compile.sh              # Paper compilation script
```

## Quick Start

```bash
# Install dependencies
pip install -r code/requirements.txt

# Run a baseline evaluation
cd code
python run_docker_eval.py --task web_shopping --agent react

# Compile paper
./compile.sh
```

## Paper

The ICML 2026 submission is in `paper/`:
- `agentslabench_icml.tex` - Main LaTeX source
- `agentslabench_icml.pdf` - Compiled PDF
- `figures/` - Profile concept and step breakdown figures

## Sealed Tests

Test sets are in `code/sealed_tests/` with SHA256 hashes in `MANIFEST.json` to prevent data contamination. Each task has:
- `*_test.jsonl` - Sealed test set (2000 samples)
- `*_challenge.jsonl` - Challenge set for calibration

## Results

Key results in `code/results/`:
- `final_paper5_results.jsonl` - Final 5-core-task evaluation
- `final_core5_eval.jsonl` - Core task results
- `judge_calibration.jsonl` - Human-LLM agreement data
- `human_judge_spotcheck_*.jsonl` - Human verification

## Citation

```bibtex
@inproceedings{agentslabench2026,
  title={AgentLabBench: A Benchmark for Profiling AI Agent Capabilities},
  author={...},
  booktitle={Proceedings of the 43rd International Conference on Machine Learning (ICML)},
  year={2026}
}
```
