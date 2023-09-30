"""from deepface import DeepFace
import pandas as pd


# df = DeepFace.find(img_path="C:\\Users\\Nathan\\PycharmProjects\\Basics-1\\target.jpg" ,db_path="C:\\Users\\Nathan\\PycharmProjects\\Basics-1\\my_db")
df = DeepFace.find(img_path="C:\\Users\\srivi\\PycharmProjects\\deep\\target.jpg",
                   db_path="C:\\Users\\srivi\\my_db", distance_metric='cosine')

# Check if there are any entries in df
if df!=0:
    # The child is found
    print("The child is found.")
    print(df)
else:
    # No data found
    print("No data found.")"""
from flask import Flask, request, jsonify

import os
import numpy as np

app = Flask(__name__)
db_path = "C:\\Users\\srivi\\my_db"
model_path = "C:\\Users\\srivi\\my_db\\representations_vgg_face.pkl"


"""def training():
    # Check if the model file exists and delete it if it does
    if os.path.exists(model_path):
        os.remove(model_path)

    # Recreate the representations by finding faces in the database images
    DeepFace.build_model(db_path)

    print("Training complete. New representations created.")"""

from deepface import DeepFace
import pandas as pd
"""
def training():
    if os.path.exists(model_path):
        os.remove(model_path)
    # Specify the correct model_name here (e.g., "VGG-Face")
    model_name = "representations_vgg_face.pkl"

    DeepFace.build_model(model_name)
"""




def upload_image(image_path):
    # Manually copy or move the image to your database directory
    if os.path.exists(model_path):
        os.remove(model_path)
    image_filename = os.path.basename(image_path)
    destination_path = os.path.join(db_path, image_filename)

    # Copy the image to the database directory
    os.rename(image_path, destination_path)

    # Check if the representations need to be trained


db_directory = "C:\\Users\\srivi\\my_db"


def find_target(image_path):
    try:
        # Run the code to find a target image with enforce_detection set to False
        df = DeepFace.find(img_path=image_path, db_path=db_directory, distance_metric='cosine', enforce_detection=False)
        uploaded_file = request.files['image']
        # Check if there are any entries in df
        if df!=0:
            # The child is found
            print("The child is found.")
            list_str = '\n'.join(map(str, df))

            # Specify the file path
            file_path = "D:\\list.txt"

            # Open the file in write mode
            with open(file_path, 'w') as file:
                # Write the string representation to the file
                file.write(list_str)

            # Confirm that the data is written to the file
            print(f'The list has been stored in {file_path}')
            # Open the file in read mode
            with open(file_path, 'r') as file:
                # Read the first three lines
                top_three_lines = [next(file) for _ in range(4)]

            # Display the top three lines
            print("Top three lines:")
            for line in top_three_lines:
                print(line.strip())  # Remove trailing newline characters

        else:
            # No data found
            print("No data found.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
upload_directory = "C:\\Users\\srivi\\my_db"
@app.route('/image', methods=['POST'])
def image():
    try:
        uploaded_file = request.files['image']
        if uploaded_file:
            # Save the uploaded image to the upload directory
            image_filename = os.path.join(upload_directory, uploaded_file.filename)
            uploaded_file.save(image_filename)

            # Check if the file was successfully saved
            if os.path.exists(image_filename):
                print(f"Image '{uploaded_file.filename}' has been successfully saved to {upload_directory}")

                # Call the find_target function with the image path as a parameter
                find_target(image_filename)

                return "Image upload and processing completed."
            else:
                print("Failed to save the uploaded image.")
        else:
            print("No image file uploaded.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    return "Image upload completed."


if __name__ == '__main__':
    app.run(debug=True)


