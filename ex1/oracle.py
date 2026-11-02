import os
import sys

try:
    from dotenv import load_dotenv
except ImportError:
    print("ORACLE STATUS: python-dotenv is not installed")
    print("Install it with: pip install -r ex1/requirements.txt")
    sys.exit(1)

REQUIRED = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
]

LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR"]


def mask(secret: str, visible: int = 0) -> str:
    """Hide a secret, optionally leaving the first few characters visible."""
    if not secret:
        return "(empty)"
    if visible <= 0 or len(secret) <= visible * 2:
        return "*" * 8
    return secret[:visible] + "*" * 8


def load_config() -> dict:
    """Load .env (real environment variables take priority) and read config."""
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    loaded = load_dotenv(env_path, override=False)
    config: dict = {name: os.environ.get(name) for name in REQUIRED}
    config["_dotenv_loaded"] = loaded
    return config


def report_missing(config: dict) -> list:
    """Return the list of missing variables."""
    return [name for name in REQUIRED if not config.get(name)]


def show_development(config: dict) -> None:
    print("MODE: development")
    print("Debug output enabled - values are shown for easier testing.")
    print()
    print(f"Database : {config['DATABASE_URL']}")
    print(f"API key  : {mask(config['API_KEY'], visible=3)}")
    print(f"Log level: {config['LOG_LEVEL']}")
    print(f"Zion     : {config['ZION_ENDPOINT']}")


def show_production(config: dict) -> None:
    print("MODE: production")
    print("Strict mode - sensitive values are hidden.")
    print()
    print(f"Database : {mask(config['DATABASE_URL'])}")
    print(f"API key  : {mask(config['API_KEY'])}")
    print(f"Log level: {config['LOG_LEVEL']}")
    print(f"Zion     : {config['ZION_ENDPOINT']}")


def main() -> None:
    config = load_config()

    print("ORACLE STATUS: Reading the matrix...")
    if config["_dotenv_loaded"]:
        print("Source: .env file + environment variables")
    else:
        print("Source: environment variables only (no .env file found)")
    print()

    missing = report_missing(config)
    if missing:
        print("Missing configuration:")
        for name in missing:
            print(f"  [MISSING] {name}")
        print()
        print("To fix it, copy the template and fill in your values:")
        print("  cp ex1/.env.example ex1/.env")
        print("Or export them directly, e.g.:")
        print("  export MATRIX_MODE=development")
        sys.exit(1)

    mode = config["MATRIX_MODE"].strip().lower()
    level = config["LOG_LEVEL"].strip().upper()
    config["LOG_LEVEL"] = level

    if level not in LOG_LEVELS:
        print(f"WARNING: unknown LOG_LEVEL '{level}'. "
              f"Expected one of: {', '.join(LOG_LEVELS)}")
        print()

    if mode == "development":
        show_development(config)
    elif mode == "production":
        show_production(config)
    else:
        print(f"ERROR: MATRIX_MODE must be 'development' or 'production', "
              f"got '{config['MATRIX_MODE']}'")
        sys.exit(1)

    print()
    print("The Oracle sees all. Configuration loaded safely.")


if __name__ == "__main__":
    main()