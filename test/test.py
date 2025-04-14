# Import the pipeline class
from facexformer_pipeline import FacexformerPipeline
from image_input_handler import UniversalImageInputHandler 
from visual_debugger import VisualDebugger, Annotation, AnnotationType

# Initialize the pipeline with desired tasks
pipeline = FacexformerPipeline(tasks=['age_gender_race', 'headpose', 'landmark', 'faceparsing', 'attributes', 'visibility', 'age_gender_race'])

# Put your code for reading an image 
image_path = "../public/MU.jpg"
uih = UniversalImageInputHandler(image_path)   #  to use UniversalImageInputHandler you need "pip install image_input_handler"
img = uih.img
print(img)
# Run the model on an image
results = pipeline.run_model(img)

print(results)

# Access the results from results dictionary
print(results['headpose'])
print(results['landmarks']) 
print(results['faceparsing_mask']) 


# Also you can access intermediate results such as face region crop, face coordinates etc
print(results['face_ROI'])
print(results['face_coordinates']) 
print(results['head_coordinates']) 

vdebugger = VisualDebugger(tag="facex", debug_folder_path="./result", active=True)

annotation_landmarks_face_ROI = [Annotation(type=AnnotationType.POINTS, coordinates=results["landmarks_face_ROI"])]
annotation_landmarks = [Annotation(type=AnnotationType.POINTS, coordinates=results["landmarks"])]
annotation_headpose = [Annotation(type=AnnotationType.PITCH_YAW_ROLL, orientation=[results["headpose"]["pitch"],results["headpose"]["yaw"],results["headpose"]["roll"] ])]
annotation_face_coordinates = [Annotation(type=AnnotationType.RECTANGLE, coordinates=results["face_coordinates"])]
annotation_head_coordinates = [Annotation(type=AnnotationType.RECTANGLE, coordinates=results["head_coordinates"])]
annotation_faceparsing = [Annotation(type=AnnotationType.MASK, mask=results["faceparsing_mask"])]
annotation_faceparsing_head_ROI = [Annotation(type=AnnotationType.MASK, mask=results["faceparsing_mask_head_ROI"])]

vdebugger.visual_debug(img, name="original_image")
vdebugger.visual_debug(img, annotation_face_coordinates, name="", stage_name="face_coor")
vdebugger.visual_debug(results["face_ROI"], name="", stage_name="cropped_face_ROI")
vdebugger.visual_debug(img, annotation_head_coordinates, name="", stage_name="head_coor")
vdebugger.visual_debug(results["head_ROI"], name="", stage_name="cropped_head_ROI")
vdebugger.visual_debug(results["face_ROI"], annotation_landmarks_face_ROI, name="landmarks", stage_name="on_face_ROI")
vdebugger.visual_debug(img, annotation_landmarks, name="landmarks", stage_name="on_image")
vdebugger.visual_debug(results["face_ROI"], annotation_headpose, name="headpose")
vdebugger.visual_debug(results["head_ROI"], annotation_faceparsing_head_ROI, name="faceparsing", stage_name="mask_on_head_ROI")
vdebugger.visual_debug(img, annotation_faceparsing, name="faceparsing", stage_name="mask_on_full_image")
vdebugger.cook_merged_img() # creates merged image