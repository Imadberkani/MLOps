import pandas as pd
from sklearn.preprocessing import LabelEncoder


def get_feat_and_target(df, target):
    """
    Get features and encoded target variables seperately from given dataframe and target
    input: dataframe and target column
    output: two dataframes for x and y
    """
    x = df.drop(target, axis=1)
    encoder = LabelEncoder()
    y_label = df[target]
    encoder.fit(y_label)
    y = pd.DataFrame(encoder.fit_transform(y_label), columns=[target])
    return x, y


def test_get_feat_and_target():
    df = pd.DataFrame(columns=["A", "B", "C"])
    target = "B"
    x, y = get_feat_and_target(df, target)
    assert all([a == b for a, b in zip(x.columns, ["A", "C"])])
    assert all([a == b for a, b in zip(y.columns, ["B"])])
