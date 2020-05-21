# Predicting-the-max.-profit-a-company-could-generate-using-Uplift-Modelling

This project discusses about the various types of Uplift Modelling. A sample dataset which contains many parameters including Promotion, Response etc.. were given as an input to the models. 

The main aim of the project is to see if the company could generate more revenue by giving discounts to a selected number of customers based on previous campaign data and other parameters such as income, no. of web visits, children etc.. The cost to send out a promotion to a customer is $3 and the revenue generated if the customer accepts that promotion or purchases a product with that promotion is $11. 

With this information, we can calculate the revenue by using a formula

                                    revenue=11*n_treat_purch - 3*n_treat + 11*n_control_purch
                                    
Here,
    n_treat_purch - no. of customers were given a promotion and purchased a product
    n_treat - no. of customers who were given a promotion
    n_control_purch - no. of customers who were not given a promotion but purchased a product

There are numerous approaches to tackle this problem. I have chosen to implement uplift models to optimize the promotional strategy. 4 different types of uplift models were implemented:

  1) Traditional Uplift Model
  2) Two Models Approach
  3) Single Model with Treatment Indicator Variable
  4) Four Quadrant Approach
  
  # Dataset details
AcceptedCmp1 - 1 if customer accepted the offer in the 1st campaign, 0 otherwise    
AcceptedCmp2 - 1 if customer accepted the offer in the 2nd campaign, 0 otherwise
AcceptedCmp3 - 1 if customer accepted the offer in the 3rd campaign, 0 otherwise
AcceptedCmp4 - 1 if customer accepted the offer in the 4th campaign, 0 otherwise
AcceptedCmp5 - 1 if customer accepted the offer in the 5th campaign, 0 otherwise
Response (target) - 1 if customer accepted the offer in the last campaign, 0 otherwise
Complain - 1 if customer complained in the last 2 years
DtCustomer - date of customer’s enrolment with the company
Education - customer’s level of education
Marital - customer’s marital status
Kidhome - number of small children in customer’s household
Teenhome - number of teenagers in customer’s household
Income - customer’s yearly household income
MntFishProducts - amount spent on fish products in the last 2 years
MntMeatProducts - amount spent on meat products in the last 2 years
MntFruits - amount spent on fruits products in the last 2 years
MntSweetProducts - amount spent on sweet products in the last 2 years
MntWines - amount spent on wine products in the last 2 years
MntGoldProds - amount spent on gold products in the last 2 years
NumDealsPurchases - number of purchases made with discount
NumCatalogPurchases - number of purchases made using catalogue
NumStorePurchases - number of purchases made directly in stores
NumWebPurchases - number of purchases made through company’s web site
NumWebVisitsMonth - number of visits to company’s web site in the last month
Recency - number of days since the last purchase

