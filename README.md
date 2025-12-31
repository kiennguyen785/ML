# DỰ ĐOÁN TRẦM CẢM
---
## Bài toán
Bộ dữ liệu này tổng hợp nhiều thông tin nhằm mục đích hiểu, phân tích và dự đoán mức độ trầm cảm ở sinh viên. Bộ dữ liệu được thiết kế cho mục đích nghiên cứu tâm lý học, khoa học dữ liệu và giáo dục, cung cấp thông tin chi tiết về các yếu tố góp phần gây ra những thách thức về sức khỏe tâm thần ở sinh viên và hỗ trợ thiết kế các chiến lược can thiệp sớm.

Mô tả bài toán
    
Bài toán nhằm phân tích và dự đoán mức độ trầm cảm của sinh viên dựa trên nhiều yếu tố liên quan đến học tập, công việc, thói quen sinh hoạt và hoàn cảnh cá nhân.

Mục tiêu:
1. Hiểu các yếu tố ảnh hưởng đến sức khỏe tinh thần của sinh viên
2. Xây dựng mô hình dự đoán xem một sinh viên có bị trầm cảm hay không
Mô tả dữ liệu: Định dạng: CSV (mỗi hàng đại diện cho một học sinh) Đặc trưng:
1. ID: Mã định danh
2. Age: Tuổi
3. Gender: Giới tính
4. Profession: Lĩnh vực công việc hoặc học tập của sinh viên
5. City: Thành phố hoặc khu vực nơi sinh viên cư trú
6. Academic Pressure: Áp lực học tập
7. Work Pressure: Áp lực công việc
8. CGPA: Điểm trung bình tích lũy của sinh viên
9. Study Satisfaction: Độ hài lòng trong học tập
10. Job Satisfaction: Độ hài lòng trong công việc
11. Sleep Duration: Số giờ ngủ
12. Dietary Habits: Đánh giá chế độ ăn uống
13. Degree: Bằng cấp hoặc chương trình học thuật mà sinh viên đang theo đuổi
14. Have you ever had suicidal thoughts : phản ánh liệu sinh viên đã từng có ý định tự tử hay chưa
15. Work/Study Hours: Số giờ trung bình mỗi ngày mà sinh viên dành cho công việc hoặc học tập
16. Financial Stress: Một thước đo mức độ căng thẳng do lo lắng về tài chính
17. Family History of Mental Illness: Cho biết liệu có tiền sử gia đình mắc bệnh tâm thần hay không (Có/Không)
18. Depression: Biến mục tiêu cho biết liệu học sinh có bị trầm cảm hay không (Có/Không)
Dữ liệu gồm: 27901 sample, 17 feature và 1 target
## Mục tiêu bài toán
Xây dựng mô hình dự đoán bệnh trầm cảm 
## Nguồn dữ liệu
Nguồn: kaggle
https://www.kaggle.com/datasets/adilshamim8/student-depression-dataset
## Pipeline
Dataset → EDA → Clean → Encode → Normalize → Train → Evaluate → Inference
## Mô hình sử dụng
Logistic Regression
Random Foress
K-Nearest Neighbors
## Kết quả
| Model | Accuracy | Precision | Recall | F1-score |
| :--- | :---: | :---: | :---: | :---: |
| Logistic Regression | 0.84 | 0.85 | 0.88 | 0.86 |
| K-Nearest Neighbors | 0.81 | 0.82 | 0.85 | 0.84 |
| Random Forest | 0.82 | 0.84 | 0.86 | 0.85 |
## Cách chạy
Chạy trên vscode hoặc colab với những cell code giống trong app/predict_depression.ipynb
## Tác giả
Nguyễn Trần Kiên - 12423018 - 12423TN12423TN
