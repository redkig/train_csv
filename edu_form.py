import pandas as pd
df =pd.read_csv("train.csv")
df.drop(["id","bdate",'has_photo','has_mobile','followers_count','graduation','relation','life_main','people_main','city','last_seen','occupation_name','career_start','career_end'], axis=1,inplace=True)
df.info()
df['education_form'].fillna("Full-time", inplace=True)

def education_form_1(edu_form):
    if edu_form == "Full-time":
        return 0 
    elif edu_form == "Part-time":
        return 2
    elif edu_form == "Distance Learning":
        return 3
    else:
        return 4
df['education_form'] = df['education_form'].apply(education_form_1)
print(df["education_form"].value_counts())