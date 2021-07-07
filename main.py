import cv2 as cv


class ImageToAscii:
    def __init__(self, path, re_val):
        self.path = path
        self.frames_list = []
        self.ASCII = ['@', '#', 'S', '/', '\\', '*', '+', ';', ':', ',']
        self.resize_fact = re_val

    def load_image(self):
        image = cv.imread(self.path)
        image = cv.resize(image, (image.shape[1] // self.resize_fact,
                                  image.shape[0] // self.resize_fact))
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        return image

    def image_ascii(self, *args, **kwargs):
        try:
            if args:
                img = args[0]
            else:
                img = self.load_image()
            rows, cols = img.shape
            frame = "\n"
            for i in range(rows):
                for j in range(cols):
                    im_val = img.item(i, j)
                    frame += self.ASCII[im_val // 30]
                frame += "\n"
            print(frame)
            return frame
        except Exception as e:
            print(e)


obj = ImageToAscii("res/elephant.jpg", 5)
obj.image_ascii()