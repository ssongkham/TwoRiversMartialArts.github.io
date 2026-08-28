'''
Per-page context for legacy bodies now rendered under the 2026 chrome.
LEGACY pulls in the old stylesheet and JS so existing markup keeps working;
PAGE_TITLE replaces the banner block layout1 used to render.
Generated from the templates' own banner headings — do not hand-edit lightly.
'''

context = {
  'awards.html':                   { 'LEGACY': True, 'TR_ACTIVE': 'about', 'PAGE_TITLE': 'Awards' },
  'blackbeltlist.html':            { 'LEGACY': True, 'TR_ACTIVE': 'about', 'PAGE_TITLE': 'Black Belt List' },
  'calendar.html':                 { 'LEGACY': True, 'TR_ACTIVE': 'calendar', 'PAGE_TITLE': 'Calendar' },
  'carlisle-videos.html':          { 'LEGACY': True, 'TR_ACTIVE': 'resources', 'PAGE_TITLE': 'Carlisle Branch Videos' },
  'community.html':                { 'LEGACY': True, 'TR_ACTIVE': 'about', 'PAGE_TITLE': 'Community Outreach' },
  'competition.html':              { 'LEGACY': True, 'TR_ACTIVE': 'about', 'PAGE_TITLE': 'Competition' },
  'curriculum.html':               { 'LEGACY': True, 'TR_ACTIVE': 'resources', 'PAGE_TITLE': 'Curriculum' },
  'donate.html':                   { 'LEGACY': True, 'TR_ACTIVE': '', 'PAGE_TITLE': 'Donate to Two Rivers' },
  'donation.html':                 { 'LEGACY': True, 'TR_ACTIVE': '', 'PAGE_TITLE': 'Donate to Two Rivers' },
  'dues.html':                     { 'LEGACY': True, 'TR_ACTIVE': 'resources', 'PAGE_TITLE': 'Black Belt Dues Payment' },
  'history-tkd.html':              { 'LEGACY': True, 'TR_ACTIVE': 'about', 'PAGE_TITLE': 'History of Tae Kwon Do' },
  'history2decades.html':          { 'LEGACY': True, 'TR_ACTIVE': 'about', 'PAGE_TITLE': 'Two Decades Later' },
  'hold-the-mayo.html':            { 'LEGACY': True, 'TR_ACTIVE': 'about', 'PAGE_TITLE': 'Hold the Mayo (Clinic)' },
  'instructors-primary.html':      { 'LEGACY': True, 'TR_ACTIVE': 'about', 'PAGE_TITLE': 'Primary Instructors' },
  'kobudo.html':                   { 'LEGACY': True, 'TR_ACTIVE': 'start', 'PAGE_TITLE': 'Kobudo' },
  'location-carlisle.html':        { 'LEGACY': True, 'TR_ACTIVE': 'classes', 'PAGE_TITLE': 'Branch Location: Carlisle' },
  'location-hub.html':             { 'LEGACY': True, 'TR_ACTIVE': 'classes', 'PAGE_TITLE': 'Branch Location: Two Rivers Hub and Business Office' },
  'location-indianola.html':       { 'LEGACY': True, 'TR_ACTIVE': 'classes', 'PAGE_TITLE': 'Branch Location: Indianola' },
  'location-waukee.html':          { 'LEGACY': True, 'TR_ACTIVE': 'classes', 'PAGE_TITLE': 'Branch Location: Waukee' },
  'location-wdm.html':             { 'LEGACY': True, 'TR_ACTIVE': 'classes', 'PAGE_TITLE': 'Branch Location: Clive/West Des Moines' },
  'location-winterset.html':       { 'LEGACY': True, 'TR_ACTIVE': 'classes', 'PAGE_TITLE': 'Branch Location: Winterset' },
  'locations-trma.html':           { 'LEGACY': True, 'TR_ACTIVE': 'classes', 'PAGE_TITLE': 'Where To Find Us' },
  'martial-spirit.html':           { 'LEGACY': True, 'TR_ACTIVE': 'start', 'PAGE_TITLE': 'Martial Spirit' },
  'memoriam.html':                 { 'LEGACY': True, 'TR_ACTIVE': 'about', 'PAGE_TITLE': 'In Memoriams' },
  'portfolio.html':                { 'LEGACY': True, 'TR_ACTIVE': 'resources', 'PAGE_TITLE': 'Portfolio' },
  'resource-belts.html':           { 'LEGACY': True, 'TR_ACTIVE': 'resources', 'PAGE_TITLE': 'Significance of Belts' },
  'resource-dresscode.html':       { 'LEGACY': True, 'TR_ACTIVE': 'resources', 'PAGE_TITLE': 'Dress Code' },
  'resource-forms.html':           { 'LEGACY': True, 'TR_ACTIVE': 'resources', 'PAGE_TITLE': 'Forms' },
  'resource-photos.html':          { 'LEGACY': True, 'TR_ACTIVE': 'resources', 'PAGE_TITLE': 'Photo Archive' },
  'resource-terminology.html':     { 'LEGACY': True, 'TR_ACTIVE': 'resources', 'PAGE_TITLE': 'Terminology' },
  'resource-videos.html':          { 'LEGACY': True, 'TR_ACTIVE': 'resources', 'PAGE_TITLE': 'Video Archive' },
  'startingtkd.html':              { 'LEGACY': True, 'TR_ACTIVE': 'start', 'PAGE_TITLE': 'How Do I Start' },
  'taichi.html':                   { 'LEGACY': True, 'TR_ACTIVE': 'start', 'PAGE_TITLE': 'Tai Chi' },
  'test-schedule.html':            { 'LEGACY': True, 'TR_ACTIVE': 'resources', 'PAGE_TITLE': 'Test Schedule' },
  'testimonials.html':             { 'LEGACY': True, 'TR_ACTIVE': 'about', 'PAGE_TITLE': 'Testimonials' },
  'tkdt-bbyg.html':                { 'LEGACY': True, 'TR_ACTIVE': 'start', 'PAGE_TITLE': 'Black Belt Youth Group' },
  'torts-to-tkd.html':             { 'LEGACY': True, 'TR_ACTIVE': 'about', 'PAGE_TITLE': 'Torts to Tae Kwon Do' },
  'ybbc.html':                     { 'LEGACY': True, 'TR_ACTIVE': 'start', 'PAGE_TITLE': 'Black Belt Youth Group' },
}
