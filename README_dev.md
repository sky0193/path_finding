# Development Information

Here are some usefull tips for developers.

## mypy

### About mypy

Mypy is an optional static type checker for Python that aims to combine the benefits of dynamic (or "duck") typing and static typing. Mypy combines the expressive power and convenience of Python with a powerful type system and compile-time type checking.

### Install mypy

```bash
python3 -m pip install mypy
```

### Call mypy on single file

```bash
mypy grid_controller.py --namespace-packages
```

### Call mypy with config

`mypy.ini` shall be in the folder

```bash
mypy
```