# Price-Optimization
First of all we are taking data that based upon both internal and external data there we are selecting only categorical variables from all data-set . 
These categorical variables direct impact on profit prediction , these categorical variables (date-time) are to be taken in boolean form “0” and “1” . Here “1” =>“yes” while “0”=>”No” .
The data would be customized with 32 columns and rows  with little modification ,this addition of some external data is date value in boolean form . 
These data-set contain 32(columns) and 263(rows).
Now there we are labeling profit variable with some important categorical variable separately ,replacing each NAN value with average input value . 
In the first of processing we are converting categorical variables into numeric form for further processing and then using bi-variate bar graph to visualize the relationship between profit and the predicted variables this relation would be established between categorical and profit variable and then checking mean, std , maximum ,and min values of quantitative variables . 
Here product-Sale-Price run the scatter plot together to get both linear and 2nd order fit lines for x121_2012 , checking significance using regression analysis by including all other predictors .
