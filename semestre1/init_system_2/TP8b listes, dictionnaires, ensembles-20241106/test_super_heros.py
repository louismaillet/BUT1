import super_heros as sh
avengers = {
    ' Spiderman ': (5 , 5 , ' araign ée a quatre pattes ') ,
    ' Hulk ': (7 , 4 , " Grand homme vert " ) ,
    ' Agent 13 ': (2 , 3 , ' agent 13 ') ,
    'M Melin ': (2 , 6, ' expert en archi ') 
    }

def test_intelligence_moyenne():
    assert sh.intelligence_moyenne(avengers) == 4.5
    assert sh.intelligence_moyenne({}) == (None, 'il sont tous nuls')
    assert sh.intelligence_moyenne({' Spiderman ': (5 , 1 , ' araignée a quatre pattes '), 'bete' : (7,0,'le mec a 0 d"intelligence_moyenne'), 'Nul' : (7,0,'le mec a 0 d"intelligence_moyenne')}) == 1/3

def test_kikelplusfort():
    assert sh.kikelplusfort(avengers) == ' Hulk '
    assert sh.kikelplusfort({}) == None
    assert sh.kikelplusfort({' Spiderman ': (5 , 1 , ' araignée a quatre pattes '), 'bete' : (7,0,'le mec a 0 d"intelligence_moyenne'), 'Nul' : (7,0,'le mec a 0 d"intelligence_moyenne')}) == 'bete'
    assert sh.kikelplusfort({' Spiderman ': (5 , 1 , ' araignée a quatre pattes '), 'bete' : (7,0,'le mec a 0 d"intelligence_moyenne'), 'Nul' : (8,0,'le mec a 0 d"intelligence_moyenne'), ' Hulk ': (7 , 4 , " Grand homme vert " )}) == 'Nul'
    assert sh.kikelplusfort({' Spiderman ': (10 , 1 , ' araignée a quatre pattes '), 'bete' : (7,0,'le mec a 0 d"intelligence_moyenne'), 'Nul' : (8,0,'le mec a 0 d"intelligence_moyenne'), ' Hulk ': (7 , 4 , " Grand homme vert " )}) == ' Spiderman '

def test_combienDeCretins():
    assert sh.combienDeCretins(avengers) == 2
    assert sh.combienDeCretins({}) == 0
    assert sh.combienDeCretins({' a ': (0,1,'0'), 'b' : (0,1,'0'), 'c' : (0,1,'0')}) == 0
    assert sh.combienDeCretins({' Spiderman ': (5 , 1 , ' araignée a quatre pattes '), 'bete' : (7,0,'le mec a 0 d"intelligence_moyenne'), 'Nul' : (7,0,'le mec a 0 d"intelligence_moyenne')}) == 2