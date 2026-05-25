import streamlit as st
import google.generativeai as genai

# إعداد واجهة التطبيق
st.set_page_config(page_title="AnimeFlow Studio", page_icon="🎬")
st.title("🎬 AnimeFlow Studio - مصنع أفلام الأنمي")
st.markdown("تحويل أفكارك عن Zedko و Shru إلى سيناريوهات سينمائية.")

# إعداد الـ API
api_key = st.sidebar.text_input("أدخل مفتاح Google AI API:", type="password")

# المدخلات
idea = st.text_area("اكتب فكرتك للمشهد القادم:", "مثال: Zedko يواجه Shru في قتال ملحمي.")

if st.button("صناعة السيناريو"):
    if not api_key:
        st.error("يرجى إدخال مفتاح API من Google AI Studio أولاً.")
    else:
        try:
            genai.configure(api_key=api_key)
            # تم تعديل السطر التالي ليعمل مباشرة بدون خطأ 404
            model = genai.GenerativeModel('models/gemini-1.5-flash')
            
            with st.spinner('المخرج Gemini يكتب السيناريو...'):
                prompt = f"أنت مخرج أنمي. اكتب سيناريو مفصل للشخصيتين Zedko و Shru بناءً على: {idea}. ركز على أسلوب Dragon Ball Super."
                response = model.generate_content(prompt)
                
                st.success("تم الانتهاء!")
                st.write("### السيناريو الملحمي:")
                st.write(response.text)
        except Exception as e:
            st.error(f"حدث خطأ: {e}")

# text formatting fixation
st.sidebar.markdown("---")
st.sidebar.info("للحصول على المفتاح: [Google AI Studio](https://aistudio.google.com/)")
