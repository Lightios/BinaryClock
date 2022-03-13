from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.clock import Clock
import time


class BinaryClock(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"

        Clock.schedule_interval(lambda dt: self.update_time(), 1)

    def update_time(self):
        """
        Updates images every second
        :return: None
        """
        hour = int(time.strftime("%H"))
        minute = int(time.strftime("%M"))
        second = int(time.strftime("%S"))

        hour_tens = hour // 10
        hour_ones = hour % 10

        minute_tens = minute // 10
        minute_ones = minute % 10

        second_tens = second // 10
        second_ones = second % 10

        hour_tens_binary = bin(hour_tens).replace("0b", "")
        hour_tens_binary = self.adjust_length(hour_tens_binary, 2)

        hour_ones_binary = bin(hour_ones).replace("0b", "")
        hour_ones_binary = self.adjust_length(hour_ones_binary, 4)

        minute_tens_binary = bin(minute_tens).replace("0b", "")
        minute_tens_binary = self.adjust_length(minute_tens_binary, 3)

        minute_ones_binary = bin(minute_ones).replace("0b", "")
        minute_ones_binary = self.adjust_length(minute_ones_binary, 4)

        second_tens_binary = bin(second_tens).replace("0b", "")
        second_tens_binary = self.adjust_length(second_tens_binary, 3)

        second_ones_binary = bin(second_ones).replace("0b", "")
        second_ones_binary = self.adjust_length(second_ones_binary, 4)

        for i in range(2):
            self.root.ids.hour_tens.children[i].source = "Images/Glowing.jpg" if hour_tens_binary[i] == "1" else "Images/empty.jpg"

        for i in range(4):
            self.root.ids.hour_ones.children[i].source = "Images/Glowing.jpg" if hour_ones_binary[i] == "1" else "Images/empty.jpg"

        for i in range(3):
            self.root.ids.minute_tens.children[i].source = "Images/Glowing.jpg" if minute_tens_binary[i] == "1" else "Images/empty.jpg"

        for i in range(4):
            self.root.ids.minute_ones.children[i].source = "Images/Glowing.jpg" if minute_ones_binary[i] == "1" else "Images/empty.jpg"

        for i in range(3):
            self.root.ids.second_tens.children[i].source = "Images/Glowing.jpg" if second_tens_binary[i] == "1" else "Images/empty.jpg"

        for i in range(4):
            self.root.ids.second_ones.children[i].source = "Images/Glowing.jpg" if second_ones_binary[i] == "1" else "Images/empty.jpg"

    @staticmethod
    def adjust_length(binary_number: str, size: int) -> str:
        """
        Changes given number by adding 0 at the beginning
        :param binary_number: number to change
        :param size: expected size
        :return: changed number
        """
        for i in range(size - len(binary_number)):
            binary_number = "0" + binary_number

        return binary_number


Window.size = (300, 200)
BinaryClock().run()
