# epen Project

This is a Python application.

## Prerequisites

This project uses `uv` for fast Python package management and execution.

### Manual Installation of `uv`

If you don't have `uv` installed, you can manually install it using one of the following methods:

**macOS and Linux:**
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

For more installation options, please refer to the [official uv documentation](https://docs.astral.sh/uv/getting-started/installation/).

## Running the App

### Using `uv` (Recommended)

To run the application using `uv`, execute the following command from the root directory of the project:

```sh
uv run game.py.tembakk.py
```

### Using standard `python` and `pip`

First, set up a virtual environment and install the dependencies (like `pygame`):

```sh
python -m venv .venv
# On Linux/macOS
source .venv/bin/activate
# On Windows
.venv\Scripts\activate

pip install pygame-ce
```

Then, run the application using the virtual environment's Python:

```sh
python game.py.tembakk.py
```
