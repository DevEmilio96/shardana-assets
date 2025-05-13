import os
from PIL import Image

# Estensioni supportate
SUPPORTED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']

def convert_to_webp(root_folder):
    for root, _, files in os.walk(root_folder):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in SUPPORTED_EXTENSIONS:
                full_path = os.path.join(root, file)
                try:
                    with Image.open(full_path) as img:
                        # Imposta output path
                        new_filename = os.path.splitext(full_path)[0] + '.webp'
                        img.save(new_filename, 'webp')
                        print(f"✅ Converted: {full_path} → {new_filename}")
                except Exception as e:
                    print(f"❌ Failed to convert {full_path}: {e}")

# Esegui lo script
if __name__ == '__main__':
    folder_path = input("Inserisci il percorso della cartella da convertire: ").strip()
    if os.path.isdir(folder_path):
        convert_to_webp(folder_path)
    else:
        print("❗ Percorso non valido.")
