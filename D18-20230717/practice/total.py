a=[{"name":"sivarajan","place":"vadasery","hobbies":["cricket","music","movies"],"sslc":{"tamil":90,"english":95,"maths":95,"science":100,"social":90}},
    {"name":"sharmila","place":"monday market","hobbies":["temple","cooking","movie"],"sslc":{"tamil":95,"english":90,"maths":100,"science":93,"social":89}},
    {"name":"alfreena","place":"souththamaraikulam","hobbies":["planets","web series","movie"],"sslc":{"tamil":95,"english":91,"maths":93,"science":87,"social":80}}]
for i in (a):
    t=(i["sslc"])
    w=(t["tamil"]+t["english"]+t["maths"]+t["science"]+t["social"])
    print(w)
    average=(w*3)
    print(average) 


    
    
    
    

