# Changelog

All notable changes to SAGE Edge will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Configuration file support (edge.yaml)
- Multiple gateway instances mounting
- Load balancing support
- Metrics endpoint

## [0.1.0] - 2026-01-15

### Added
- 🎉 Initial release as independent package
- FastAPI aggregator shell for mounting SAGE Gateway
- Default mounting at `/` with path preservation
- Custom prefix support via `--llm-prefix`
- Health check endpoints (`/healthz`, `/readyz`)
- CLI entrypoint `sage-edge`
- Environment variable configuration
- XDG-compliant user paths for logs/state
- Comprehensive documentation and examples

### Features
- ✅ Mount complete Gateway application (Control Plane, RAG, Sessions)
- ✅ Preserve `/v1/*` OpenAI-compatible endpoints
- ✅ Flexible deployment (with/without Gateway mounting)
- ✅ Production-ready logging and error handling
- ✅ Python 3.10+ support

### Dependencies
- `isage-llm-gateway>=0.1.0` - SAGE LLM Gateway
- `isage-llm-core>=0.2.0` - Control Plane client
- `isage-common>=0.2.0` - Common utilities
- `fastapi>=0.115.0` - Web framework
- `uvicorn[standard]>=0.34.0` - ASGI server

### Documentation
- Complete README with usage examples
- Architecture diagram
- Configuration guide
- Comparison: Edge vs Gateway

---

## Migration from SAGE Monorepo

Prior to v0.1.0, `sage-edge` was part of the [SAGE monorepo](https://github.com/intellistream/SAGE). This release marks its independence as a standalone package.

**Breaking Changes**: None (API remains identical)

**Migration Guide**:
```bash
# Old (monorepo install)
pip install -e packages/sage-edge

# New (PyPI install)
pip install isage-edge
```

---

[Unreleased]: https://github.com/intellistream/sage-edge/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/intellistream/sage-edge/releases/tag/v0.1.0
