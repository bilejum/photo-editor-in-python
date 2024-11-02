import customtkinter
from PIL import Image, ImageOps


class App:
    def __init__(self):
        # customtkinter.set_default_color_theme("dark-blue")
        self.app = customtkinter.CTk()
        self.app.geometry("800x600")

        # app.grid_columnconfigure([0, 1, 2], weight=1)
        # app.grid_rowconfigure([0, 1, 2], weight=1)

        self.image_frame = customtkinter.CTkFrame(
            self.app, width=192 * 2, height=108 * 2
        )
        self.image_frame.grid(row=0, column=1, columnspan=1)
        # creat PIL object image
        self.my_image = Image.open("img\泉此方 壁纸.jpg")

        self.image_container = customtkinter.CTkImage(
            light_image=self.my_image, size=(192 * 2, 108 * 2)
        )

        self.image_label = customtkinter.CTkLabel(
            self.image_frame, image=self.image_container, text=""
        )

        self.image_label.grid(ipadx=30, ipady=30)
        # image_label.grid(row=0, column=0, sticky="news", columnspan=2, pady=200)

        left_button_frame = customtkinter.CTkFrame(self.app)
        left_button_frame.grid(column=0, row=0)
        flip_button = customtkinter.CTkButton(
            left_button_frame, text="翻转", command=self.flip_operation
        )
        flip_button.grid()

        addsize_button = customtkinter.CTkButton(left_button_frame, text="放大")
        addsize_button.grid()

    def run(self):
        self.app.mainloop()

    def flip_operation(self):
        self.my_image = ImageOps.flip(self.my_image)
        print("run_flip")
        self.image_label = customtkinter.CTkLabel(
            self.image_frame, image=self.image_container, text=""
        )


my_app = App()
my_app.run()
