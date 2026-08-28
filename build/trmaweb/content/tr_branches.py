'''
Branch data for the 2026 redesign: one source of truth for the homepage
summary cards, the Classes & Locations page and the dues table.
Schedules and prices mirror schedule.py / prices.py.
'''

BRANCHES = [
  { 'key': 'hub', 'name': 'Hub &mdash; Des Moines', 'short': 'Hub', 'town': 'Des Moines',
    'addr': ['2017 Southlawn Drive, Suite D', 'Des Moines, Iowa 50315'],
    'phone': '(515) 423-0804', 'email': 'trmaweb@tworiversmartialarts.com',
    'price': 30, 'page': 'location-hub.html', 'status': None,
    'summary': ['Mon &ndash; Thu evenings', 'Fri brown &amp; black belt', 'Sat 10:30 am &middot; Sun classes'],
    'sched': [('Monday', '5:30 &ndash; 6:30 pm', ''),
              ('Tuesday', '6:00 &ndash; 7:00 pm &middot; 7:15 &ndash; 8:15 pm', ''),
              ('Wednesday', '6:00 &ndash; 7:00 pm', ''),
              ('Thursday', '5:45 &ndash; 7:00 pm &middot; 7:15 &ndash; 8:15 pm', ''),
              ('Friday', '6:00 &ndash; 7:30 pm', 'brown &amp; black belt'),
              ('Saturday', '10:30 am &ndash; 12:00 pm', ''),
              ('Sunday', 'Martial Spirit 9:30 &middot; Kobudo 12:00 &middot; TKD 2:00', '')],
    'instructors': ['Grandmaster Steve Gonzalez', 'Master Bryan Siever', 'Master Brad Kramer'] },

  { 'key': 'wdm', 'name': 'Clive / West Des Moines', 'short': 'Clive / WDM', 'town': 'Clive',
    'addr': ['8801 University Ave, Suite 23', 'Clive, Iowa 50325'],
    'phone': '(515) 650-3808', 'email': 'wdm@tworiversmartialarts.com',
    'price': 30, 'page': 'location-wdm.html', 'status': None,
    'summary': ['Mon &ndash; Thu 5:45 &amp; 6:45 pm', 'Sat 10:00 &ndash; 11:00 am'],
    'sched': [('Mon &ndash; Thu', '5:45 &ndash; 6:45 pm &middot; 6:45 &ndash; 7:45 pm', ''),
              ('Saturday', '10:00 &ndash; 11:00 am', ''),
              ('Sunday', '2:00 &ndash; 3:30 pm', 'brown &amp; black, 3rd Sunday')],
    'instructors': ['Master Jennifer Bailey', 'Mr. Kendall Bailey', 'Mr. Doug Whitehead'] },

  { 'key': 'indianola', 'name': 'Indianola', 'short': 'Indianola', 'town': 'Indianola',
    'addr': ['2406 W. 2nd Avenue', 'Indianola, Iowa 50125'],
    'phone': '(515) 249-1947', 'email': 'indianola@tworiversmartialarts.com',
    'price': 30, 'page': 'location-indianola.html', 'status': None,
    'summary': ['Mon 6:30 &amp; 7:30 pm', 'Wed 6:30 pm &middot; Thu 6:00 &amp; 7:00 pm'],
    'sched': [('Monday', 'Beginner 6:30 &middot; Advanced 7:30 pm', ''),
              ('Wednesday', 'Advanced 6:30 &ndash; 7:30 pm', ''),
              ('Thursday', 'Beginner 6:00 &middot; Advanced 7:00 pm', '')],
    'instructors': ['Master Roger Netsch', 'Master Marvin Samuelson', 'Master Lucy Kingsbury'] },

  { 'key': 'carlisle', 'name': 'Carlisle', 'short': 'Carlisle', 'town': 'Carlisle',
    'addr': ['Carlisle Community Building', '35 Vine Street, Carlisle, Iowa 50047'],
    'phone': '(515) 423-0804', 'email': 'carlisle@tworiversmartialarts.com',
    'price': 25, 'page': 'location-carlisle.html', 'status': None,
    'summary': ['Mon &amp; Wed 6:30 &ndash; 7:30 pm'],
    'sched': [('Monday', '6:30 &ndash; 7:30 pm', ''),
              ('Wednesday', '6:30 &ndash; 7:30 pm', '')],
    'instructors': ['Ms. Vickie Hornback', 'Mr. Don McDonald'] },

  { 'key': 'winterset', 'name': 'Winterset', 'short': 'Winterset', 'town': 'Winterset',
    'addr': ['404 South 2nd Avenue', 'Winterset, Iowa 50273'],
    'phone': '(515) 423-0804', 'email': 'winterset@tworiversmartialarts.com',
    'price': 25, 'page': 'location-winterset.html', 'status': None,
    'summary': ['Mon &amp; Wed 7:00 &ndash; 8:00 pm'],
    'sched': [('Monday', '7:00 &ndash; 8:00 pm', ''),
              ('Wednesday', '7:00 &ndash; 8:00 pm', '')],
    'instructors': ['Master Roger Netsch', 'Ms. Makenna Konkol', 'Ms. Madison McVay'] },

  { 'key': 'waukee', 'name': 'Waukee', 'short': 'Waukee', 'town': 'Waukee',
    'addr': ['1155 SE Boone Drive', 'Waukee, Iowa 50263'],
    'phone': '(515) 650-3808', 'email': 'waukee@tworiversmartialarts.com',
    'price': 25, 'page': 'location-waukee.html',
    'status': 'NOT TAKING NEW STUDENTS',
    'status_note': 'Waukee is full at present. Families of current Waukee students may still start '
                   'here &mdash; everyone else is welcome at Clive, fifteen minutes east.',
    'summary': ['Tue &amp; Thu 6:30 &ndash; 7:30 pm'],
    'sched': [('Tuesday', '6:30 &ndash; 7:30 pm', ''),
              ('Thursday', '6:30 &ndash; 7:30 pm', '')],
    'instructors': ['Master Jennifer Bailey', 'Mr. Kendall Bailey', 'Mr. Jim McNamara'] },
]

