# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Enhanced CI/CD pipeline with linting, type checking, and security audits
- Comprehensive CONTRIBUTING.md guide for collaboration
- MAINTENANCE.md documenting release and maintenance processes
- ROADMAP.md outlining future development directions
- Pre-commit hook configuration for automated code quality checks
- Coverage reporting in CI pipeline via Codecov
- Security vulnerability scanning with pip-audit
- Dedicated release workflow for trusted publishing to PyPI/TestPyPI from version tags
- Binary wheels for CPython 3.12–3.14 on Linux (x86_64, aarch64), macOS 11+ (x86_64, arm64), and Windows (x86_64), built with cibuildwheel, so `pip install` no longer needs a Fortran compiler

### Fixed
- Dropped the `timeutil` runtime dependency: it is no longer on PyPI, which made `pip install pyhwm2014` fail; the library never imported it (only `scripts/pyhwmapps.py` does)
- HWM14 data files are now found when the install path is longer than 128 characters (previously the Fortran code printed "Can not find file" and exited the interpreter)
- A missing HWM14 data file no longer ends the Python process with exit status 0: `import pyhwm2014` raises `FileNotFoundError` naming the missing files, and the Fortran fallback now uses `ERROR STOP` (non-zero exit) instead of `STOP`

### Changed
- Updated GitHub Actions versions (v3 → v4, v4 → v5)
- Improved CI workflow organization (separate lint, test, security jobs)
- Release documentation now follows dynamic `setuptools_scm` versioning (tag-driven, no manual pyproject version edits)

### Deprecated
- (None at this time)

### Removed
- (None at this time)

### Security
- Added automated security audit during CI pipeline

## [1.1.0] - 2026-02-15

### Added
- Full type hint coverage with mypy strict mode
- Comprehensive test suite covering all major functionality
- PyPI publishing with automated CI/CD pipeline
- Support for Python 3.13
- Modern build system (scikit-build-core)
- API documentation with docstrings

### Fixed
- Initial release of pyHWM14 package

## [Previous]

See GitHub releases for historical versions: https://github.com/rilma/pyHWM14/releases
