# %%
import pandas as pd
import glob,os
# %%
data_lake_file_path=os.path.join('Data','Emily')
JDAT_file_path=os.path.join('Data','JDAT')
BOOST2_file_path=os.path.join('Data','BOOST-II_UTAH_MOBERG_CLEANED_HDF5_FILES')
for root, dirs, files in os.walk(JDAT_file_path):
    Ilayda_file_path=os.path.join(root,files[1])
    
Ilayda_df=pd.read_excel(Ilayda_file_path)
patient_lst=Ilayda_df.MRN.unique()
measure_lst=Ilayda_df['Measure_Description'].unique()

# %%
def select_patient(patient_MRN,df):
    assert patient_MRN in df['MRN'].unique()
    patient_df=df[df['MRN']==patient_MRN]
    return patient_df

def select_measure(measure_name,df):
    assert measure_name in df['Measure_Description'].unique()
    measure_df=df[df['Measure_Description']==measure_name]
    return measure_df

def create_meta_data_dict(df):
    meta_data_dict={}
    out_df=df.copy()
    for col in df.columns:
        if len(df[col].unique())==1:
            meta_data_dict[col]=df[col].unique()
            out_df=out_df.drop([col],axis=1)
    # out_df['meta_data']=pd.DataFrame.from_dict(meta_data_dict)
    return meta_data_dict,out_df
# %%

# %%
# my_patient_df=select_patient('MR1111569',Ilayda_df)
# %%
# my_measure_df=select_measure('ICP MEAN (MMHG)',my_patient_df)
# %%
# out_dict,out_df=create_meta_data_dict(my_measure_df)
# %%
