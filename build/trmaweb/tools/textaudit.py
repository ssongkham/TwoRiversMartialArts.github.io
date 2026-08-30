#!/usr/bin/env python3
"""
Compare the visible text of every built page against the same page on another
git ref (default: main), and report any run of words that was lost.

Word-level, not line-level: the redesign rewraps every paragraph, so comparing
lines produces hundreds of false hits. This walks the two word streams with
difflib and reports only genuine deletions.

A run that is missing from its own page but present on some other page is
reported separately -- that is content that moved, not content that was lost.
Runs that appeared on many pages of the old site are counted as nav/footer
chrome, which the redesign replaced wholesale.

This screens; it does not judge. difflib aligns the two word streams globally,
so a deleted link label ("More info") can drag surviving prose into the same
run. Read each hit before acting on it.

    python3 tools/textaudit.py              # vs main, runs of 5+ words
    python3 tools/textaudit.py --min 3      # stricter
    python3 tools/textaudit.py --ref v1.0 --page web/history-trma.html
"""
import argparse, difflib, html, io, os, re, subprocess, sys

SKIP_TAGS = re.compile(r'<(script|style)[^>]*>.*?</\1>', re.S)
COMMENT = re.compile(r'<!--.*?-->', re.S)
JINJA = re.compile(r'\{[%#\{].*?[%#\}]\}', re.S)
TAG = re.compile(r'<[^>]+>')


def visible(markup):
    """Visible text of a page, as a list of lowercase words."""
    s = SKIP_TAGS.sub(' ', markup)
    s = COMMENT.sub(' ', s)
    s = JINJA.sub(' ', s)
    s = TAG.sub(' ', s)
    s = html.unescape(s)
    s = (s.replace('’', "'").replace('‘', "'")
          .replace('“', '"').replace('”', '"')
          .replace('—', '-').replace('–', '-')
          .replace(' ', ' '))
    s = re.sub(r"[^a-z0-9'$&/.@:+-]+", ' ', s.lower())
    return s.split()


def at_ref(ref, path):
    try:
        return subprocess.check_output(['git', 'show', '%s:%s' % (ref, path)],
                                       stderr=subprocess.DEVNULL).decode('utf8', 'replace')
    except subprocess.CalledProcessError:
        return None


def pages(ref):
    out = subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', ref]).decode()
    return [p for p in out.split('\n')
            if p.endswith('.html') and not p.startswith('build/')]


def repo_root():
    return subprocess.check_output(
        ['git', 'rev-parse', '--show-toplevel']).decode().strip()


def main():
    # Always work from the repo root. Run from anywhere else, every page looks
    # missing and the audit quietly reports a clean bill of health.
    os.chdir(repo_root())
    ap = argparse.ArgumentParser()
    ap.add_argument('--ref', default='main')
    ap.add_argument('--min', type=int, default=5, help='shortest run to report')
    ap.add_argument('--page', help='check one page only')
    ap.add_argument('--quiet', action='store_true', help='summary line only')
    ap.add_argument('--chrome', type=int, default=5,
                    help='a run on this many old pages counts as nav/footer chrome')
    a = ap.parse_args()

    # Report on `todo`, but always learn the baselines from the whole site:
    # with --page they would otherwise come from a single file, and every
    # shared nav item would look like a unique loss.
    allpages = pages(a.ref)
    todo = [a.page] if a.page else allpages
    # every page as it stands now, for the "moved, not lost" check
    everything = []
    for p in allpages:
        if os.path.exists(p):
            everything += visible(io.open(p, encoding='utf8', errors='replace').read())
    whole_site = ' ' + ' '.join(everything) + ' '

    # A run that appeared on many pages of the old site is chrome -- the old
    # nav, footer and sidebars, which the redesign replaced wholesale. Counting
    # those as lost content buries the handful of real losses.
    old_text = {}
    for p in allpages:
        o = at_ref(a.ref, p)
        if o is not None:
            old_text[p] = ' ' + ' '.join(visible(o)) + ' '

    def is_chrome(run):
        hits = sum(1 for t in old_text.values() if (' ' + run + ' ') in t)
        return hits >= a.chrome

    lost = moved = chrome = gone_pages = 0
    for path in sorted(todo):
        old = at_ref(a.ref, path)
        if old is None:
            continue
        if not os.path.exists(path):
            gone_pages += 1
            print('PAGE GONE  %s' % path)
            continue
        o = visible(old)
        n = visible(io.open(path, encoding='utf8', errors='replace').read())
        runs = []
        for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, o, n, autojunk=False).get_opcodes():
            if tag in ('delete', 'replace') and (i2 - i1) >= a.min:
                runs.append(' '.join(o[i1:i2]))
        if not runs:
            continue
        here = []
        for r in runs:
            if (' ' + r + ' ') in whole_site:
                moved += 1
            elif is_chrome(r):
                chrome += 1
            else:
                lost += 1
                here.append(r)
        if here and not a.quiet:
            print('\n%s' % path)
            for r in here:
                print('   LOST  %s' % (r if len(r) < 160 else r[:157] + '...'))

    print('\n%d page(s) checked against %s' % (len(todo), a.ref))
    print('  runs of %d+ words missing from the site entirely: %d' % (a.min, lost))
    print('  runs missing from their own page but present elsewhere: %d' % moved)
    print('  runs that were nav/footer chrome on %d+ old pages: %d' % (a.chrome, chrome))
    if gone_pages:
        print('  pages that no longer exist: %d' % gone_pages)
    return 1 if lost else 0


if __name__ == '__main__':
    sys.exit(main())
