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

### CI Workflow (Implemented) ✅

- [x] Create `.github/workflows/ci.yml`
- [x] Configure pytest to run on push/PR
- [x] Add linting (flake8)
- [x] Add code coverage reporting
- [x] Multi-version Python testing (3.10, 3.11, 3.12)

**Triggers**: On push to `main` and pull requests

### CD Workflow (Implemented) ✅

- [x] Create `.github/workflows/cd.yml`
- [x] Build package distribution
- [x] Create GitHub releases on version tags
- [x] Publish to PyPI (optional)
- [x] Deployment notifications

**Triggers**: On version tags (`v*`)

**Steps**:
1. **Build**: Creates Python package distribution
2. **Create Release**: Generates GitHub release with tag
3. **Publish to PyPI**: Uploads package (requires PyPI token)
4. **Notification**: Confirms deployment completion

To deploy:
```bash
# Create a version tag
git tag v0.1.0
git push origin v0.1.0
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

1. ✅ Set up GitHub Actions workflow for CI
2. ✅ Set up GitHub Actions workflow for CD
3. Configure PyPI credentials in GitHub Secrets (for publishing)
4. Add code coverage badge to README
5. Configure branch protection rules
6. Set up automated versioning/changelog
