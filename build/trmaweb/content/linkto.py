
def linktofn( prefix ) :
    def lt(x) :
        if 'index.html' in x :
            return '"../index.html"'
        return '"%s%s"' % (prefix,x)
    return lt

def indexlt(x) :
    # if x == '#' : return '"index.html#"'
    if 'index.html' in x : 
        return x
    return linktofn('web/')(x)

def pathfn(lt):
    '''Bare path for the same target, so a #fragment can be appended.

    linkto() returns the path already wrapped in quotes, which is fine for
    href={{linkto(...)}} but cannot carry a fragment.
    '''
    def p(x):
        return lt(x).strip('"')
    return p

context = {

  '*' :          { 'linkto' : linktofn(''), 'pathto' : pathfn(linktofn('')) },
  # if index is outside folder of other pages, 
  #   set the prefix accordingly
  
  'index.html' : { 'linkto' : indexlt, 'pathto' : pathfn(indexlt) },
  'annualmeeting.html' : { 'linkto' : indexlt, 'pathto' : pathfn(indexlt) },
  'donate.html' : { 'linkto' : indexlt, 'pathto' : pathfn(indexlt) },
  
}
