def archive(filename: str) -> None:
    """
    Inscribes new quantum discoveries into the Archives.
    Authorized for 'w' mode operations.
    """
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {filename}")

    try:
        file = open(filename, 'w')
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")

        entries: list = [
            "New quantum algorithm discovered",
            "Efficiency increased by 347%",
            "Archived by Data Archivist trainee"
        ]

        for i, text in enumerate(entries, 1):
            entry_string = f"[ENTRY {i:03}] {text}"
            file.write(entry_string + "\n")
            print(entry_string)
        file.close()

        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{filename}' ready for long-term preservation.")

    except FileNotFoundError:
        print("CRITICAL SYSTEM ERROR:FileNotFoundError")
    except PermissionError:
        print("CRITICAL SYSTEM ERROR: PermissionError")
    except Exception as e:
        print(f"CRITICAL SYSTEM ERROR: {e}")


if __name__ == "__main__":
    filename: str = "new_discovery.txt"
    archive(filename)
