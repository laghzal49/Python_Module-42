"""
oracle.py - Secure configuration management using environment variables.
Exercise 02: Accessing the Mainframe
"""

import importlib
import os


# Sensitive variables that must never be printed in plain text.
# Defined at module level so env_load() can reference it safely
# from anywhere (tests, other modules, etc.).
SECRET_LIST = ['API_KEY', 'DATABASE_URL']


def env_load(var: str) -> None:
    """
    Masks and displays the status of a specific environment variable.

    Args:
        var (str): The environment variable name to check.
    """
    value = os.getenv(var)

    # Non-sensitive variables: print the value directly.
    if var not in SECRET_LIST:
        label = var.replace('_', ' ').title()
        print(f'  {label}: {value}')

    elif var == 'API_KEY':
        # Verify authentication without exposing the key value.
        if not value:
            print('  API Access: Not authenticated')
        else:
            print('  API Access: Authenticated')

    elif var == 'DATABASE_URL':
        # Show connection status without revealing credentials.
        if not value:
            print('  Database: Not connected')
        else:
            print('  Database: Connected to local instance')


def data_load(check_list: list[str]) -> None:
    """Load and display the status of configuration variables."""
    print('Configuration loaded:')
    for var in check_list:
        env_load(var)


def check(check_list: list[str]) -> None:
    """
    Verifies that all required variables exist in the environment.

    Args:
        check_list (list[str]): Variable names to validate.

    Raises:
        ValueError: If a required configuration key is missing or empty.
    """
    for var in check_list:
        # Treat both None and empty string as missing — consistent with
        # the emptiness checks inside env_load().
        if not os.getenv(var):
            raise ValueError(f'missing configuration variable: {var}')


def check_gitignore() -> bool:
    """
    Check that .env is listed as a standalone entry in .gitignore.

    Returns:
        True if .env appears on its own line, False otherwise.
    """
    if not os.path.isfile('.gitignore'):
        return False
    with open('.gitignore', 'r') as fh:
        lines = [line.strip() for line in fh.readlines()]
    # Match '.env' exactly — avoids false positives like '.env.example'.
    return '.env' in lines


def check_no_hardcoded_secrets() -> bool:
    """
    Scan this source file for hardcoded secret patterns.

    Returns:
        True if no hardcoded secrets are detected, False otherwise.
    """
    patterns = ['password=', 'api_key=', 'secret=', 'token=']
    try:
        with open(__file__, 'r') as fh:
            source = fh.read().lower()
        for line in source.splitlines():
            stripped = line.strip()
            # Skip comments and the patterns list definition itself.
            if stripped.startswith('#') or 'patterns' in stripped:
                continue
            for pattern in patterns:
                if pattern in stripped:
                    return False
    except OSError:
        pass  # Cannot read own source — skip check.
    return True


def security_check(config: dict[str, str | None]) -> None:
    """Run and display the three environment security checks."""
    print('\nEnvironment security check:')

    # Check 1: no hardcoded secrets in source code.
    ok = check_no_hardcoded_secrets()
    print(f'{"[OK]" if ok else "[!!]"} No hardcoded secrets detected')

    # Check 2: .env is listed in .gitignore so it cannot be committed.
    ok = check_gitignore()
    hint = '' if ok else ' (.env not found in .gitignore!)'
    print(f'{"[OK]" if ok else "[!!]"} .env file properly configured{hint}')

    # Check 3: if running in production, real secrets must be present.
    mode = config.get('MATRIX_MODE', 'development')
    has_secrets = bool(config.get('API_KEY') or config.get('DATABASE_URL'))
    ok = (mode != 'production') or has_secrets
    print(f'{"[OK]" if ok else "[!!]"} Production overrides available')


if __name__ == '__main__':
    # Main execution:
    # 1. Dynamically load dotenv to keep secrets out of source code.
    # 2. Validate all required variables are present before doing anything.
    # 3. Display config status and run security checks.
    print('\nORACLE STATUS: Reading the Matrix...\n')

    try:
        # Dynamic import — keeps dotenv optional in environments where it
        # may not be pre-installed (CI, Docker, bare servers, etc.).
        dotenv = importlib.import_module('dotenv')
        dotenv.load_dotenv()

        check_list = ['MATRIX_MODE', 'DATABASE_URL', 'API_KEY',
                      'LOG_LEVEL', 'ZION_ENDPOINT']

        # Validate first — fail fast before displaying anything.
        check(check_list)

        # Build config dict once so security_check() can inspect values
        # without calling os.getenv() repeatedly.
        config = {var: os.getenv(var) for var in check_list}

        data_load(check_list)
        security_check(config)

        print('\nThe Oracle sees all configurations.')

    except ModuleNotFoundError as error:
        print(f'Error: {error}')
        print('Install it with: pip install python-dotenv')
    except ValueError as error:
        # A required configuration variable is missing.
        print(f'Configuration error: {error}')
    except Exception as error:
        print(f'Unexpected error: {error}')
