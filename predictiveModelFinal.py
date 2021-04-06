import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt
import math


import statsmodels.api as sm
from statsmodels.stats import diagnostic as diag
from statsmodels.stats.outliers_influence import variance_inflation_factor

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


#Return home and away score from a single cell
def splitScore(score):
    index = 0
    for ele in score:
        if ele == "-":
             break
        else:
             index+=1
    home = int(score[:index])
    away = int(score[index+1:])
    return (home,away)


#Used to get the current 20 teams in a particular season
#3 teams are relegated at the end so the three new teams
# are included each season
def teamsx(df):
    teams = []
    for index, row in df.iterrows():
        homeT =row["HomeTeam"].replace(" ", "")
        AwayT = row["AwayTeam"].replace(" ", "")
        if ( homeT not in teams):
            teams.append(homeT)
        if(AwayT not in teams):
            teams.append(AwayT)
        if len(teams) == 20:
            break
    return teams


#check to see if a team is in a given row of a data frame
def teamInRow(team,row):
    if team ==  row["HomeTeam"].replace(" ", ""):
        return True
    if team == row["AwayTeam"].replace(" ", ""):
        return True
    else:
        return False

# check to see if a team is home team
def isHomeTeam(team,row):
        if team ==  row["HomeTeam"].replace(" ", ""):
            return True
        else:
            return False
        
#check to see if a team is an away team
def isAwayTeam(team,row):
    if team == row["AwayTeam"].replace(" ", ""):
        return True
    else:
        return False

#check to see if a team has one a game
# in the current row of the data frame
def isWin(team,row):
    #print(row["FTR"].replace(" ", ""))
    if isAwayTeam(team,row) and row["FTR"].replace(" ", "")== "A":
        return True
    if isHomeTeam(team,row) and row["FTR"].replace(" ", "")== "H":
        return True
    else:
        return False

#check to see if a team has lost 
# the current game(r0w) in the data frame
def isLost(team, row):
    if isAwayTeam(team,row) and row["FTR"].replace(" ", "")== "H":
        return True
    if isHomeTeam(team,row) and row["FTR"].replace(" ", "")== "A":
        return True
    else:
        return False

#check if a game is a draw
def isDraw(team,row):
    return (not isLost(team,row)) and (not isWin(team,row))




# Returns a list of data frame for each team
# each data frame contains a particular teams stat of:
#wins losses draws away-victories tophalfvictories
#and bottom half victories
def progressionTables(teams,df,topHalf,bottomHalf):
    tables = []
    indexCount = 0
    for team in teams:
        index = []
        data = ({'Points':[],
        'AwayVictories':[],
        'TopHalfVictories':[],
        "BottomHalfVictories":[],
        "Wins":[],
        "Loss":[],
        "Draws":[]},
               index)
        pts, aw, thv, bhv, wins, loss, draws = 0,0,0,0,0,0,0
        for index, row in df.iterrows():
            if teamInRow(team,row):
                data[1].append(indexCount)
                indexCount+=1
                if isWin(team,row):
                    pts+=3
                    wins+=1
                    data[0]["Points"].append(pts)
                    data[0]["Wins"].append(wins)
                else:
                    data[0]["Wins"].append(wins)

                if isDraw(team,row):
                    pts+=1
                    draws+=1
                    data[0]["Points"].append(pts)
                    data[0]["Draws"].append(draws)
                else:
                    data[0]["Draws"].append(draws)


                if isLost(team,row):
                    pts+=0
                    loss+=1
                    data[0]["Points"].append(pts)
                    data[0]["Loss"].append(loss)
                else:
                    data[0]["Loss"].append(loss)


                if isAwayTeam(team,row) and isWin(team,row):
                    aw+=1
                    data[0]["AwayVictories"].append(aw)
                else:
                    data[0]["AwayVictories"].append(aw)


                if isWin(team,row) and isAwayTeam(team,row) and row["HomeTeam"].replace(" ", "") in topHalf :
                    thv+=1
                    data[0]["TopHalfVictories"].append(thv)
                elif isWin(team,row) and isHomeTeam(team,row) and row["AwayTeam"].replace(" ", "") in topHalf :
                    thv+=1
                    data[0]["TopHalfVictories"].append(thv)
                else:
                    data[0]["TopHalfVictories"].append(thv)

                if isWin(team,row) and isAwayTeam(team,row) and row["HomeTeam"].replace(" ", "") in bottomHalf :
                    bhv+=1
                    data[0]["BottomHalfVictories"].append(bhv)
                elif isWin(team,row) and isHomeTeam(team,row) and row["AwayTeam"].replace(" ", "") in bottomHalf :
                    bhv+=1
                    data[0]["BottomHalfVictories"].append(bhv)
                else:
                    data[0]["BottomHalfVictories"].append(bhv)






        tables.append(pd.DataFrame(data=data[0],index=data[1]))


        #tables.append(data)
        #pd.DataFrame(data=data)
    return tables





def main():
    
#Teams of the current season broken up into top and bottom half based on
#their historical positon between 1-10 and 11-20
    
    topHalf1 = ['ManUnited', 'Leicester', 'Bournemouth',
               'Chelsea', 'Tottenham',
               'Wolves', 'Everton', 'Arsenal', 'ManCity', 'Liverpool']
    
    bottomHalf1 = [ 'Cardiff', 'Fulham','CrystalPalace',
                  'Huddersfield', 'Newcastle',  'Watford',
                  'Brighton',  'WestHam','Southampton', 'Burnley']
    
