import streamlit as st
import pandas as pd
import numpy as np

st.title("محاسبه Allowable Stress")
st.write("این یک نسخه آزمایشی برای خواندن فایل اکسل شماست.")

# خواندن فایل اکسل (بهتر است کش شود تا سرعت بالا برود)
@st.cache_data
def load_data():
    # نام فایل باید دقیقاً هم‌نام فایلی باشد که آپلود کرده‌اید
    file_name = 'Alowable Stress Data Bank.xlsx'
    # خواندن همه شیت‌ها
    xls = pd.read_excel(file_name, sheet_name=None, header=None)
    return xls

try:
    data = load_data()
    st.success("فایل اکسل با موفقیت بارگذاری شد!")
    
    # استخراج نام شیت‌ها به عنوان Design Code
    sheet_names = list(data.keys())
    
    # حذف شیت Input Data از لیست کدهای طراحی
    if 'Input Data' in sheet_names:
        sheet_names.remove('Input Data')
        
    design_code = st.selectbox("Design Code (انتخاب شیت):", sheet_names)
    
    if design_code:
        df = data[design_code]
        st.write(f"نمایش 5 سطر اول از اطلاعات {design_code}:")
        st.dataframe(df.head())
        
except Exception as e:
    st.error(f"خطا در خواندن فایل: {e}")
