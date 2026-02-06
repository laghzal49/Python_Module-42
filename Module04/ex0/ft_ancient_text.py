def opening() -> None:
    """
    Accesses the ancient_fragment.txt vault and recovers all data fragments.
    This function handles the connection, prints formatted fragments,
    and ensures the storage unit is disconnected safely.
    """
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    try:
        file = open("ancient_fragment.txt", 'r')
        print("Accessing Storage Vault: ancient_fragment.txt")
        print("Connection established...\n")
        content: str = file.read()
        print(content)
        file.close()
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
    print("\nData recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    opening()