#--------------------------------------------------------------------------   
#Teams of the current season broken up into top and bottom half based on
#their historical positon between 1-10 and 11-20
    topHalf2 = ['Arsenal', 'Leicester', 'ManCity', 
                'Chelsea', 'CrystalPalace', 'Everton',
                'Liverpool', 'Bournemouth', 'ManUnited', 
                'Tottenham']
    
    bottomHalf2 = ['Brighton', 'Burnley', 'CrystalPalace', 'Huddersfield', 
                 'Stoke', 'Southampton', 'Swansea', 'Watford', 'WestBrom',
                'WestHam', 'Newcastle', ]

#--------------------------------------------------------------------------   
#Teams of the current season broken up into top and bottom half based on
#their historical positon between 1-10 and 11-20
    topHalf3 = ['Everton', 'Tottenham', 'Leicester', 'ManCity',
                'Southampton', 'Arsenal', 'Liverpool', 'ManUnited',
                'Chelsea', 'WestHam']
    
    bottomHalf3 = ['Burnley', 'Swansea', 'CrystalPalace', 'WestBrom', 
                   'Hull',  'Sunderland', 'Middlesbrough', 'Stoke',  
                   'Watford', 'Bournemouth',]
#--------------------------------------------------------------------------   
#Teams of the current season broken up into top and bottom half based on
#their historical positon between 1-10 and 11-20
    
    topHalf4 = [ 'Chelsea', 'Swansea', 'ManUnited', 'Tottenham',  
                'CrystalPalace', 'Arsenal', 'Southampton', 'Stoke', 
                'Liverpool',  'ManCity']

    bottomHalf4 = ['Bournemouth', 'AstonVilla',  'Everton', 'Watford', 
                   'Leicester', 'Sunderland', 'Norwich',   'WestHam', 
                   'Newcastle',  'WestBrom']
    
    
#loading csv files into pandas data frame
    seasonResultDF = pd.read_csv("season-1819_csv.csv")
    seasonResultDF2 = pd.read_csv("season-1718_csv.csv")
    seasonResultDF3 = pd.read_csv("season-1617_csv.csv")
    seasonResultDF4 = pd.read_csv("season-1516_csv.csv")
    
    
#Retrieving the teams for each season
    
    teams = teamsx(seasonResultDF)
    teams2 = teamsx(seasonResultDF2)
    teams3 = teamsx(seasonResultDF3)
    teams4 = teamsx(seasonResultDF4)
    
  
    
    
# Loading the various derived stats from the first pandas data from
#into another data frame
    dfs1819 = progressionTables(teams,seasonResultDF,topHalf1,bottomHalf1)
    dfs1718 = progressionTables(teams2,seasonResultDF2,topHalf2,bottomHalf2)
    dfs1617 = progressionTables(teams3,seasonResultDF3,topHalf3,bottomHalf3)
    dfs1516 = progressionTables(teams4,seasonResultDF4,topHalf4,bottomHalf4)
    
    
#The above were list of pandas data frame
#concatenating them into one large data frame
#for each season
    allData1819 = pd.concat(dfs1819)
    allData1718 = pd.concat(dfs1718)
    allData1617 = pd.concat(dfs1617)
    allData1516 = pd.concat(dfs1516)
    

#creating the training data from all seasons except for 18/19
    trainingData = allData1516
    trainingData = trainingData.append(allData1617,ignore_index=True)
    trainingData = trainingData.append(allData1718,ignore_index=True)
    
#test data. In a dictionary form as each team has the own data frame
#for their own performance for the 18/19 season
    Season1819TestX = {k:v.drop("Points", axis = 1) for (k,v) in zip(teams, dfs1819)}
    Season1819TestY = {k:v[["Points"]] for (k,v) in zip(teams, dfs1819)}
    

 
        
    #--------------------------------------------------------------------------
        
    
    #Season1819TestY = {k:v[["Points"]] for (k,v) in zip(teams, dfs1819)}
    

#dropping the unecessary column so only my independent columns of
# away victory, topHalf victories and bottom half victories remain

    newXTrain = trainingData.drop(["Points","Wins","Loss","Draws"], axis = 1)
    newXTest = allData1819.drop(["Points","Wins","Loss","Draws"], axis = 1)
    YTrain = trainingData[["Points"]]
    
#creating regression model
    regressionModel = LinearRegression()
    
    
#fit model
    regressionModel.fit(newXTrain,YTrain)
    
    
#Printing each teams predicted performance for the 18/19
#season using 19/18 x values

    for k in Season1819TestX:
        print("The current team is: " + k)
        #print(Season1819TestX[k])
        y_Predict = regressionModel.predict(Season1819TestX[k].drop(["Wins","Loss","Draws"], axis = 1))
        print(y_Predict[37:38], "is the predicted final points after the last match of the season")
        print()
        
        # calculate the mean squared error
        model_mse = mean_squared_error(Season1819TestY[k], y_Predict)
        # calculate the mean absolute error
        model_mae = mean_absolute_error(Season1819TestY[k], y_Predict)
        # calulcate the root mean squared error
        model_rmse =  math.sqrt(model_mse)
        # display the output
        print("MSE {:.3}".format(model_mse))
        print("MAE {:.3}".format(model_mae))
        print("RMSE {:.3}".format(model_rmse))
        print()
        print()
        
        
    
        
    
    
    
    







if __name__ == '__main__':
    main()
