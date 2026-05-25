import streamlit as st
import google.generativeai as genai

# إعداد واجهة التطبيق
st.set_page_config(page_title="AnimeFlow Studio", page_icon="🎬")
st.title("🎬 AnimeFlow Studio - مصنع أفلام الأنمي")
st.markdown("تحويل أفكارك عن Zedko و Shru إلى سيناريوهات سينمائية.")

# إعداد الـ API
api_key = st.sidebar.text_input("أدخل مفتاح Google AI API:", type="password")

# المدخلات
idea = st.text_area("اكتب فكرتك للمشهد القادم:", "Zedko يواجه Shru في قتال ملحمي.")

if st.button("صناعة السيناريو"):
    if not api_key:
        st.error("يرجى إدخال مفتاح API من Google AI Studio أولاً.")
    else:
        try:
            genai.configure(api_key=api_key)
            
            with st.spinner('المخرج Gemini يكتب السيناريو...'):
                # تجربة استدعاء النموذج بالاسم الصافي المستقر
                try:
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    prompt = f"أنت مخرج أنمي محترف. اكتب سيناريو مشهد أنمي مفصل ومشوق للشخصيتين Zedko و Shru بناءً على الفكرة التالية: {idea}. ركز على أسلوب وإثارة Dragon Ball Super، واجعل الأحداث حماسية ومليئة بالطاقة المذهلة."
                    response = model.generate_content(prompt)
                except Exception:
                    # آلية احتياطية في حال رفض السيرفر الاسم الأول
                    model = genai.GenerativeModel('models/gemini-1.5-flash')
                    prompt = f"أنت مخرج أنمي محترف. اكتب سيناريو مشهد أنمي مفصل ومشوق للشخصيتين Zedko و Shru بناءً على الفكرة التالية: {idea}. ركز على أسلوب وإثارة Dragon Ball Super، واجعل الأحداث حماسية ومليئة بالطاقة المذهلة."
                    response = model.generate_content(prompt)
                
                st.success("تم الانتهاء بنجاح!")
                st.write("### 🎬 السيناريو الملحمي الناتج:")
                st.write(response.text)
        except Exception as e:
            st.error(f"حدث خطأ أثناء الاتصال: {e}")

st.sidebar.markdown("---")
st.sidebar.info("للحصول على المفتاح: [Google AI Studio](https://aistudio.google.com/)")
