'''Which nav item is lit, per page, for the 2026 layout.'''
DEFAULT_DESC = ('Two Rivers Martial Arts &mdash; traditional Tae Kwon Do taught by volunteers '
                'at six branches across central Iowa. First class free, dues from $25 a month.')

context = {
  '*': { 'TR_ACTIVE': '', 'PAGE_DESC': DEFAULT_DESC },

  'index.html': { 'TR_ACTIVE': 'home' },

  'classes.html': { 'TR_ACTIVE': 'classes',
    'PAGE_DESC': 'Class times, addresses and instructors for all six Two Rivers Martial Arts '
                 'branches in central Iowa. Your first class is free.' },

  'start-here.html': { 'TR_ACTIVE': 'start',
    'PAGE_DESC': 'How to start Tae Kwon Do at Two Rivers: your first class is free, what to '
                 'wear, what a class is like, and what it costs &mdash; from $25 a month.' },

  'resource-tenets.html': { 'TR_ACTIVE': 'resources',
    'PAGE_DESC': 'Courtesy, Integrity, Perseverance, Self-Control and Indomitable Spirit &mdash; '
                 'the five tenets of Tae Kwon Do, in full.' },
}
