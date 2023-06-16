from django.shortcuts import render
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np

def home(request):
    return render(request, 'home.html')

def home3(request):
    return render(request, 'home3.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    data = load_breast_cancer()
    X = data.data
    Y = data.target
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train, Y_train)

    var1 = float(request.GET['n1'])
    var2 = float(request.GET['n2'])
    var3 = float(request.GET['n3'])
    var4 = float(request.GET['n4'])
    var5 = float(request.GET['n5'])
    var6 = float(request.GET['n6'])
    var7 = float(request.GET['n7'])
    var8 = float(request.GET['n8'])
    var9 = float(request.GET['n9'])
    var10 = float(request.GET['n10'])
    var11 = float(request.GET['n11'])
    var12 = float(request.GET['n12'])
    var13 = float(request.GET['n13'])
    var14 = float(request.GET['n14'])
    var15 = float(request.GET['n15'])
    var16 = float(request.GET['n16'])
    var17 = float(request.GET['n17'])
    var18 = float(request.GET['n18'])
    var19 = float(request.GET['n19'])
    var20 = float(request.GET['n20'])
    var21 = float(request.GET['n21'])
    var22 = float(request.GET['n22'])
    var23 = float(request.GET['n23'])
    var24 = float(request.GET['n24'])
    var25 = float(request.GET['n25'])
    var26 = float(request.GET['n26'])
    var27 = float(request.GET['n27'])
    var28 = float(request.GET['n28'])
    var29 = float(request.GET['n29'])
    var30 = float(request.GET['n30'])

    pred = model.predict(np.array([[var1, var2, var3, var4, var5, var6, var7, var8, var9, var10,
                                    var11, var12, var13, var14, var15, var16, var17, var18, var19, var20,
                                    var21, var22, var23, var24, var25, var26, var27, var28, var29, var30]]))
  

    result = ""
    if pred == 0:
        result = "The model predicts that the tumor is likely to be Benign, indicating a lower risk of cancer."
    else:
        result = "The model predicts that the tumor is likely to be Malignant, indicating a higher risk of cancer."


    return render(request, 'home3.html', {"result2": result})
