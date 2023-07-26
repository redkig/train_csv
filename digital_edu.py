#создай здесь свой индивидуальный проект!
import pandas as pd
df =pd.read_csv("train.csv")
df.drop(["id","bdate",'has_photo','has_mobile','followers_count','graduation','relation','life_main','people_main','city','last_seen','occupation_name','career_start','career_end'], axis=1,inplace=True)
df.info()
df['education_form'].fillna("Full-time", inplace=True)
df[list(pd.get_dummies(df['education_form']).columns)] = pd.get_dummies(df["education_form"])
df.drop(["education_form"],axis = 1,inplace = True)
def sex_apply(sex):
    if sex==2:
        return 0 
    return 1
df['sex']=df['sex'].apply(sex_apply)
print(df['education_status'].value_counts())
def edu_status_apply(edu_status):
    if edu_status == 'Undergraduate applicant':
        return 0 
    elif edu_status == "Student (Bachelor's)" or edu_status == 'Student (Specialist)' or  edu_status == "Student (Master's)":
        return 1
    elif edu_status == "Alumnus (Bachelor's)" or edu_status == 'Alumnus (Specialist)' or edu_status == "Alumnus (Master's)":
        return 2
    elif edu_status == "Candidate of Sciences":
        return 3
    else:
        return 4
df['education_status'] = df['education_status'].apply(edu_status_apply)
print(df["education_status"].value_counts())



    