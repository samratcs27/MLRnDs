from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
from pandas import DataFrame
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from sklearn.model_selection import RandomizedSearchCV
from sklearn import metrics
import datetime
pd.set_option('display.max_columns', 50)


class RFModelTrainer:

    model = None

    @classmethod
    def randomisedGridSearch(cls):
        # Number of trees in random forest
        n_estimators = [int(x) for x in np.linspace(start=100, stop=1200, num=12)]
        # Number of features to consider at every split
        max_features = ['auto', 'sqrt']
        # Maximum number of levels in tree
        max_depth = [int(x) for x in np.linspace(5, 30, num=6)]
        # max_depth.append(None)
        # Minimum number of samples required to split a node
        min_samples_split = [2, 5, 10, 15, 100]
        # Minimum number of samples required at each leaf node
        min_samples_leaf = [1, 2, 5, 10]

        random_grid = {'n_estimators': n_estimators,
                       'max_features': max_features,
                       'max_depth': max_depth,
                       'min_samples_split': min_samples_split,
                       'min_samples_leaf': min_samples_leaf}

        return random_grid

    @classmethod
    def trainData(cls, df: DataFrame):
        df = df[
            ['Year', 'Selling_Price', 'Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission',
             'Owner']]
        df['Current Year'] = datetime.datetime.today().year
        df['no_year'] = df['Current Year'] - df['Year']
        df.drop(['Year'], axis=1, inplace=True)
        print(df.head())
        df = pd.get_dummies(df, drop_first=True)
        print(df.head())
        df = df.drop(['Current Year'], axis=1)
        X = df.iloc[:, 1:]
        y = df.iloc[:, 0]
        model = ExtraTreesRegressor()
        model.fit(X, y)
        feature_importances = pd.Series(model.feature_importances_, index=X.columns)
        X = X[list(feature_importances.nlargest(5).index)]


        print("Train-Test Split")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

        print("Now train")
        rf = RandomForestRegressor()
        # Random search of parameters, using 3 fold cross validation,
        # search across 100 different combinations
        rf_random = RandomizedSearchCV(estimator=rf, param_distributions=cls.randomisedGridSearch(), scoring='neg_mean_squared_error',
                                       n_iter=10, cv=5, verbose=2, random_state=42, n_jobs=1)

        rf_random.fit(X_train, y_train)
        print(rf_random.best_params_)
        print(rf_random.best_score_)
        predictions = rf_random.predict(X_test)

        print('MAE:', metrics.mean_absolute_error(y_test, predictions))
        print('MSE:', metrics.mean_squared_error(y_test, predictions))
        print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

        return rf_random

    @classmethod
    def predictData(cls, df: DataFrame):
        df = df[
            ['Year', 'Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission',
             'Owner']]
        df['Current Year'] = datetime.datetime.today().year
        df['no_year'] = df['Current Year'] - df['Year']
        df.drop(['Year'], axis=1, inplace=True)
        df = pd.get_dummies(df, drop_first=True)
        df = df.drop(['Current Year'], axis=1)
        if cls.model is not None:
            result = cls.model.predict(df.values)

        print("\n\n")
        result = pd.DataFrame(result, columns=['Selling_price_forecasted'])

        return result






