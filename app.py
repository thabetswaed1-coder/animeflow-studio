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
            
            with st.spinner('المخرج الذكي يكتب السيناريو الآن...'):
                # قائمة بالأسماء المدعومة (الجديدة والقديمة) ليجربها التطبيق تلقائياً
                models_to_try = ['gemini-2.5-flash', 'models/gemini-2.5-flash', 'gemini-1.5-flash', 'models/gemini-1.5-flash']
                response = None
                
                for model_name in models_to_try:
                    try:
                        model = genai.GenerativeModel(model_name)
                        prompt = f"أنت مخرج أنمي محترف. اكتب سيناريو مشهد أنمي مفصل ومشوق للشخصيتين Zedko و Shru بناءً على الفكرة التالية: {idea}. ركز على أسلوب وإثارة Dragon Ball Super، واجعل الأحداث حماسية ومليئة بالقوة."
                        response = model.generate_content(prompt)
                        if response:
                            break # إذا نجح، يخرج من الحلقة فوراً
                    except Exception:
                        continue # إذا فشل اسم، يجرب الاسم التالي تلقائياً
                
                if response:
                    st.success("تم الانتهاء بنجاح باهر!")
                    st.write("### 🎬 السيناريو الملحمي الناتج:")
                    st.write(response.text)
                else:
                    st.error("لم نتمكن من الاتصال بالنموذج، يرجى التحقق من صلاحية مفتاح الـ API الخاص بك.")
                    
        except Exception as e:
            st.error(f"حدث خطأ غير متوقع: {e}")

st.sidebar.markdown("---")
st.sidebar.info("للحصول على المفتاح: [Google AI Studio](https://aistudio.google.com/)")
