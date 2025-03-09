from facexformer_pipeline import FacexformerPipeline

def agc_detection(img):
    pipeline = FacexformerPipeline(debug=True, tasks=['age_gender_race'])

    results = pipeline.run_model(img)
    
    # Xuất kết quả
    if "age_gender_race_dict" in results:
        return results["age_gender_race_dict"]
    else:
        return {"data": "not found image"}