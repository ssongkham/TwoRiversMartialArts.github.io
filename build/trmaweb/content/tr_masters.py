'''
The Grand Masters and Masters shown at the foot of the homepage.

Names, ranks and biographies are the club's own, copied verbatim from the
pre-redesign index.html. 'anchor' is set only where instructors-primary.html
actually has that id -- most of these instructors are not on that page, and a
link to a fragment that does not exist just drops the reader at the top of it.
'''

GRANDMASTERS = [
  { 'name': 'Grandmaster Brett McBroom', 'dan': '8th Dan',
    'img': 'assets/images/instructors/winterset/instructor_McbroomB.jpg',
    'alt': 'Grandmaster Mcbroom', 'anchor': None,
    'bio': 'Grandmaster McBroom began training with Master Heintz in the early 1980s. '
           'He earned his 8th Dan in December 2016.' },
  { 'name': 'Grandmaster Steve Gonzalez', 'dan': '8th Dan',
    'img': 'assets/images/instructors/hub/MrGonzalez.png',
    'alt': 'Grandmaster Gonzalez', 'anchor': 'mr_gonzalez',
    'bio': 'Grandmaster Gonzalez started training with Master Heintz in the mid 1980s. '
           'He earned his 8th Dan in December 2016.' },
  { 'name': 'Grandmaster Brad Deaton', 'dan': '8th Dan',
    'img': 'assets/images/instructors/hub/MrDeaton.png',
    'alt': 'Grandmaster Deaton', 'anchor': None,
    'bio': 'Grandmaster Deaton began training with Master Heintz in 1986. '
           'He earned his 8th Dan in December 2016.' },
  { 'name': 'Grandmaster Anita Williams', 'dan': '8th Dan',
    'img': 'assets/images/instructors/hub/instructor_WilliamsA.jpg',
    'alt': 'Master Williams', 'anchor': None,
    'bio': 'Grandmaster Williams began training with Master Heintz in 1987 and earned '
           'her 8th Dan in August 2023.' },
  { 'name': 'Grandmaster Dwayne Ferguson', 'dan': '8th Dan',
    'img': 'assets/images/instructors/hub/instructor_FergusonD.jpg',
    'alt': 'Master Ferguson', 'anchor': None,
    'bio': 'Grandmaster Ferguson began training with Master Heintz in 1989 and earned '
           'his 8th Dan in August 2023.' },
]

MASTERS = [
  { 'name': 'Master Bryan Siever', 'dan': '7th Dan',
    'img': 'assets/images/instructors/hub/MstrSiever_sm.png',
    'alt': 'Master Siever', 'anchor': 'mr_siever',
    'bio': 'Master Siever began training with Master Heintz in the spring of 1993. '
           'He earned his 7th Dan in August of 2023.' },
  { 'name': 'Master Roger Netsch', 'dan': '7th Dan',
    'img': 'assets/images/instructors/indianola/MrNetsch.png',
    'alt': 'Master Roger Netsch', 'anchor': 'mr_netsch',
    'bio': 'Master Netsch earned his 7th Dan in August 2023.' },
  { 'name': 'Master Lucy Kingsbury', 'dan': '6th Dan',
    'img': 'assets/images/instructors/indianola/mskingsbury.jpg',
    'alt': 'Master Lucy Kingsbury', 'anchor': 'ms_kingsbury',
    'bio': 'Master Kingsbury earned her 6th Dan in April 2026.' },
  { 'name': 'Master Brian Anderson', 'dan': '6th Dan',
    'img': 'assets/images/instructors/indianola/MrAnderson.png',
    'alt': 'Master Brian Anderson', 'anchor': 'mr_anderson',
    'bio': 'Master Anderson began his training with Two Rivers in 2003 and earned his '
           '6th Dan in June 2026.' },
  { 'name': 'Master Drew Cummings', 'dan': '5th Dan',
    'img': 'assets/images/instructors/hub/MrCummings.png',
    'alt': 'Master Drew Cummings', 'anchor': None,
    'bio': 'Master Cummings began his training with Two Rivers in 2004 and earned his '
           '5th Dan in June 2021.' },
  { 'name': 'Master Brad Kramer', 'dan': '5th Dan',
    'img': 'assets/images/instructors/MrKramer.png',
    'alt': 'Master Brad Kramer', 'anchor': 'mr_kramer',
    'bio': 'Master Kramer began his training in 1983 at the Eric Heintz Black Belt '
           'Academy and earned his 5th Dan in April 2022.' },
  { 'name': 'Master Perry Comito', 'dan': '5th Dan',
    'img': 'assets/images/instructors/MrComito.png',
    'alt': 'Master Perry Comito', 'anchor': None,
    'bio': 'Master Comito began his training in 1995 at the Eric Heintz Black Belt '
           'Academy and earned his 5th Dan in April 2022.' },
  { 'name': 'Master Jennifer Bailey', 'dan': '5th Dan',
    'img': 'assets/images/instructors/wdsm/MsBaileyThumb.png',
    'alt': 'Master Jennifer Bailey', 'anchor': 'ms_bailey',
    'bio': 'Master Bailey started training at Two Rivers in August 2008 and earned her '
           '5th Dan in April 2022.' },
  { 'name': 'Master Steven Goldstein', 'dan': '5th Dan',
    'img': 'assets/images/instructors/MrGoldstein.jpg',
    'alt': 'Master Steven Goldstein', 'anchor': None,
    'bio': 'Master Goldstein started training at Two Rivers in March 2010 and earned '
           'his 5th Dan in December 2023.' },
]

context = { '*': { 'GRANDMASTERS': GRANDMASTERS, 'MASTERS': MASTERS } }
