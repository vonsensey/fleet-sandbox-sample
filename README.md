# Fleet Sandbox sample — the AWS U12 non-Rails validation target

## Usage

```python
from greet import greet

greet()              # "Hello from the Fleet Sandbox!"
greet("Ali")         # "Hello Ali from the Fleet Sandbox!"
greet("Ali", loud=True)  # "HELLO ALI FROM THE FLEET SANDBOX!"
```

- `greet(name=None)` greets the world by default, or `name` when given.
- `loud=True` uppercases the greeting.

## Running the tests

```sh
python -m pytest
```
