from fractions import Fraction
import numpy as np
import pandas as pd



from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromedriver = r"C:\Users\robla\Downloads\chromedriver_win32 (3)\chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--incognito')
chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
#chrome_options.add_argument('--headless')

driver = webdriver.Chrome(options = chrome_options,executable_path = chromedriver)

# ============================================================================================================================================================================
# Defining URL's for FanDuel line pages MLB
# ============================================================================================================================================================================

fanduel_mlb = 'https://sportsbook.fanduel.com/sports/navigation/1110.1/7627.1'


# ============================================================================================================================================================================
# FanDuel Function to get Odds and Team Names
# ============================================================================================================================================================================


driver.get(fanduel_mlb)
mlb_moneyline_market = driver.find_elements_by_class_name("selectionprice")
mlb_teams_slate = driver.find_elements_by_class_name("name")
mlb_total_indicators = driver.find_elements_by_class_name("had-value")
mlb_totals = driver.find_elements_by_class_name("uo-currenthandicap")
mlb_handicaps = driver.find_elements_by_class_name("currenthandicap")


mlb_odds_list = []
mlb_teams_playing = []     # slate of teams currently listed on fanduels page
mlb_over_under_indicators = []
mlb_over_unders = []
mlb_points_spread = []

for i in mlb_moneyline_market:
  mlb_odds_list.append(i.text)
for i in mlb_teams_slate:
  mlb_teams_playing.append(i.text)
for i in mlb_total_indicators:
  mlb_over_under_indicators.append(i.text)
for i in mlb_totals:
  mlb_over_unders.append(i.text)
for i in mlb_handicaps:
  mlb_points_spread.append(i.text)

for i in mlb_points_spread:
  if (i == ''):
    i = '0'
    


#print(mlb_points_spread)




teams = mlb_teams_playing[1:len(mlb_teams_playing)]

matchups = []

k = 0

while (k < len(teams) - 1):
  matchups.append(teams[k] + " vs. " + teams[k+1])
  k += 2
  continue

###############################################################################
i = 0
handicap_values = []

# Getting Handicap values for spread lines

while ( i < len(mlb_points_spread)):
  
  handicap_values.append(mlb_points_spread[i])
  handicap_values.append(mlb_points_spread[i+2])
  
  i += 6
  
  continue
  
###############################################################################


#print("\n", mlb_odds_list)

#print("\n Moneyline Index Map [team_name_index]{spread index,moneyline index,total index}")
#print("""

#      [0] {0,2,4}
#      [1] {1,3,5}
#      [2] {6,8,10}
#      [3] {7,9,11}
#       .
#       .
#       .
#      [n]""")

##############################################################################

mlb_spread_index_list = []             # Listing Indices for Spread Odds
counter = 0

while (counter < len(mlb_odds_list)):
  mlb_spread_index_list.append(counter)
  mlb_spread_index_list.append(counter + 1)
  counter += 6
  continue

##############################################################################
  
mlb_ml_index_list = []              # Listing Indices for Moneyline Odds
counter = 2

while (counter < len(mlb_odds_list)):
  mlb_ml_index_list.append(counter)
  mlb_ml_index_list.append(counter + 1)
  counter += 6
  continue

##############################################################################

mlb_over_under_index_list = []            # Listing Indices for O/U Odds
counter = 4

while (counter < len(mlb_odds_list)):
  mlb_over_under_index_list.append(counter)
  mlb_over_under_index_list.append(counter + 1)
  counter += 6
  continue

##############################################################################

mlb_spread = []
mlb_moneyline = []
mlb_over_under = []

for i in range(0,len(mlb_ml_index_list)):
  mlb_moneyline.append(mlb_odds_list[mlb_ml_index_list[i]])
  
for i in range(0,len(mlb_spread_index_list)):
  mlb_spread.append(mlb_odds_list[mlb_spread_index_list[i]])

for i in range(0,len(mlb_over_under_index_list)):
  mlb_over_under.append(mlb_odds_list[mlb_over_under_index_list[i]])



###############################################################################
  
#Making a refined O/U list to eventually put in a dictionary with matchup label
  
###############################################################################
  
mlb_Totals = []



if(len(mlb_over_under)==len(mlb_over_under_indicators)==len(mlb_over_unders)):
  
  j = 0
  
  while (j < len(mlb_over_under)):
    
    mlb_Totals.append(mlb_over_under_indicators[j])
    mlb_Totals.append(mlb_over_unders[j])
    mlb_Totals.append(mlb_over_under[j])
    
    j+=1
    
    continue
  
else:
  
  mlb_Totals = mlb_Totals
   

# ============================================================================================================================================================================
#  Slate Stuff -->> mlb_teams_playing = Ordered List of teams playing matchup by matchup 
#
#  Over/Under Stuff -->>   mlb_over_under_indicators = Alternating List of O's and U'S
#                          mlb_over_unders = Ordered List of totals for each matchup
#                          mlb_over_under = Ordered List of associated american odds
#                                          for corresponding Over or Under pick
#  
#  Moneyline Stuff -->>    mlb_moneyline = Ordered List of associated american odds
#  
#  
#  Spread Stuff -->>       mlb_spread = Ordered list of associated american odds
#                          handicap_values = Ordered list of points spread values
# 
#  
#  
#  
#  
# ============================================================================================================================================================================



