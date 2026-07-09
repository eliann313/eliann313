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

# Ensure output directory exists
os.makedirs('assets/badges', exist_ok=True)

# Retrieve user-level stats for follower/public repo badges
def write_simple_svg(path, left_text, right_text, color="#4c1"):
    # simple two-part badge SVG
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="220" height="20">
  <linearGradient id="b" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <rect rx="3" width="220" height="20" fill="#555"/>
  <rect rx="3" x="110" width="110" height="20" fill="{color}"/>
  <path fill="{color}" d="M110 0h4v20h-4z"/>
  <g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11">
    <text x="55" y="14">{left_text}</text>
    <text x="165" y="14">{right_text}</text>
  </g>
</svg>'''
    with open(path, 'w', encoding='utf-8') as f:
        f.write(svg)

# get user stats
user_url = 'https://api.github.com/users/eliann313'
try:
    r = requests.get(user_url, headers=HEADERS, timeout=10)
    if r.status_code == 200:
        jd = r.json()
        followers = str(jd.get('followers', 0))
        public_repos = str(jd.get('public_repos', 0))
    else:
        followers = 'N/A'
        public_repos = 'N/A'
except Exception:
    followers = 'N/A'
    public_repos = 'N/A'

write_simple_svg('assets/badges/followers.svg', 'Followers', followers, color='#24292e')
write_simple_svg('assets/badges/public-repos.svg', 'Public repos', public_repos, color='#0366d6')

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
    except Exception:
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
    except Exception:
        date_str = 'error'

    OUT.append((repo_id, lang_str, date_str))

    # write static svg badges per repo
    safe_name = f"{owner}-{repo}".replace('/', '-')
    lang_svg_path = f"assets/badges/{safe_name}-lang.svg"
    commit_svg_path = f"assets/badges/{safe_name}-commit.svg"
    write_simple_svg(lang_svg_path, 'Top language', lang_str, color='#007ec6')
    write_simple_svg(commit_svg_path, 'Last commit', date_str, color='#2b9348')

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

print('STATS.md and static SVG badges updated')
