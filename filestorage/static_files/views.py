from django.http.response import HttpResponse
from time import sleep


def get_dummy_static_file(request, file_name):
    print(f"Uploading {file_name} started.")
    sleep(1)
    print(f"Uploading {file_name} finished.")
    return HttpResponse(200)
