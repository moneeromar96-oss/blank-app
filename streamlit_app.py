import streamlit as st

st.set_page_config(page_title="منظومة معتصم", layout="centered")
st.title("🏛️ منظومة الإدارة الذكية")

tab1, tab2 = st.tabs(["➕ إضافة موظف", "📋 سجل البيانات"])

with tab1:
    st.subheader("إدخال بيانات الموظف")
    with st.form("employee_form"):
        name = st.text_input("الأسم الكامل")
        nat_id = st.text_input("الرقم الوطني")
        grade = st.selectbox("الدرجة الوظيفية", ["الأولى", "الثانية", "الثالثة", "الرابعة", "خبير"])
        salary = st.number_input("الراتب الحالي", min_value=0)
        
        submit = st.form_submit_button("حفظ البيانات في المنظومة")
        if submit:
            st.success(f"✅ تم تسجيل الموظف: {name} بنجاح")

with tab2:
    st.subheader("قاعدة البيانات")
    st.info("سيتم عرض قائمة الموظفين هنا بعد الربط.")
