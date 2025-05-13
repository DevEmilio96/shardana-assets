import os

def delete_png_files(root_folder):
    deleted = 0
    for root, _, files in os.walk(root_folder):
        for file in files:
            if file.lower().endswith('.png'):
                full_path = os.path.join(root, file)
                try:
                    os.remove(full_path)
                    print(f"🗑️ Deleted: {full_path}")
                    deleted += 1
                except Exception as e:
                    print(f"❌ Failed to delete {full_path}: {e}")
    print(f"\n✅ Eliminati {deleted} file .png.")

if __name__ == '__main__':
    folder_path = input("📁 Inserisci il percorso della cartella da pulire: ").strip()
    if os.path.isdir(folder_path):
        confirm = input(f"⚠️ Sei sicuro di voler eliminare TUTTI i .png in '{folder_path}'? (y/n): ").lower()
        if confirm == 'y':
            delete_png_files(folder_path)
        else:
            print("❌ Operazione annullata.")
    else:
        print("❗ Cartella non valida.")
