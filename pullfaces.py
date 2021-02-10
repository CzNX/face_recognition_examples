from PIL import Image
import face_recognition

image = face_recognition.load_image_file('./img/groups/team1.jpg')
face_locations = face_recognition.face_locations(image)

for face_location in face_locations:
    t, r, b, l = face_location

    face_image = image[t:b,l:r]
    pil_image = Image.fromarray(face_image)
    # # pil_image.show()
    # pil_image.save(f'{t}.jpg')
    print(pil_image)