# Dues tiers, mirroring prices.py PRICE_ARR (single, 2, 3, 4, 5 family members)
DUES_TIERS = [
  { 'label': 'Carlisle &middot; Winterset &middot; Waukee', 'prices': [25, 45, 60, 70, 80] },
  { 'label': 'Hub &middot; Clive/WDM &middot; Indianola',   'prices': [30, 50, 65, 75, 85] },
]

def _per_person():
    '''Range of per-person cost at each family size, across the two tiers.'''
    out = []
    for i in range(5):
        vals = sorted(t['prices'][i] / float(i + 1) for t in DUES_TIERS)
        lo, hi = int(round(vals[0])), int(round(vals[-1]))
        out.append('$%d' % lo if lo == hi else '$%d&ndash;%d' % (lo, hi))
    return out

TENETS = [
  ('예의', 'Ye Ui', 'Courtesy',
   'Be polite, be fair, and respect the people you train with.'),
  ('염치', 'Yom Chi', 'Integrity',
   'Know right from wrong &mdash; and be honest about which one you chose.'),
  ('인내', 'In Nae', 'Perseverance',
   'Set the goal, then keep coming back. Patience leads to merit.'),
  ('극기', 'Guk Gi', 'Self-Control',
   'Work within your limits, in the do-jang and outside it.'),
  ('백절불굴', 'Baekjul Boolgool', 'Indomitable Spirit',
   'Speak and stand for what is right, whatever the odds.'),
]

context = {
  '*': {
    'BRANCHES': BRANCHES,
    'DUES_TIERS': DUES_TIERS,
    'PER_PERSON': _per_person(),
    'TENETS': TENETS,
  }
}
