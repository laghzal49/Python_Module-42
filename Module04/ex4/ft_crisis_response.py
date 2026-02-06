def ft_crisis_response() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    files: list[tuple[str, str]] = [
        ("lost_archive.txt", "r"),
        ("classified_vault.txt", "r"),
        ("standard_archive.txt", "r")
    ]
    for file, perm in files:
        try:
            with open(file, perm) as op:
                content = op.read()
                print(f"ROUTINE ACCESS: Attempting access to '{file}'...")
                print(f"SUCCESS: Archive recovered - ``{content.strip()}''")
                print("STATUS: Normal operations resumed\n")

        except FileNotFoundError:
            print(f"CRISIS ALERT: Attempting access to '{file}'...")
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable\n")

        except PermissionError:
            print(f"CRISIS ALERT: Attempting access to '{file}'...")
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained\n")

        except Exception as e:
            print(f"CRISIS ALERT: Attempting access to '{file}'...")
            print(f"RESPONSE: Unexpected error - {e}")
            print("STATUS: Crisis handled, system stable\n")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_crisis_response()
