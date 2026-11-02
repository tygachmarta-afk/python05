import importlib
import sys

REAGENTS = [
    ("pandas", "Data manipulation"),
    ("numpy", "Numerical computation"),
]


def check_reagent(name: str) -> str:
    """Try to import a reagent; return its version, or "" if missing."""
    try:
        module = importlib.import_module(name)
    except ImportError:
        return ""
    return str(getattr(module, "__version__", "unknown"))


def main() -> None:
    print("REAGENT STATUS: Loading reagents...")
    print()
    print("Checking dependencies:")

    missing = []
    for name, purpose in REAGENTS:
        version = check_reagent(name)
        if not version:
            print(f"[MISSING] {name} - {purpose} not available")
            missing.append(name)
        else:
            print(f"[OK] {name} ({version}) - {purpose} ready")

    print()
    print("pip vs Poetry:")
    print("requirements.txt declares what to install; pip resolves it at")
    print("install time. pyproject.toml declares the same constraints, and")
    print("Poetry pins the resolved versions in poetry.lock so every")
    print("install is identical.")
    print()

    if missing:
        print("Some reagents are missing. Install them with:")
        print("  pip:    pip install -r ex0/requirements.txt")
        print("  Poetry: poetry install")
        print("          poetry run python ex0/loading.py")
    else:
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    main()