# Symptom Diary

A privacy-first health symptom tracking PWA for chronic conditions. Track symptoms, wellness scores, and identify patterns—all on your device, no accounts required.

## Features

- **Quick-Log Symptoms**: Tap from a grid of 15 common symptoms (headache, fatigue, nausea, dizziness, joint pain, etc.)
- **Severity Tracking**: Rate each symptom 1-10 with visual color coding (green/yellow/red)
- **Time of Day**: Log when symptoms occur (morning, afternoon, evening, night)
- **Notes**: Add optional details for each symptom
- **Custom Symptoms**: Add your own symptoms to the grid
- **Daily Wellness Score**: Track your overall wellness (1-10) each day
- **Dashboard**:
  - Today's logged symptoms as color-coded pills
  - This week's top 5 most frequent symptoms with counts
  - 7-day wellness score trend chart
  - 30-day symptom calendar heatmap
- **History**: Browse all logged symptoms by date
- **Export**: Download all data as CSV
- **localStorage**: All data stays on your device

## Design

- Dark theme with sand/gold accents (#c4a882)
- Cormorant Garamond (headers) + Inter (body)
- Responsive design for mobile and tablet
- Onboarding overlay on first visit

## Price

$3.99 one-time purchase

Undercuts competitors:
- Bearable: $50/year
- Symple: $5/month

## Technical

- Single-file HTML/CSS/JS PWA
- Service worker for offline support
- localStorage for persistent data
- Canvas charts for wellness trends
- No external dependencies beyond Google Fonts

## Files

- `index.html` — Complete app (single file)
- `manifest.json` — PWA metadata
- `sw.js` — Service worker (cache-first strategy)
- `generate-icons.py` — Icon generator (health cross visual)
- `icon-180.png`, `icon-192.png`, `icon-512.png` — App icons

## Deploy

```bash
# Generate icons
python3 generate-icons.py

# Commit and push
git add -A
git commit -m "feat: description"
git push

# Enable Pages (one-time)
gh api repos/gcicc/symptom-diary/pages -X POST \
  -f "build_type=legacy" \
  -f "source[branch]=master" \
  -f "source[path]=/"
```

Live at: https://gcicc.github.io/symptom-diary/

## Privacy

- No tracking, no analytics
- No accounts or login
- No data collection
- No unnecessary permissions
- All data stored locally on your device

## Data

Example log entry:
```json
{
  "date": "2026-04-12",
  "symptom": "Headache",
  "severity": 7,
  "time": "afternoon",
  "notes": "Started after lunch, worse with bright light"
}
```

Export as CSV and analyze trends in your own tools.
