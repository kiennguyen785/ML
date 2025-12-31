import streamlit as st
import pandas as pd
import joblib
import os

@st.cache_resource
def load_assets():
    # Tự động lấy đường dẫn thư mục hiện tại để load file .pkl
    base_path = os.path.dirname(__file__)
    models = {
        "Random Forest": joblib.load(os.path.join(base_path, 'rf_model.pkl')),
        "Logistic Regression": joblib.load(os.path.join(base_path, 'log_reg.pkl')),
        "KNN": joblib.load(os.path.join(base_path,'knn_model.pkl'))
    }
    feature_names = joblib.load(os.path.join(base_path, 'feature_columns.pkl'))
    return models, feature_names
# Load mô hình và tên cột
try:
    all_models, feature_names = load_assets()
except Exception as e:
    st.error(f"Không tìm thấy file mô hình tại {os.path.dirname(__file__)}. Lỗi: {e}")
    st.stop()
st.title("Hệ thống Dự đoán Tình trạng Trầm cảm Sinh viên")

with st.form("predict_form"):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Thông tin cá nhân")
        gender = st.selectbox(
            "Giới tính", 
            options=[0, 1], 
            format_func=lambda x: 
                {0: "Nữ", 1: "Nam"}[x]
                )
        age = st.number_input("Tuổi", 18, 60, 18)
        city = st.selectbox(
            "Khu vực sinh sống:",
            options=[0, 1, 2], 
            format_func=lambda x: {0: "0 (Nông thôn)", 1: "1 (Thành phố vừa)", 2: "2 (Thành phố lớn)"}[x])
        working_prof = st.selectbox("Đang đi làm?", options=[0, 1], format_func=lambda x: {0: "Không", 1: "Có"}[x])
        family_hist = st.selectbox("Tiền sử gia đình có người mắc bệnh tâm thần?", options=[0, 1], format_func=lambda x: {0: "Không", 1: "Có"}[x])

    with col2:
        st.subheader("Học tập & Công việc")
        cgpa = st.slider("Điểm CGPA", 0.0, 10.0, 7.5)
        degree = st.selectbox("Bằng cấp hiện tại:", options=[1, 2, 3, 4], 
                              format_func=lambda x: {1: "1 (Phổ thông)", 2: "2 (Cử nhân)", 3: "3 (Thạc sĩ)", 4: "4 (Tiến sĩ)"}[x])
        acad_pressure = st.selectbox("Mức độ áp lực học tập:", options=[1, 2, 3, 4, 5], 
                                     format_func=lambda x: {1: "1 (Rất thấp)", 2: "2 (Ít)", 3: "3 (Trung bình)", 4: "4 (Cao)", 5: "5 (Cực cao)"}[x])
        job_sat = st.selectbox("Mức độ hài lòng công việc:", options=[0, 1, 2, 3, 4, 5],
                               format_func=lambda x: {0: "0 (Không đi làm)", 1: "1 (Kém)", 2: "2 (Ít)", 3: "3 (Trung bình)", 4: "4 (Tốt)", 5: "5 (Rất tốt)"}[x])
        study_sat = st.selectbox("Mức độ hài lòng việc học", options=[1, 2, 3, 4, 5],
                                 format_func=lambda x: {1: "1 (Kém)", 2: "2 (Ít)", 3: "3 (Trung bình)", 4: "4 (Tốt)", 5: "5 (Rất tốt)"}[x])
        study_hours = st.number_input("Số giờ học mỗi ngày", 1, 15, 6)

    with col3:
        st.subheader("Sức khỏe & Tâm lý")
        sleep = st.selectbox("Thời gian ngủ", [1, 2, 3], format_func=lambda x: {1: "1 (<5h)", 2: "2 (5-8h)", 3: "3 (>8h)"}[x])
        diet = st.selectbox("Chế độ ăn uống", [0, 1, 2], format_func=lambda x: {0: "0 (Lành mạnh)", 1: "1 (Trung bình)", 2: "2 (Kém)"}[x])
        suicidal = st.selectbox("Từng có ý nghĩ tự tử?", [0, 1], format_func=lambda x: {0: "Không", 1: "Có"}[x])
        work_pressure = st.selectbox("Mức độ áp lực công việc", options=[0, 1, 2, 3, 4, 5],
                                     format_func=lambda x: {0: "0 (Không áp lực)", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5 (Rất cao)"}[x])
        fin_stress = st.selectbox("Mức độ áp lực tài chính", options=[1, 2, 3, 4, 5],
                                  format_func=lambda x: {1: "1 (Thấp)", 2: "2", 3: "3", 4: "4", 5: "5 (Rất cao)"}[x])

    st.markdown("---")
    model_name = st.selectbox("Mô hình dự đoán", list(all_models.keys()))
    submit = st.form_submit_button("Dự đoán")

# 3. Xử lý dự đoán
if submit:
    # Đảm bảo đủ 16 giá trị khớp với feature_names
    input_values = [
        gender, age, city, working_prof, cgpa, 
        acad_pressure, study_sat, sleep, diet, 
        degree, suicidal, work_pressure, fin_stress, 
        family_hist, study_hours, job_sat
    ]
    
    input_df = pd.DataFrame([input_values], columns=feature_names)
    
    model = all_models[model_name]
    prediction = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0]

    st.markdown("---")
    if prediction == 1:
        st.error(f"KẾT QUẢ: Có dấu hiệu trầm cảm (Độ tin cậy: {prob[1]*100:.2f}%)")
        st.warning("Lời khuyên: Bạn nên dành thời gian nghỉ ngơi và chia sẻ với người thân.")
    else:
        st.success(f"KẾT QUẢ: Không có dấu hiệu trầm cảm (Độ tin cậy: {prob[0]*100:.2f}%)")
        st.balloons()