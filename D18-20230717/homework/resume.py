resume={"NAME":"M.S.SIVARAJAN",
        "E-MAIL":"sivarajanms14@gmail.com",
        "MOBILE-NO":"8760541817",
        "SOFT SKILLS":["MOTIVATION","CREATIVITY"],
        "HARD SKILLS":["WRITING","COPY WRITING"],
        "EDUCATIONAL QUALIFICATION":[{"COURSE":"SSLC",
                                      "INSTITUTE NAME":"S.M.R.V",
                                      "YEAR PASSOUT":"2013"},
                                     {"COURSE":"HSC",
                                      "INSTITUTE NAME":"S.M.R.V",
                                      "YEAR PASSOUT":"2105"},
                                     {"COURSE":"DEGREE",
                                      "INSTITUTE NAME":"K.N.S.K",
                                       "YEAR PASSOUT" :"2016 to 2018"}],
        "PROJECTS":[{"PROJECTS 1": "NO"},
                    {"PROJECTS 2":"NO"}],
        "EXPERIENCE":[{"COMPANY NAME":"DEVAXEL","ROLE":"TESTING","DURATION":"2.0"},
                     {"COMPANY NAME":"CAPE START","ROLE":"TESTING","DURATION":"1.5"},
                     {"COMPANT NAME":"VISION","ROLE":"TESTING","DURATION":"1.8"}],
        "HOBBIES":["CRICKET","TENNIS","MUSIC","TREK"],
        "PERSONALDETAILS":{"FATHER'S NAME":"A.MURUGAN",
                            "FATHER'S OCCUPATION":"BUSINESS",
                            "LANGUAGES KNOWN":"TAMIL","ENGLISH"
                            "DOB":"14-02-1999",
                            "GENDER":"MALE",
                            "MARTIAL STATUS":"SINGLE",
                            "ADDRESS":"20/68,KANAGAMOOLAM NEW STREET VADASERY,NAGERCOIL"}}                                                                                   

for i in resume["EDUCATIONAL QUALIFICATION"]:
        COURSE=i["COURSE"]
        INSTITUTENAME=i["INSTITUTE NAME"]
        YEARPASSOUT=i["YEAR PASSOUT"]
        print(f"COURSE:{COURSE}\nINSTITUTENAME{INSTITUTENAME}\nYEARPASSOUT{YEARPASSOUT}")
for i in resume["PERSONALDETAILS"]:
        print(f"{i} : {resume ['PERSONALDETAILS'][i]}")


        

                         




