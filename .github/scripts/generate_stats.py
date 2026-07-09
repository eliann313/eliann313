import os
import requests
from datetime import datetime

TOKEN = os.environ.get('GITHUB_TOKEN')
HEADERS = {'Authorization': f'token {TOKEN}'} if TOKEN else {}

REPOS = [
    ('eliann313','SkillRadar'),
    ('Juamp1Sch','WMS'),
    ('Antonio-sharp-plus','Pochocleando'),
    ('bunicodea','proyecto-pokedex'),
    ('eliann313','ProyectoInmuebles'),
]

OUT = []

for owner, repo in REPOS:
    repo_id = f"{owner}/{repo}"
    lang_url = f"https://api.github.com/repos/{owner}/{repo}/languages"
    commits_url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=1"
    try:
        lang_r = requests.get(lang_url, headers=HEADERS, timeout=30)
        if lang_r.status_code == 200:
            langs = lang_r.json()
            total = sum(langs.values()) or 1
            top = max(langs.items(), key=lambda x: x[1]) if langs else (None,0)
            top_lang = top[0] if top[0] else 'N/A'
            pct = round((top[1]/total)*100,1) if total else 0
            lang_str = f"{top_lang} ({pct}%)"
        else:
            lang_str = 'private or unavailable'
    except Exception as e:
        lang_str = 'error'

    try:
        c_r = requests.get(commits_url, headers=HEADERS, timeout=30)
        if c_r.status_code == 200 and isinstance(c_r.json(), list) and c_r.json():
            c = c_r.json()[0]
            date = c.get('commit', {}).get('committer', {}).get('date')
            if date:
                dt = datetime.fromisoformat(date.replace('Z','+00:00'))
                date_str = dt.date().isoformat()
            else:
                date_str = 'unknown'
        else:
            date_str = 'private or unavailable'
    except Exception as e:
        date_str = 'error'

    OUT.append((repo_id, lang_str, date_str))

# Write STATS.md
lines = [
    '# Generated repo stats',
    f'Updated: {datetime.utcnow().date().isoformat()}',
    '',
    '| Repo | Top language | Last commit |',
    '|---|---:|---|',
]
for repo_id, lang_str, date_str in OUT:
    lines.append(f'| {repo_id} | {lang_str} | {date_str} |')

content = '\n'.join(lines) + '\n'
with open('STATS.md','w',encoding='utf-8') as f:
    f.write(content)

print('STATS.md updated')
