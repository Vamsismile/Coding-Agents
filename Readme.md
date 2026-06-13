# Coding-Agents Workspace

A collection of coding projects and AI agents.

## Projects

### dummy-project

A minimal Python testing project.
***********************************
- **Location**: `./dummy-project/`
- **Language**: Python 3.12+
- **Main**: `app.py` — simple entrypoint that prints a message
- **Tests**: `test_app.py` — test suite with pytest

#### Quick Start

```bash
cd dummy-project
python app.py
pytest test_app.py -v
```

#### Dependencies

Install from `requirements.txt`:

```bash
pip install -r dummy-project/requirements.txt
```

## CI/CD: GitHub Actions

### CI Workflow (Implemented)

- [x] Create `.github/workflows/ci.yml`
- [x] Configure pytest to run on push/PR
- [x] Add linting (flake8)
- [x] Add code coverage reporting
- [ ] Add automated test badge to README

### Example Workflow (To-Do)

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r dummy-project/requirements.txt
      - name: Run tests
        run: pytest dummy-project/ -v --cov
```

## Structure

```
Coding-Agents/
├── README.md
├── .git/
└── dummy-project/
    ├── app.py
    ├── test_app.py
    ├── requirements.txt
    ├── .gitignore
    └── README.md
```

## Next Steps

1. Set up GitHub Actions workflow for CI
2. Add code coverage tracking
3. Add linting and formatting checks
4. Configure branch protection rules
