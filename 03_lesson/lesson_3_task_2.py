from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+791258852336"),
    Smartphone("Samsung", "Galaxy S21", "+791258852337"),
    Smartphone("Google", "Pixel 6", "+791258852338"),
    Smartphone("Huawei", "P40 Pro", "+791258852339"),
    Smartphone("Xiaomi", "Mi 11", "+791258852340")
]
for smartphone in catalog:
    print(
        f"{smartphone.phone_brand}-{smartphone.phone_model}."
        f"{smartphone.phone_number}"
          )
