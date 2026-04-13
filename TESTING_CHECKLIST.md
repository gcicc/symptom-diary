# Symptom Diary — Testing Checklist

**Live at:** https://gcicc.github.io/symptom-diary/

## Quick Test Guide

### Log Tab
- [ ] Open app on mobile phone
- [ ] Onboarding overlay appears on first visit
- [ ] Click "Get Started" to dismiss
- [ ] Tap wellness score slider (1-10) — should update display
- [ ] Tap a symptom pill (e.g., "Headache") — should highlight and show details
- [ ] Adjust severity slider in details (should update)
- [ ] Select a time of day (4 buttons)
- [ ] Type optional notes
- [ ] Click "Save Symptom" — should log and show confirmation
- [ ] Clear button should reset without saving
- [ ] Add another symptom the same day
- [ ] Scroll to see all symptom pills

### Dashboard Tab
- [ ] Today's Symptoms section shows pills with color coding (green/yellow/red by severity)
- [ ] Top 5 symptoms shows this week's most frequent with counts
- [ ] Wellness trend chart displays 7-day trend with dots
- [ ] Calendar heatmap shows 30 days with intensity/numbers
- [ ] Add symptom on Log tab, refresh Dashboard — new symptom appears

### History Tab
- [ ] Shows all logged symptoms grouped by date
- [ ] Date header formatted nicely (e.g., "Sunday, Apr 12")
- [ ] Each entry shows: Symptom, severity, time, notes
- [ ] Delete button removes symptom (both from History and data)
- [ ] Refresh confirms deletion

### Settings Tab
- [ ] Custom Symptom input + Add button works
- [ ] Custom symptoms appear as tags with × button
- [ ] Remove custom symptom (×) works immediately
- [ ] CSV Export button downloads file to device
- [ ] CSV format: Date,Symptom,Severity,Time,Notes
- [ ] Reset Data button shows confirmation
- [ ] Confirm reset clears all data

### Data Persistence
- [ ] Log a symptom, close app completely, reopen
- [ ] Symptom still appears in History and Dashboard
- [ ] Wellness score persists
- [ ] Custom symptoms persist
- [ ] Close DevTools, refresh page — data remains

### Design & Responsiveness
- [ ] Colors match spec: bg #0d1117, accent #c4a882
- [ ] Fonts load (Cormorant Garamond headers, Inter body)
- [ ] Dark theme (no bright elements)
- [ ] Works on 4" phone (iPhone SE)
- [ ] Works on 6" phone (iPhone 12)
- [ ] Works on tablet (iPad)
- [ ] All buttons are thumb-reachable
- [ ] No horizontal scrolling needed

### PWA Features
- [ ] Add to Home Screen (iOS: Share → Add to Home Screen)
- [ ] App icon shows correctly on home screen
- [ ] Standalone mode (no browser chrome)
- [ ] Tap icon opens fullscreen
- [ ] Status bar color matches theme

### Performance
- [ ] App loads in <2 seconds on 3G
- [ ] Tab switching is instant
- [ ] Scrolling is smooth (60fps)
- [ ] No console errors

### Offline Support
- [ ] Open DevTools → Network → Offline
- [ ] Existing app works (cached)
- [ ] Can view saved symptoms
- [ ] CSV export still works (downloads from cache)
- [ ] Go back online — all works again

## Bug Tracking

| Issue | Steps | Status | Notes |
|-------|-------|--------|-------|
| — | — | — | — |

## Device Matrix

| Device | iOS Version | Status | Notes |
|--------|------------|--------|-------|
| iPhone 15 | 18 | [ ] | |
| iPhone 12 | 17 | [ ] | |
| iPhone SE | 17 | [ ] | |
| iPad Air | 17 | [ ] | |
| Chrome Mobile | Latest | [ ] | |
| Safari Mobile | Latest | [ ] | |

## Success Metrics

- [ ] Zero JavaScript console errors
- [ ] All data saves correctly to localStorage
- [ ] Offline functionality works
- [ ] CSV export is valid
- [ ] UI is responsive on all screen sizes
- [ ] No accessibility issues (tab navigation works)
- [ ] App feels snappy (<200ms interactions)

---

**Once all checkboxes are complete, mark as "Ready for Beta Testing"**
