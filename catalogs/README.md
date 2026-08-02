# Machine-readable catalogs

Release `0.1.0-draft` contains:

- `domains.json/csv`: 20
- `controls.json/csv`: 160
- `tests.json/csv`: 240
- `threats.json/csv`: 100
- `weaknesses.json/csv`: 100

Individual Markdown records are provided in subdirectories. Run:

```bash
python tools/validate_catalogs.py
```

Catalogs are draft and must be used with the Rules of Engagement and system context.