# Making Data Frames
  
# moneyline
  
columns = ['Team','Odds']
moneyline_df = pd.DataFrame(mlb_teams_playing)
moneyline_df['odds'] = mlb_moneyline
moneyline_df.columns = columns
moneyline_df.head(-1)  




def kelly(C,B,name_a,a,prob_a,name_b,b,prob_b):

  # kelly(Capital,Default Unit,name a,a moneyline,a prob,name b,b moneyline,b prob)

  f_1 = 0  # fractional odds for a
  d_1 = 0  # decimal odds for a
  i_1 = 0  # implied odds for a

  f_2 = 0  # fractional odds for b
  d_1 = 0  # decimal odds for b
  i_2 = 0  # implied odds for b


  if (a > 0):

    d_1 = abs(a)/100 + 1               # Decimal odds for a
    i_1 = 100*100/(a + 100)            # Implied odds for a
    f_1 = str(Fraction(abs(a),100))    # Fractional odds for a

  if (a < 0):

    d_1 = 100/abs(a) + 1               # Decimal odds for a
    i_1 = 100*abs(a)/(abs(a) + 100)    # Implied odds for a
    f_1 = str(Fraction(100,abs(a)))    # Fractional odds for a


  if (b > 0):

    d_2 = abs(b)/100 + 1               # Decimal odds for b
    i_2 = 100*100/(b + 100)            # Implied odds for b
    f_2 = str(Fraction(abs(b),100))    # Fractional odds for b

  if (b < 0):

    d_2 = 100/abs(b) + 1               # Decimal odds for b
    i_2 = 100*abs(b)/(abs(b) + 100)    # Implied odds for b
    f_2 = str(Fraction(100,abs(b)))    # Fractional odds for b


  no_vig_odds_1 = i_1/(i_1 + i_2)
  no_vig_odds_2 = i_2/(i_1 + i_2)

  vig = round(i_1 + i_2 - 100,3)

  odds_1 = [a, round(d_1,4), f_1, round(i_1,4), round(no_vig_odds_1,4),str(round(prob_a*100,5)) + "% Prob"]
  odds_2 = [b, round(d_2,4), f_2, round(i_2,4), round(no_vig_odds_2,4),str(round(prob_b*100,5)) + "% Prob"]

  pot_profit_1 = d_1 - 1
  pot_profit_2 = d_2 - 1
  
  potential_loss = B
  
# =============================================================================
#   Expected Value = (pot profit)*(prob of win) - (pot losses)*(prob of loss)
#   Potential losses are at most always what we initially wager
#   f = (Expected Value)/(pot profit)
# 
#   Note:
#
#   Using no vig odds is a relatively poor estimate of win/loss probability.
#   Need to figure out a way to better estimate either by using historical data,
#   online projection, or my own statistical model.
#   
#
#   Figuring out a rubust and accurate estimate of win probability is
#   what makes the Kelly Criterion for sports betting highly profitable
#
# =============================================================================



  EV_1 = round(pot_profit_1 * prob_a - potential_loss *(1-prob_a),4)
  EV_2 = round(pot_profit_2 * prob_b - potential_loss *(1-prob_b),4)

  EV = [EV_1, EV_2]

  kelly_fraction_1 = 0
  kelly_fraction_2 = 0


  if (EV[0] > 0):
    kelly_fraction_1 = EV[0]/(pot_profit_1)
    if kelly_fraction_1 >= .1:
      print("\n","BIG BET WARNING")
  else:
    kelly_fraction_1 = 0

  if (EV[1] > 0):
    kelly_fraction_2 = EV[1]/(pot_profit_2)
    if kelly_fraction_1 >= .1:
      print("\n","BIG BET WARNING")
  else:
    kelly_fraction_2 = 0



  print("\n")
  print("Team: [American Odds, decimal odds, fractional odds, implied odds %, no vig implied prob, projected probability] \n")
  print(name_a,": " ,odds_1, "\n")
  print(name_b,": " ,odds_2, "\n")
  print("!!!",vig,"% Juice","!!!", "\n")
  print("$",round(pot_profit_1,2), "Potential profit per dollar bet on ",name_a)
  print("$",EV_1,"EV per dollar betting on", name_a , "at" ,a, "odds" ,'&',prob_a,'probability',"\n")
  print("$" ,round(pot_profit_2,1), "Potential profit per dollar bet on ",name_b)
  print("$",EV_2,"EV per dollar betting on", name_b , "at" ,b, "odds" ,'&',prob_b,'probability',"\n")
  print("\u0192\u2081 =",round(kelly_fraction_1,4))
  print("\u0192\u2082 =",round(kelly_fraction_2,4),"\n")
  print("Optimized Bet on", name_a," = $",round(C*kelly_fraction_1,2) ,
        " w/ initial bankroll = $",C,", Total EV = $",
        round(round(C*kelly_fraction_1,2)*d_1 - round(C*kelly_fraction_1,2),2),"\n")

  print("Optimized Bet on", name_b," = $",round(C*kelly_fraction_2,2) ,
        " w/ initial bankroll = $",C,", Total EV = $",
        round(round(C*kelly_fraction_2,2)*d_1 - round(C*kelly_fraction_2,2),2))
  
  print("\n","------------------------------------------------------------------------------------------------------")



  return

