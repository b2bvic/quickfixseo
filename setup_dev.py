#!/usr/bin/env python3
"""
QuickFixSEO - Development Environment Setup
A product of Scale With Search (https://scalewithsearch.com)
Created by Victor Valentine Romo (@b2bvic)

This script helps set up your local development environment while keeping
personal files separate from the open source repository.
"""

import os
import shutil
from pathlib import Path
import sys

def create_dev_config():
    """Create a personalized dev_config.py from the example"""
    example_path = Path("dev_config.py.example")
    config_path = Path("dev_config.py")
    
    if config_path.exists():
        print("✅ dev_config.py already exists")
        return True
    
    if not example_path.exists():
        print("❌ dev_config.py.example not found")
        return False
    
    # Copy example to actual config
    shutil.copy(example_path, config_path)
    print("✅ Created dev_config.py from example")
    
    # Prompt user to customize
    print("\n📝 Please edit dev_config.py to customize for your environment:")
    print("   • Update OBSIDIAN_VAULT_PATH to your vault location")
    print("   • Update REFERENCE_FILES paths to your local files")
    print("   • Adjust FEATURE_FLAGS as needed")
    
    return True

def create_directories():
    """Create necessary directories for development"""
    directories = [
        "core",
        "core/analyzers", 
        "core/reporters",
        "core/utils",
        "cli",
        "cli/commands",
        "tests",
        "tests/core",
        "docs",
        "docs/examples",
        "scripts",
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        
        # Create __init__.py files for Python packages
        if not directory.startswith(('docs', 'scripts', 'tests')):
            init_file = Path(directory) / "__init__.py"
            if not init_file.exists():
                init_file.touch()
    
    print("✅ Created directory structure")

def create_requirements_files():
    """Create requirements files for different environments"""
    
    # Core requirements (open source)
    core_requirements = """# QuickFixSEO - Core Requirements
requests>=2.28.0
beautifulsoup4>=4.11.0
lxml>=4.9.0
urllib3>=1.26.0
textstat>=0.7.0
python-dateutil>=2.8.0
"""
    
    # Development requirements
    dev_requirements = """# QuickFixSEO - Development Requirements
# Include core requirements
-r requirements.txt

# Development tools
pytest>=7.0.0
pytest-cov>=4.0.0
black>=22.0.0
flake8>=5.0.0
mypy>=0.991
pre-commit>=2.20.0

# Documentation
mkdocs>=1.4.0
mkdocs-material>=8.5.0

# Optional dependencies for development
pandas>=1.5.0  # For CSV analysis
jupyter>=1.0.0  # For data exploration
"""
    
    # Pro requirements (additional dependencies)
    pro_requirements = """# QuickFixSEO - Professional Features Requirements
# Include core requirements
-r requirements.txt

# Advanced analysis
scikit-learn>=1.1.0
nltk>=3.7
spacy>=3.4.0

# Database support
sqlalchemy>=1.4.0
alembic>=1.8.0

# API framework
fastapi>=0.85.0
uvicorn>=0.18.0

# Cloud integrations
google-api-python-client>=2.65.0
google-auth>=2.12.0

# Reporting
reportlab>=3.6.0
jinja2>=3.1.0
"""
    
    # Write requirements files
    files = {
        "requirements.txt": core_requirements,
        "requirements-dev.txt": dev_requirements,
        "requirements-pro.txt": pro_requirements,
    }
    
    for filename, content in files.items():
        with open(filename, 'w') as f:
            f.write(content)
    
    print("✅ Created requirements files")

def create_contributing_guide():
    """Create contributing guidelines"""
    contributing_content = """# Contributing to AUTO SEO

Thank you for your interest in contributing to AUTO SEO! This guide will help you get started.

## 🚀 Quick Start

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/auto-seo.git
   cd auto-seo
   ```
3. **Set up development environment**:
   ```bash
   python setup_dev.py
   pip install -r requirements-dev.txt
   ```
4. **Create a branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 🏗️ Development Setup

### Local Configuration
- Copy `dev_config.py.example` to `dev_config.py`
- Customize paths and settings for your environment
- Your `dev_config.py` won't be committed (it's gitignored)

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=auto_seo

# Run specific test file
pytest tests/test_core/test_crawler.py
```

### Code Quality
```bash
# Format code
black auto_seo/

# Check linting
flake8 auto_seo/

# Type checking
mypy auto_seo/
```

## 📝 Contribution Guidelines

### Core vs Pro Features
- **Core Features**: Open source, MIT licensed
- **Pro Features**: Proprietary, separate licensing

### What We Accept
- ✅ Bug fixes for core functionality
- ✅ Performance improvements
- ✅ Documentation improvements
- ✅ New core SEO analysis features
- ✅ Test coverage improvements
- ❌ Pro features (these are developed separately)

### Code Standards
- Follow PEP 8 style guidelines
- Add type hints where possible
- Include docstrings for public functions
- Write tests for new functionality
- Update documentation as needed

## 🐛 Reporting Issues

### Bug Reports
Include:
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages/logs

### Feature Requests
- Describe the use case
- Explain why it belongs in core vs pro
- Provide examples if possible

## 📋 Pull Request Process

1. **Update documentation** if needed
2. **Add tests** for new functionality
3. **Ensure all tests pass**
4. **Follow commit message conventions**:
   ```
   feat: add new title tag analyzer
   fix: resolve canonical tag detection bug
   docs: update installation guide
   test: add coverage for content analysis
   ```
5. **Submit pull request** with clear description

## 🤝 Community

- **GitHub Discussions**: For questions and ideas
- **Issues**: For bugs and feature requests
- **Discord**: [Community chat] (coming soon)

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License for core features.

---

Thank you for helping make AUTO SEO better! 🚀
"""
    
    with open("CONTRIBUTING.md", 'w') as f:
        f.write(contributing_content)
    
    print("✅ Created CONTRIBUTING.md")

def setup_git_hooks():
    """Set up git hooks for development"""
    pre_commit_config = """# AUTO SEO - Pre-commit Configuration
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-merge-conflict

  - repo: https://github.com/psf/black
    rev: 22.10.0
    hooks:
      - id: black
        language_version: python3

  - repo: https://github.com/pycqa/flake8
    rev: 5.0.4
    hooks:
      - id: flake8
        args: [--max-line-length=88, --extend-ignore=E203]

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v0.991
    hooks:
      - id: mypy
        additional_dependencies: [types-requests]
"""
    
    with open(".pre-commit-config.yaml", 'w') as f:
        f.write(pre_commit_config)
    
    print("✅ Created pre-commit configuration")

def main():
    """Main setup function"""
    print("🚀 Setting up AUTO SEO development environment...\n")
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ is required")
        sys.exit(1)
    
    # Run setup steps
    steps = [
        ("Creating directory structure", create_directories),
        ("Creating development config", create_dev_config),
        ("Creating requirements files", create_requirements_files),
        ("Creating contributing guide", create_contributing_guide),
        ("Setting up git hooks", setup_git_hooks),
    ]
    
    for description, func in steps:
        print(f"📦 {description}...")
        try:
            func()
        except Exception as e:
            print(f"❌ Failed: {e}")
            continue
    
    print("\n🎉 Development environment setup complete!")
    print("\n📋 Next steps:")
    print("1. Edit dev_config.py to match your local setup")
    print("2. Install dependencies: pip install -r requirements-dev.txt")
    print("3. Install pre-commit hooks: pre-commit install")
    print("4. Run tests to verify setup: pytest")
    print("5. Start developing! 🚀")

if __name__ == "__main__":
    main() 