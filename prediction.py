import joblib

model = joblib.load('price_estimator.pkl')

cols = ['Isweekday','Isweekend','Isworkday','IsBankHoliday',
'ProductSalePrice','PurchasePrice','OrderItemQuantity']

values = []
print('kindly input 1/0 for attributes with values true/false')
for col in cols:
    temp = float(input(f'Enter {col}: '))
    values.append(temp)

print(model.predict([values]))