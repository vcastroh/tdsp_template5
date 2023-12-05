from load_data import load_data
from perform_eda import perform_eda

def prepare_data(data):
    data.isnull().sum()
    data.bmi[data.bmi.isnull()] = data.bmi.mean()
    data.bmi.isnull().sum()

    data.age = data.age.astype('int64')
    data['gender'].replace({'Male': 3, 'Female': 1, 'Other': 2}, inplace=True)
    data['gender'] = data['gender'].astype('uint8')

    data.hypertension = data.hypertension.astype('uint8')
    data.heart_disease = data.heart_disease.astype('uint8')

    label_encoder = LabelEncoder()
    data['smoking_status'] = label_encoder.fit_transform(data['smoking_status'])
    data.smoking_status = data.smoking_status.astype('uint8')

    data.ever_married[data.ever_married == 'Yes'] = 1
    data.ever_married[data.ever_married == 'No'] = 0
    data.ever_married = data.ever_married.astype('uint8')

    data.Residence_type[data.Residence_type == 'Rural'] = 1
    data.Residence_type[data.Residence_type == 'Urban'] = 0
    data.Residence_type = data.Residence_type.astype('uint8')

    work_type_dummies = pd.get_dummies(data['work_type'])
    data = pd.concat((data, work_type_dummies), axis=1)
    data.drop('work_type', axis=1, inplace=True)

    return data