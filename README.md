# CFA Python Practice

Workspace for learning Python fundamentals alongside the CFA curriculum.

## Layout

- `exercises/` – practice scripts (start with `tvm.py`, time value of money)
- `tests/` – pytest checks for the exercises
- `requirements.txt` – numpy, pandas, matplotlib, pytest, ruff

## Commands

```bash
pip install -r requirements.txt   # automatic in Claude Code on the web
python exercises/tvm.py           # run an exercise
pytest                            # run all tests
ruff check .                      # lint (style / common mistakes)
```
