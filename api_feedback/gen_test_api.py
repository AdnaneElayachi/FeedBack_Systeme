import requests
from datetime import datetime
from faker import Faker
from PIL import Image
import io

# Initialize Faker
fake = Faker()

def generate_temp_image(file_format="JPEG", size=(100, 100)):
    """
    Create a temporary image in memory.
    :param file_format: Format of the image (default: JPEG)
    :param size: Size of the image (default: 100x100)
    :return: BytesIO object containing the image data
    """
    # Generate an image with a random color
    image = Image.new("RGB", size, color=(
        fake.random_int(0, 255),
        fake.random_int(0, 255),
        fake.random_int(0, 255)
    ))
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format=file_format)
    img_byte_arr.seek(0)
    return img_byte_arr  # Return a file-like object

def populate_history_entry_api(n=10):
    """
    Populate the database via the HistoryEntry API endpoint with fake data.
    :param n: Number of entries to create (default: 10)
    """
    for i in range(n):
        # Generate a temporary image
        image_file = generate_temp_image()

        # Prepare data for the API
        data = {
            "image_path": fake.file_path(category="image"),
            "prediction": fake.word(),
            "confidence": fake.pyfloat(min_value=0.1, max_value=1.0),
            "date": datetime.now().isoformat(),
            "latitude": fake.latitude(),
            "longitude": fake.longitude(),
        }
        
        # Prepare the file for upload
        files = {
            "image": (f"test_image_{i}.jpg", image_file, "image/jpeg")
        }
        
        # Send the POST request
        try:
            response = requests.post(
                "http://127.0.0.1:8000/api/v1/history_entries/",  # HistoryEntry endpoint
                data=data,
                files=files
            )
            print(f"[HistoryEntry {i+1}] Response Status: {response.status_code}, Response Body: {response.text}")
        except Exception as e:
            print(f"[HistoryEntry {i+1}] Error: {str(e)}")
        finally:
            image_file.close()  # Close the temporary file after use

def populate_feedback_api(n=10):
    """
    Populate the database via the Feedback API endpoint with fake data.
    :param n: Number of entries to create (default: 10)
    """
    for i in range(n):
        # Generate a temporary image
        image_file = generate_temp_image()

        # Prepare data for the API
        data = {
            "predicted_class": fake.word(),
            "suggested_class": fake.word(),
            "date": datetime.now().isoformat(),
            "latitude": fake.latitude(),
            "longitude": fake.longitude(),
        }
        
        # Prepare the file for upload
        files = {
            "image": (f"test_image_{i}.jpg", image_file, "image/jpeg")
        }
        
        # Send the POST request
        try:
            response = requests.post(
                "http://127.0.0.1:8000/api/v1/feedbacks/",  # Feedback API endpoint
                data=data,
                files=files
            )
            print(f"[Feedback {i+1}] Response Status: {response.status_code}, Response Body: {response.text}")
        except Exception as e:
            print(f"[Feedback {i+1}] Error: {str(e)}")
        finally:
            image_file.close()  # Close the temporary file after use

if __name__ == "__main__":
    # Number of entries to generate
    n = 10

    print(f"Populating the database with {n} entries for HistoryEntry...")
    populate_history_entry_api(n)

    print(f"\nPopulating the database with {n} entries for Feedback...")
    populate_feedback_api(n)