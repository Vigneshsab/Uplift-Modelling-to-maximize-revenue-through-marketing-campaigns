# Predicting-the-max.-profit-a-company-could-generate-using-Uplift-Modelling
***
This project discusses about the various types of Uplift Modelling. A sample dataset which contains many parameters including Promotion, Response etc.. were given as an input to the models. 

The main aim of the project is to see if the company could generate more revenue by giving discounts to a selected number of customers based on previous campaign data and other parameters such as income, no. of web visits, children etc.. The cost to send out a promotion to a customer is $3 and the revenue generated if the customer purchases with that promotion is $11. 

With this information, we can calculate the revenue by using a formula

                                    revenue=11*n_treat_purch - 3*n_treat + 11*n_control_purch
                                    
There are numerous approaches to tackle this problem. I have chosen to implement uplift models to optimize the promotional strategy. 4 different types of uplift models were implemented:

  1) Traditional Uplift Model
  2) Two Models Approach
  3) Single Model with Treatment Indicator Variable
  4) Four Quadrant Approach
  
  # Dataset
  ***

