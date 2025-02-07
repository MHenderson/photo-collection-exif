from exif import Image
import json

photos_collection_path = "/Users/matthew/1_Project/Photography/photo-collection/json/onetouch-archive-photo-2019.json"

with open(photos_collection_path, 'r') as f:
    photos_collection = json.load(f)

photo_path = photos_collection[0]['name']
month_name = photos_collection[0]['contents'][0]['name']
photo_file_name = photos_collection[0]['contents'][0]['contents'][0]['name']

image_path = photo_path + '/' + month_name + '/' + photo_file_name

with open(image_path, 'rb') as image_file:
    my_image = Image(image_file)

print(my_image.has_exif)

print(photos_collection[0]['contents'][0]['contents'][0])

photo_json = photos_collection[0]['contents'][0]['contents'][0]
photo_json.update(make = my_image.make, model = my_image.model)
print(photo_json)
