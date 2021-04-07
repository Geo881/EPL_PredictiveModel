# EPL_PredictiveModel

Idea of Project: Being an avid fan of the English Premeir League(EPL) I wanted to see how well a 'model' was able to predict
the points of each teams given only a few variables, namely:
AwayVictories: Winning away from home
TopHalfVictories: Winning againts a team who is historically in the top 10
BottomHalfVictories: Winning againts a team who is historically in the bottom half of the table (bottom 10)

EPL Overview:
The English Premier League consists of 20 teams who play one another home and away resulting in 760 games each season. 
Each team play 38 games in the seasson. A team is given three points if they win, one point if they tie 
and no point if the lose to another team.


Given the popularity of the EPL the historical data regarding certain statistics were easy to find.
All the data came from  datahub.io and were in a CSV format. The data were obtained for four different seasons, 
2015/16, 2016/17, 2017/18, and the 2018/19 season. All theCSV files had the same format which can be seen below:



The data in the CSV had no malformed or empty cells, so I did not have to remove any data from the data frame. 
I, however, had to derive more data from the previously listed columns to obtain the below columns:
Points,  AwayVictories,  TopHalfVictories,  BottomHalfVictories,  Wins,  Loss,  Draws.


The listed columns were used into a table containing 38 rows representing the number of games that each team has to play each season. Each incrementing row would track the titled statistic for a particular team after a matchday where each row contains the increment stats from the previous row. (Done by the following function def progressionTables(teams,df,topHalf,bottomHalf): )

The resulting data frame would then be further divided into independent and dependent variable to train the model.


The columns were then broken into:
Points,  AwayVictories,  TopHalfVictories,  BottomHalfVictories
The columns containing wins, losses, and draws were dropped from the data frame. The columns of AwayVictories,  TopHalfVictories, and  BottomHalfVictories were chosen to be independent variables, and the Points column was chosen to be the dependent column. These columns were chosen to be the independent column as I wanted to see how well the model would predict the points of each team with the absence of losses and draws corresponding to each team.The model was trained on the data from 2015/16, 2016/17, 2017/18, and was validated on the 2018/19 season.



Output

MSE 2.35
MAE 1.15
RMSE 1.53


The current team is: Leicester
[[51.05120543]] is the predicted final points after the last match of the season

MSE 3.91
MAE 1.5
RMSE 1.98


The current team is: Bournemouth
[[45.93674967]] is the predicted final points after the last match of the season

MSE 7.84
MAE 2.69
RMSE 2.8


The current team is: Cardiff
[[34.93813321]] is the predicted final points after the last match of the season

MSE 1.31
MAE 0.965
RMSE 1.15


The current team is: Fulham
[[25.73012445]] is the predicted final points after the last match of the season

MSE 1.6
MAE 1.02
RMSE 1.26


The current team is: CrystalPalace
[[47.65165616]] is the predicted final points after the last match of the season

MSE 3.36
MAE 1.54
RMSE 1.83


The current team is: Huddersfield
[[11.91999755]] is the predicted final points after the last match of the season

MSE 3.06
MAE 1.52
RMSE 1.75


The current team is: Chelsea
[[73.04843835]] is the predicted final points after the last match of the season

MSE 6.45
MAE 2.43
RMSE 2.54


The current team is: Newcastle
[[41.84319667]] is the predicted final points after the last match of the season

MSE 3.87
MAE 1.68
RMSE 1.97


The current team is: Tottenham
[[78.1628941]] is the predicted final points after the last match of the season

MSE 40.4
MAE 6.19
RMSE 6.36


The current team is: Watford
[[48.80124258]] is the predicted final points after the last match of the season

MSE 4.85
MAE 1.88
RMSE 2.2


The current team is: Brighton
[[32.07364031]] is the predicted final points after the last match of the season

MSE 2.85
MAE 1.44
RMSE 1.69


The current team is: Wolves
[[53.86271588]] is the predicted final points after the last match of the season

MSE 3.64
MAE 1.55
RMSE 1.91


The current team is: Everton
[[51.61275303]] is the predicted final points after the last match of the season

MSE 1.0
MAE 0.842
RMSE 1.0


The current team is: Arsenal
[[71.15186574]] is the predicted final points after the last match of the season

MSE 5.44
MAE 1.94
RMSE 2.33


The current team is: ManCity
[[105.01344297]] is the predicted final points after the last match of the season

MSE 21.1
MAE 4.43
RMSE 4.6


The current team is: Liverpool
[[99.92547844]] is the predicted final points after the last match of the season

MSE 8.84
MAE 2.82
RMSE 2.97


The current team is: WestHam
[[52.2537743]] is the predicted final points after the last match of the season

MSE 1.97
MAE 1.1
RMSE 1.41


The current team is: Southampton
[[30.87107144]] is the predicted final points after the last match of the season

MSE 16.6
MAE 3.52
RMSE 4.07

The current team is: Burnley
[[38.39066494]] is the predicted final points after the last match of the season

MSE 1.4
MAE 1.03
RMSE 1.18

Link to Final English Priemier League Table 2018/19 season:
https://www.skysports.com/premier-league-table/2018


