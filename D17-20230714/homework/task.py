players=[{"name":"kallis","centuries":"45","halfcenturies":"58","wicketstaken":"292","hattrick":"7","topbs":[224,200,150,100,250]},
         {"name":"watson","centuries":"15","halfcenturies":"33","wicketstaken":"168","hattrick":"5","topbs":[185,170,120,110,105]},
         {"name":"stokes","centuries":"12","halfcenturies":"38","wicketstaken":"197","hattrick":"6","topbs":[258,120,190,102,103]},
         {"name":"raina","centuries":"5","halfcenturies":"36","wicketstaken":"36","hattrick":"3","topbs":[116,123,145,168,174]},
         {"name":"sammy","centuries":"13","halfcenturies":"9","wicketstaken":"84","hattrick":"4","topbs":[124,162,106,154,190]}]
for i in players:
    name=(i["name"])
    centuries=int(i["centuries"])
    if centuries>10:
        print(name,centuries)
    hattrick=int(i["hattrick"])
    if hattrick>5:
        print(name,hattrick) 
    name=(i["name"])        
    topbs=(i["topbs"])
    s=0
    

    

