from integrity import save_hash, verify_integrity


FILE_PATH = "data/test.txt"


print("=== File Integrity Checker ===")
print()
print("1. Register file")
print("2. Check file integrity")

choice = input("Choose an option: ")


if choice == "1":
    file_hash = save_hash(FILE_PATH)

    print("\nFile registered successfully!")
    print(f"SHA-256: {file_hash}")


elif choice == "2":
    result, info = verify_integrity(FILE_PATH)

    if result is None:
        print(f"\n{info}")

    elif result:
        print("\n✅ File integrity intact.")
        print(f"Current SHA-256: {info}")

    else:
        print("\n⚠️ WARNING: File has been modified!")
        print(f"Current SHA-256: {info}")

else:
    print("\nInvalid option.")