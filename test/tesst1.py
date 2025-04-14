from facexformer_pipeline import FacexformerPipeline
from image_input_handler import UniversalImageInputHandler

AGE_MAPPING = {
    0: "0-9",
    1: "10-19",
    2: "20-29",
    3: "30-39",
    4: "40-49",
    5: "50-59",
    6: "60+"
}

GENDER_MAPPING = {
    0: "Male",
    1: "Female"
}

RACE_MAPPING = {
    0: "Asian",
    1: "Black",
    2: "White",
    3: "Indian",
    4: "Other"
}

def map_age(age):
    return AGE_MAPPING.get(age, str(age))

def map_gender(gender):
    return GENDER_MAPPING.get(gender, str(gender))

def map_race(race):
    return RACE_MAPPING.get(race, str(race))

def main():
    # Đường dẫn đến hình ảnh cần xử lý
    imageArr = [
                "../public/blackman.jpg", "../public/indanman.jpg",
                "../public/oldman.jpg","../public/lena.jpg"
                ]
    for image_path in imageArr:
        # Xử lý hình ảnh đầu vào
        uih = UniversalImageInputHandler(image_path, debug=False)
        img = uih.img
        
        # Khởi tạo pipeline với task 'age_gender_race'
        pipeline = FacexformerPipeline(debug=True, tasks=['age_gender_race'])
        
        # Chạy model để lấy kết quả
        results = pipeline.run_model(img)
        
        # Xuất kết quả
        if "age_gender_race_dict" in results:
            print(f"Result for age, gender, race detection for object { image_path.split('/')[2].split('.')[0] } :")
            age_display = map_age(results["age_gender_race_dict"]['age'])
            gender_display = map_gender(results["age_gender_race_dict"]['gender'])
            race_display = map_race(results["age_gender_race_dict"]['race'])
            print(f"Age: {age_display} | Gender: {gender_display} | Race: {race_display} \n\n")
        else:
            print("Không có kết quả.")

if __name__ == "__main__":
    main()
