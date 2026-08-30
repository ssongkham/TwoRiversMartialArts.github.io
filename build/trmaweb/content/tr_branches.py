'''
Branch data for the 2026 redesign: one source of truth for the homepage
summary cards, the Classes & Locations page and the dues table.
Schedules and prices mirror schedule.py / prices.py.
'''

import math
import re
import sys

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
              ('Sunday', 'Martial Spirit 9:30 &middot; Kobudo 12:00 &middot; TKD 2:00',
               'brown &amp; black 2:00, 1st Sunday')],
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
    'instructors': ['Master Roger Netsch', 'Master Lucy Kingsbury', 'Master Brian Anderson'] },

  { 'key': 'carlisle', 'name': 'Carlisle', 'short': 'Carlisle', 'town': 'Carlisle',
    'addr': ['Carlisle Community Building', '35 Vine Street, Carlisle, Iowa 50047'],
    'phone': None, 'email': 'carlisle@tworiversmartialarts.com',
    'price': 25, 'page': 'location-carlisle.html', 'status': None,
    'summary': ['Mon &amp; Wed 6:30 &ndash; 7:30 pm'],
    'sched': [('Monday', '6:30 &ndash; 7:30 pm', ''),
              ('Wednesday', '6:30 &ndash; 7:30 pm', '')],
    'instructors': ['Ms. Vickie Hornback', 'Mr. Don McDonald'] },

  { 'key': 'winterset', 'name': 'Winterset', 'short': 'Winterset', 'town': 'Winterset',
    'addr': ['404 South 2nd Avenue', 'Winterset, Iowa 50273'],
    'phone': None, 'email': 'winterset@tworiversmartialarts.com',
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

def _tel(phone):
    '''(515) 423-0804 -> +15154230804, so tel: links actually dial.'''
    if not phone:
        return None
    digits = re.sub(r'\D', '', phone)
    return '+1' + digits if len(digits) == 10 else '+' + digits

for _b in BRANCHES:
    _b['tel'] = _tel(_b['phone'])

def _per_person():
    '''Range of per-person cost at each family size, across the two tiers.

    Rounds half UP: round() is banker's rounding, so $45 split two ways
    (22.50) came out as $22 and understated the price.
    '''
    out = []
    for i in range(5):
        vals = sorted(t['prices'][i] / float(i + 1) for t in DUES_TIERS)
        lo, hi = (int(math.floor(v + 0.5)) for v in (vals[0], vals[-1]))
        out.append('$%d' % lo if lo == hi else '$%d&ndash;%d' % (lo, hi))
    return out

# Descriptions are the club's own, from the pre-redesign homepage. 'note' is
# ours: where and when the class runs, taken from the schedule.
PROGRAMMES = [
  { 'name': 'Tae Kwon Do', 'page': 'curriculum.html', 'frag': '',
    'note': 'All six branches',
    'body': 'To try out our club and the art of Tae Kwon Do, just come to a '
            'few classes!' },
  { 'name': 'Martial Spirit', 'page': 'martial-spirit.html', 'frag': '',
    'note': 'Hub &middot; Sundays 9:30 am',
    'body': 'This is a formal martial art class that can be started at any '
            'time.' },
  { 'name': 'Kobudo', 'page': 'kobudo.html', 'frag': '',
    'note': 'Hub &middot; Sundays 12:00 pm',
    'body': 'Kobudo is an ancient art of Okinawan Weaponry.' },
  { 'name': 'Self Defense', 'page': 'curriculum.html', 'frag': '#self-defense',
    'note': 'Part of the Tae Kwon Do class',
    'body': 'Two Rivers Martial Arts Self Defense curriculum was created by '
            'Master Deaton.' },
]

def _price_range():
    '''"$25-30" derived from the branches, so it cannot drift from the cards.'''
    lo = min(b['price'] for b in BRANCHES)
    hi = max(b['price'] for b in BRANCHES)
    return '$%d' % lo if lo == hi else '$%d&ndash;%d' % (lo, hi)

_DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday',
         'saturday', 'sunday']


def _days_named(label):
    """['monday'..'thursday'] for a 'Mon - Thu' row, ['sunday'] for 'Sunday'."""
    hits = [d for d in re.findall(r'mon|tue|wed|thu|fri|sat|sun', label.lower())]
    full = [next(x for x in _DAYS if x.startswith(h)) for h in hits]
    if len(full) == 2 and ('ndash' in label or '-' in label or 'to' in label):
        a, b = (_DAYS.index(x) for x in full)
        if a < b:
            return _DAYS[a:b + 1]
    return full


def _check_schedules():
    """Warn when the summary schedules here drift from schedule.py.

    The branch pages render schedule.py; the homepage cards and the Classes
    page render the 'sched' rows above. Nothing links the two, so a class added
    in one place silently goes missing from the other -- which is how the Hub
    lost its 1st-Sunday brown/black class. Compare clock times per day and say
    so on stderr; never break the build over it.
    """
    import codecs
    data = {}
    try:
        with codecs.open('content/schedule.py', encoding='utf8') as f:
            exec(f.read(), data)
    except Exception as e:
        sys.stderr.write('tr_branches: cannot read schedule.py (%s)\n' % e)
        return

    # Compare start times and class kinds. End times are deliberately absent
    # from the card summaries, so comparing every clock token is only noise.
    kinds = ('brown', 'black', 'kobudo', 'martial spirit', 'tai chi',
             'beginner', 'advanced')

    def starts(pairs):
        out = set()
        for when in pairs:
            m = re.search(r'\d{1,2}:\d{2}', when)
            if m:
                out.add(m.group(0))
        return out

    def kinds_in(text):
        t = text.lower().replace('&amp;', '&')
        return set(k for k in kinds if k in t)

    for b in BRANCHES:
        page = data.get('context', {}).get(b['page'])
        if not page:
            continue
        theirs, their_kind = {}, {}
        for row in page.get('class_schedule', []):
            d = row['day'].lower()
            theirs.setdefault(d, set()).update(starts(t for _, t in row['classes']))
            their_kind.setdefault(d, set()).update(
                kinds_in(' '.join(n for n, _ in row['classes'])))
        mine, my_kind = {}, {}
        for label, when, note in b['sched']:
            for d in _days_named(label):
                mine.setdefault(d, set()).update(
                    starts(when.split('&middot;') + [note]))
                my_kind.setdefault(d, set()).update(kinds_in(when + ' ' + note))
        for d in _DAYS:
            for what, a, c in (('times', theirs, mine), ('classes', their_kind, my_kind)):
                if a.get(d, set()) != c.get(d, set()):
                    sys.stderr.write(
                        'tr_branches: %s %s %s -- schedule.py %s, tr_branches %s\n'
                        % (b['key'], d, what, sorted(a.get(d, ())) or 'nothing',
                           sorted(c.get(d, ())) or 'nothing'))


_check_schedules()


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
    'PRICE_RANGE': _price_range(),
    'TENETS': TENETS,
    'PROGRAMMES': PROGRAMMES,
  }
}
