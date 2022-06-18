CATCH_EXCEPTION = True
firstTime = True
ligueName_ = league + country
attempts = 0

for link in tableLinks:
    nextOnePlease = False
    while not nextOnePlease and attempts < 5:
        try:
            nextOnePlease = False
            print(link)

            #########################
            ## Get the match tab
            #########################
            
            opt = webdriver.ChromeOptions()
            opt.add_argument('--headless')
            driver = webdriver.Chrome('chromedriver', options=opt)
            #driver = webdriver.Chrome('chromedriver')
            time_delay = randint(1,2)

            driver.get(link)
            time.sleep(time_delay)


            tableElement = driver.find_elements_by_xpath("//table[@id='sortable-1']")
            for ii in tableElement:
                table = ii.text.split('\n')
                #print(ii.size)
            if len(tableElement) > 0:

                element = driver.find_elements_by_xpath("//table[@id='sortable-1']/tbody/tr/td")
                tableExtended = []
                for ii in element:
                    #print(ii.size)
                    #print(ii.text)
                    #print(ii.get_attribute('data-opening-odd'))
                    openingOdd = ii.get_attribute('data-opening-odd')
                    dataCreated = ii.get_attribute('data-created')
                    dataOpeningDate = ii.get_attribute('data-opening-date')
                    tableExtended = tableExtended + ii.text.split('\n')
                    if (openingOdd != None):
                        tableExtended.append(str(openingOdd))
                        tableExtended.append(str(dataCreated))
                        tableExtended.append(str(dataOpeningDate))

                tableExtended = list(filter(None, tableExtended))
                #tableExtended[:10]

                ##############################
                # Click on the O/U tab
                ##############################
                '''
                driver = webdriver.Chrome('chromedriver')
                time_delay = randint(10,15)

                linkOu = link + "#ou"
                driver.get(linkOu)
                time.sleep(time_delay)
                '''
                
                UOClickedOK = False
                UOClickedOKAttemps = 0
                while(not UOClickedOK):
                    UOClickedOKAttemps += 1

                    if(UOClickedOKAttemps > 5):
                        assert False
                    
                    links = driver.find_elements_by_xpath("//a[@title='Over/Under']")
                    for link in links:
                        #print(link)
                        link.send_keys("\n")  #.click() #.send_keys("\n") .submit()
                        time_delay = randint(1,3)
                        time.sleep(time_delay)
                    #print("U/O CLickeeeeeeeeeeeeeeeeeeeeeed")

                    tableNumber = 1
                    jjUO = 0;
                    UO25Break = False
                    UO25Found = False

                    while tableNumber < 10 and not UO25Break and not UO25Found:
                        UOTableString = "//*[@id='sortable-" + str(tableNumber) + "']"

                        UOElementBasic = driver.find_elements_by_xpath(UOTableString)
                        UOTableBasic = []

                        for ii in UOElementBasic:
                            UOTableBasic = UOTableBasic + ii.text.split('\n')

                            if(len(UOTableBasic) > 1):
                                splited = UOTableBasic[2].split(' ') ## The 2.5 number that I seek
                                #print(splited)
                            tableNumber += 1

                            #print(splited[0])
                            if (splited[0] == '0.5'):
                                UOTableBasicZero = UOTableBasic.copy()
                            
                            if (splited[0] == '2.5'):
                                UO25Found = True
                            #print("tttttttttttt")
                        jjUO += 1
                        if jjUO > 10:
                             UO25Break = True

                    #print(UOTableBasic) 
                    if(len(UOTableBasic) > 0):
                        UOClickedOK = True
                    #else:
                        #print("Clicking U/O again...")
                
                UOElement = driver.find_elements_by_xpath(UOTableString + "/tbody/tr/td") # Under/Over 2.5
                #print(UOElement)
                UOTable = []
                for ii in UOElement:
                    UOTable = UOTable + ii.text.split('\n')
                    #print(ii.size)
                    #print(ii.text)
                    openingOdd = ii.get_attribute('data-opening-odd')
                    if (openingOdd != None):
                        UOTable.append(str(openingOdd))
                UOTable = list(filter(None, UOTable))

                dic = {}
                ###############################
                #print("CCCCCCCCCCCCCCCCCCCCCC")
                ## Number of betHouses
                betHousesNumber_ = table[0].split(' ')[1];
                if int(betHousesNumber_) > 0:
                    ## Odds of all betHouses
                    lastCell = ""
                    for cell in table:
                        #print(cell)
                        if("Average" in cell):
                            cellSplited = cell.split(' ')
                            _AverageOdds_1_ = cellSplited[2]
                            _AverageOdds_X_ = cellSplited[3]
                            _AverageOdds_2_ = cellSplited[4]     

                        lastCell = cell

                    time_delay = randint(1,2)
                    time.sleep(time_delay)
                        
                    splited = UOTableBasic[len(UOTableBasic)-1].split(' ')
                    _AverageOdds_O25_ = splited[2]
                    _AverageOdds_U25_ = splited[3]
                    splited = UOTableBasicZero[len(UOTableBasicZero)-1].split(' ')
                    _AverageOdds_O05_ = splited[2]
                    _AverageOdds_U05_ = splited[3]

                    ###############################
                #print("DDDDDDDDDDDDDDDDDDDDDDDDDDD")
                increment = 13
                ii = 0
                #print(tableExtended)
                while(ii <= (increment * int(betHousesNumber_)) ):
                    if ii < len(tableExtended):
                        betHouse                 = tableExtended[ii]
                        #dic[str(betHouse)]       = betHouse  
                        try:
                            dic["_" + str(betHouse) + "_1_"]                          = float(tableExtended[ii+1])
                        except:
                            dic["_" + str(betHouse) + "_1_"]                          = "-"
                        #dic["_" + str(betHouse) + "_1_oppeningOdds_"]             = float(tableExtended[ii+2])
                        #dic["_" + str(betHouse) + "_1_oddsDifference_"]           = float(tableExtended[ii+1]) - float(tableExtended[ii+2])
                        #dic["_" + str(betHouse) + "_1_closingDate_"]              =       tableExtended[ii+3]
                        #dic["_" + str(betHouse) + "_1_oppeningDate_"]             =       tableExtended[ii+4]
                        try:
                            dic["_" + str(betHouse) + "_X_"]                          = float(tableExtended[ii+5])
                        except:
                            dic["_" + str(betHouse) + "_X_"]                          = "-"
                        #dic["_" + str(betHouse) + "_X_oppeningOdds_"]             = float(tableExtended[ii+6])
                        #dic["_" + str(betHouse) + "_X_oddsDifference_"]           = float(tableExtended[ii+5]) - float(tableExtended[ii+6])
                        #dic["_" + str(betHouse) + "_X_closingDate_"]              =       tableExtended[ii+7]
                        #dic["_" + str(betHouse) + "_X_oppeningDate_"]             =       tableExtended[ii+8]

                        try:
                            dic["_" + str(betHouse) + "_2_"]                          = float(tableExtended[ii+9])
                        except:  
                            dic["_" + str(betHouse) + "_2_"]                          = "-"
                        #dic["_" + str(betHouse) + "_2_oppeningOdds_"]             = float(tableExtended[ii+10])
                        #dic["_" + str(betHouse) + "_2_oddsDifference_"]           = float(tableExtended[ii+9]) - float(tableExtended[ii+10])
                        #dic["_" + str(betHouse) + "_2_closingDate_"]              =       tableExtended[ii+11]
                        #dic["_" + str(betHouse) + "_2_oppeningDate_"]             =       tableExtended[ii+12]

                    ii = ii + increment


                    ###########################
                ## Under/Over 2.5 Odds of all betHouses
                if(UO25Found):
                    betHousesNumber_UO_25_ = re.findall(r'\d+', UOTableBasic[0])[0]
                    #print(UOTable)

                    ii = 0
                    increment = 6
                    while(ii < (increment * int(betHousesNumber_UO_25_)) ):
                        betHouse                                      = UOTable[ii]
                        dic["_" + str(betHouse) + "_O25_"]            = float(UOTable[ii+2])
                        dic["_" + str(betHouse) + "_U25_"]            = float(UOTable[ii+4])
                        dic["_" + str(betHouse) + "_O25_Oppening_"]   = float(UOTable[ii+3])
                        dic["_" + str(betHouse) + "_U25_Oppening_"]   = float(UOTable[ii+5])
                        dic["_" + str(betHouse) + "_O25_Difference_"] = float(UOTable[ii+2]) - float(UOTable[ii+3])
                        dic["_" + str(betHouse) + "_U25_Difference_"] = float(UOTable[ii+4]) - float(UOTable[ii+5])

                        ii = ii + increment


                ##############################
                ## Results
                ##############################

                # Kick off
                elements = driver.find_elements_by_xpath("//p[@class='list-details__item__date']")
                for element in elements:
                    tableTime = element.text.split('.')

                day_ = int(tableTime[0])
                month_ = int(tableTime[1])
                aux = tableTime[2].split(' - ')
                year_ = int(aux[0])
                aux = aux[1].split(':')
                startHour_ = int(aux[0])
                startMinute_ = int(aux[1])

                # Result
                elements = driver.find_elements_by_xpath("//p[@class='list-details__item__score']")
                for element in elements:
                    tableResult = element.text.split(':')

                localGoals_ = int(tableResult[0])
                awayGoals_ = int(tableResult[1])

                matchResult_ = 'X'
                if localGoals_ > awayGoals_:
                    matchResult_ = '1'
                elif localGoals_ < awayGoals_:
                    matchResult_ = '2'    

                # part-time result
                elements = driver.find_elements_by_xpath("//h2[@class='list-details__item__partial']")
                for element in elements:
                    tablePartialResult = element.text.split(',')
                tablePartialResult

                aux = tablePartialResult[0].split(':')
                firstPartLocalGoals_ = int(aux[0].split('(')[1])
                firstPartAwayGoals_ = int(aux[1])

                aux = tablePartialResult[1].split(':')
                secondPartLocalGoals_ = int(aux[0])
                secondPartAwayGoals_ = int(aux[1].split(')')[0])


                season_ = season

                # Team names
                elements = driver.find_elements_by_xpath("//h2[@class='list-details__item__title']")

                localTeamName_ = elements[0].text
                awayTeamName_ = elements[1].text

                ##############################
                ## make df
                ##############################

                dfAux = pd.DataFrame([dic])

                dfAux.insert(0, "betHousesNumber", betHousesNumber_)

                dfAux.insert(0, "AverageOdds_U25", _AverageOdds_U25_)
                dfAux.insert(0, "AverageOdds_O25", _AverageOdds_O25_)
                
                dfAux.insert(0, "AverageOdds_U05", _AverageOdds_U05_)
                dfAux.insert(0, "AverageOdds_O05", _AverageOdds_O05_)

                dfAux.insert(0, "AverageOdds_2", _AverageOdds_2_)
                dfAux.insert(0, "AverageOdds_X", _AverageOdds_X_)
                dfAux.insert(0, "AverageOdds_1", _AverageOdds_1_)

                dfAux.insert(0, "firstPartLocalGoals", firstPartLocalGoals_)
                dfAux.insert(0, "firstPartAwayGoals", firstPartAwayGoals_)
                dfAux.insert(0, "secondPartLocalGoals", secondPartLocalGoals_)
                dfAux.insert(0, "secondPartAwayGoals", secondPartAwayGoals_)

                dfAux.insert(0, "day", day_)
                dfAux.insert(0, "month", month_)
                dfAux.insert(0, "year", year_)
                dfAux.insert(0, "startHour", startHour_)
                dfAux.insert(0, "startMinute", startMinute_)

                dfAux.insert(0, "awayGoals", awayGoals_)
                dfAux.insert(0, "localGoals", localGoals_)
                dfAux.insert(0, "matchResult", matchResult_)

                dfAux.insert(0, "awayTeamName", awayTeamName_)
                dfAux.insert(0, "localTeamName", localTeamName_)

                dfAux.insert(0, "ligueName", ligueName_)
                dfAux.insert(0, "season", season_)  

                #print(dfAux['_Betway_1_'])

                ###### Not Null and a float understable value 
                assert float(dfAux['AverageOdds_1']) is not None and float(dfAux['AverageOdds_1']) > 0.0
                #print(dfAux)

                #print(len(dfAux[0]) )
                if not firstTime:
                    df_ant = pd.concat([dfAux, df_ant], ignore_index=True)
                else: 
                    df_ant = dfAux
                    firstTime = False

                nextOnePlease = True
                attempts = 0
                #print(df_ant) 
            else:
                print("No bookmarket today?")
                #driver.close()
                nextOnePlease = False
                attempts += 1
            driver.close()
        except: # ValueError as e:
            if CATCH_EXCEPTION:
                print("Error catched")
                attempts += 1
                nextOnePlease = False 
                time_delay = randint(5,10)
                time.sleep(time_delay)
            else:
                attempts += 100
            driver.close()
    

df_ant
