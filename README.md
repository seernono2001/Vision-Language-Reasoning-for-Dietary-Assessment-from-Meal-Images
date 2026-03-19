# Vision Language Reasoning for Dietary Assessment from Meal Images
Semester project CVSE for building a system that detects the nutritional values of a picture of food, and give advices using VLM.

## General Pipeline
1. Careful image data augmentation designed to improve depth estimation and thereby support more confident predictions.
2. We will leverage pretrained foundation models. In particular, we require a novel view synthesis model, an object detection model to identify food items on a plate, and adopt an existing VLM that can jointly process visual and textual context in order to support caloric estimation and nutritional guidance.
3. A reliable mapping from the predicted food classes to nutritional values, integrating the information distilled from visual detection, including portion-size estimates, to produce accurate estimates of calories and macronutrients, e.g., mapping a detected pizza slice to an estimated caloric and nutritional profile such as 300 calories and 5 g of protein.
4. Compute a trained health score vector given the nutritional metrics.

## Quickstart
Inside the project folder, run the following
- **Windows:**  
``` 
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt  
python RAG_model.py
```
- **Mac/Linux:**
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python RAG_model.py
```

- **Note:**
You will need to add an API key by yourself, you can use Groq to get one for testing:
https://console.groq.com/

## Important Dates
| Dates  |  |
| ------------- | ------------- |
| 4/3  | Project Feasibility Study  |
| 4/24  | Project Midterm Report  |
| 5/4  | Project Final Report  |
