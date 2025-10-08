import os
import json

def generate_podcast_json(base_path='.'):
    podcasts = []
    for root, dirs, files in os.walk(base_path):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            index_path = os.path.join(folder_path, 'index.html')
            if os.path.isfile(index_path):
                relative_path = os.path.relpath(index_path, base_path)
                podcasts.append({
                    "title": folder.replace('-', ' ').replace('_', ' '),
                    "path": relative_path.replace('\\', '/')
                })

    with open('podcasts.json', 'w', encoding='utf-8') as f:
        json.dump(podcasts, f, indent=2, ensure_ascii=False)

    print(f"Generated podcasts.json with {len(podcasts)} entries.")

generate_podcast_json()
