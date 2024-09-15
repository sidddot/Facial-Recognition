import face_recognition

# Load an image with a face
image = face_recognition.load_image_file("./Images/Sidharth.jpg")

# Find all face locations in the image
face_locations = face_recognition.face_locations(image)

# Assuming there's only one face in the image
if len(face_locations) == 1:
    # Extract face encodings
    face_encodings = face_recognition.face_encodings(image, face_locations)

    # Convert face encoding to a hash
    face_hash = face_encodings[0]

    print("Face hash:", face_hash)
else:
    print("Error: Either no face found or multiple faces found in the image.")
