def vault_security(f1: str, f2: str) -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")

    try:
        with open(f1, "w") as vault:
            vault.write("Quantum encryption keys recovered\n")
            vault.write("Archive integrity: 100%\n")

        print("Vault connection established with failsafe protocols\n")
        print("SECURE EXTRACTION:")

        with open(f1, "r") as vault:
            for line in vault:
                print(f"[CLASSIFIED] {line}", end="")

        print("\n\nSECURE PRESERVATION:")

        with open(f2, "w") as log:
            log.write("New security protocols archived\n")

        print("[CLASSIFIED] New security protocols archived")
        print("Vault automatically sealed upon completion\n")
        print("All vault operations completed with maximum security.")

    except FileNotFoundError:
        print("CRITICAL ERROR: Storage vault file not found.")
    except PermissionError:
        print("CRITICAL ERROR: Permission denied for vault access.")
    except Exception as e:
        print(f"UNEXPECTED SYSTEM THREAT: {e}")


if __name__ == "__main__":
    vault_security("vault_data.txt", "security_log.txt")
