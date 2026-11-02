import os
import site
import sys


def in_virtualenv() -> bool:
    return sys.prefix != sys.base_prefix


def get_site_packages() -> str:
    try:
        paths = site.getsitepackages()
    except AttributeError:
        paths = []
    if paths:
        for path in paths:
            if path.startswith(sys.prefix):
                return path
        return paths[0]
    version = f"python{sys.version_info.major}.{sys.version_info.minor}"
    return os.path.join(sys.prefix, "lib", version, "site-packages")


def show_outside() -> None:
    print("LABORATORY STATUS: You are working in the open")
    print()
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected")
    print()
    print("WARNING: You are in the global environment!")
    print("Every reagent you install here leaks into the whole system.")
    print()
    print("To seal the laboratory, run:")
    print("python3 -m venv lab_env")
    print("source lab_env/bin/activate    # On Unix")
    print("lab_env\\Scripts\\activate       # On Windows")
    print()
    print("Then run this program again.")


def show_inside() -> None:
    venv_path = os.environ.get("VIRTUAL_ENV", sys.prefix)
    print("LABORATORY STATUS: The laboratory is sealed")
    print()
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {os.path.basename(venv_path)}")
    print(f"Environment Path: {venv_path}")
    print()
    print("SUCCESS: You are working in an isolated environment!")
    print("Safe to install reagents without affecting the global system.")
    print()
    print(f"Reagent installation path: {get_site_packages()}")


def main() -> None:
    if in_virtualenv():
        show_inside()
    else:
        show_outside()


if __name__ == "__main__":
    main()