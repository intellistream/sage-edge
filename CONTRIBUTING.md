# Contributing to SAGE Edge

We welcome contributions! Please follow these guidelines:

## Development Setup

```bash
git clone https://github.com/intellistream/sage-edge.git
cd sage-edge
pip install -e .[dev]
```

## Guidelines

- Follow PEP 8 style guide
- Use Ruff for linting: `ruff check src/`
- Run tests before submitting: `pytest tests/ -v`
- Update CHANGELOG.md for notable changes

## Pull Request Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

For detailed guidelines, see [SAGE Contributing Guide](https://github.com/intellistream/SAGE/blob/main/CONTRIBUTING.md).
