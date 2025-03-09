from facexformer_pipeline import FacexformerPipeline
from image_input_handler import UniversalImageInputHandler

def main():
    # Đường dẫn đến hình ảnh cần xử lý
    image_path = "captured_image.jpg"
    
    # Xử lý hình ảnh đầu vào
    uih = UniversalImageInputHandler(image_path, debug=False)
    img = uih.img
    
    # Khởi tạo pipeline với task 'age_gender_race'
    pipeline = FacexformerPipeline(debug=True, tasks=['age_gender_race'])
    
    # Chạy model để lấy kết quả
    results = pipeline.run_model(img)
    
    # Xuất kết quả
    if "age_gender_race_dict" in results:
        print("Kết quả phân loại tuổi, giới tính, chủng tộc:")
        print(results["age_gender_race_dict"])
    else:
        print("Không có kết quả.")

if __name__ == "__main__":
    main()
