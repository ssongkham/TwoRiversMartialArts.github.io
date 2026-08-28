
context = {
 'location-carlisle.html' : 
    #{'LATLNG':'41.4883211143,-93.4899016988','BRANCHNAME':'Carlisle'},
     {'LATLNG': '41.4979283,-93.4858797', 'BRANCHNAME': 'Carlisle'},
'location-hub.html' : 
    {'LATLNG':'41.53319,-93.64416','BRANCHNAME':'Hub'},
'location-indianola.html' : 
    #{'LATLNG':'41.355373,-93.583986','BRANCHNAME':'Indianola'},
    #{'LATLNG':'41.36013689,-93.56138092','BRANCHNAME':'Indianola'},
    {'LATLNG':'41.35681,-93.59286','BRANCHNAME':'Indianola'},
'location-pleasanthill.html' : 
    {'LATLNG':'41.601833,-93.504325','BRANCHNAME':'Pleasant Hill'},
'location-waukee.html' : 
    {'LATLNG':'41.601793,-93.831828','BRANCHNAME':'Waukee'},
'location-wdm.html' : 
    {'LATLNG':'41.602315, -93.740336','BRANCHNAME':'Clive/West Des Moines'},
'location-winterset.html' : 
    {'LATLNG':'41.331803,-94.015775','BRANCHNAME':'Winterset'},
}

# Each branch's address box links to Google Maps at the same point the map
# below it is centred on. Official Maps URL scheme, so it opens the app on a
# phone and the site on a desktop.
for _page, _ctx in context.items():
    _ll = _ctx['LATLNG'].replace(' ', '')
    _ctx['MAPS_URL'] = 'https://www.google.com/maps/search/?api=1&amp;query=' + _ll
