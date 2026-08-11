from preprocessing import engineer_features
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error, root_mean_squared_error
import joblib

site_df = engineer_features()

def model(df):
    exog_cols = [[]]
    split_index = 0.80
    X_train_rf, X_test_rf = site_df[exog_cols].iloc[:split_index], site_df[exog_cols].iloc[split_index:]
    y_train_rf, y_test_rf = y.iloc[:split_index], y.iloc[split_index:]

    rf = RandomForestRegressor(n_estimators=300, random_state=42)
    rf.fit(X_train_rf, y_train_rf)
    y_pred_rf = rf.predict(X_test_rf)

    mask_rf = y_test_rf != 0 #
    mape_rf = mean_absolute_percentage_error(y_test_rf[mask_rf], y_pred_rf[mask_rf])
    print(f'Random Forest MAPE: {mape_rf:.3f}')

    pd.Series(rf.feature_importances_, index=exog_cols).sort_values(ascending=False)

    # save model
    joblib.save(model)


