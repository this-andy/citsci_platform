import os

from citsci_platform.photos.models import Photo


if __name__ == "__main__":

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
    print(MIGRATION_MODULES)


    photos = Photo.objects.all()

    for photo in photos:
        photo.extract_image_info()

    #
    #
    # if len(argv) < 2:
    #     print("Usage:\n\t{} image1 [image2 [...]]".format(argv[0]))
    # imgs = []
    # for img in argv[1:]:
    #     imgs += list(glob(img))
    # print("file\tx\ty\tz\tdirection\tspeed\ttime")
    # for img in imgs:
    # # for img in argv[1:]:
    #     with Image.open(img) as image:
    #         # exif_data = get_exif_data(image)
    #         # gps_info = get_clean_gps_info(exif_data)
    #         gps_info = get_clean_gps_info_from_image(image)
    #         print("{}\t{Longitude:.6f}\t{Latitude:.6f}\t{Altitude:.3f}\t{Speed}\t{TimeStamp}".format(img, **gps_info))
    #
