import os
import json

def generate_podcast_json(base_path='.'):
    podcast_dirs = [
        d for d in os.listdir(base_path)
        if os.path.isdir(os.path.join(base_path, d)) and not d.startswith('.') and d != '.git'
    ]

    podcasts = []
    for folder in podcast_dirs:
        index_path = os.path.join(folder, 'index.html')
        if os.path.exists(index_path):
            podcasts.append({
                "title": folder.replace('-', ' ').replace('_', ' '),
                "path": f"{folder}/index.html"
            })

    with open('podcasts.json', 'w', encoding='utf-8') as f:
        json.dump(podcasts, f, indent=2, ensure_ascii=False)

generate_podcast_json()
