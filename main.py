from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.storage.jsonstore import JsonStore

from kivymd.app import MDApp

from datetime import datetime
import time
from collections import defaultdict
from random import randint

from kivymd.uix.picker import MDThemePicker


Window.size = (1150, 690)
Window.top = 165/2
Window.left = 385/2


Builder.load_file('screens/av.kv')
Builder.load_file('screens/cntt(lt).kv')
Builder.load_file('screens/cntt(th).kv')
Builder.load_file('screens/home.kv')
Builder.load_file('screens/lt(lt).kv')
Builder.load_file('screens/lt(th).kv')
Builder.load_file('screens/td.kv')
Builder.load_file('screens/trr(lt).kv')
Builder.load_file('screens/trr(th).kv')
Builder.load_file('screens/vtp(lt).kv')
Builder.load_file('screens/vtp(th).kv')


class ColorCard(Screen):
    pass

class HomeScreen(Screen):
    def add_card(self):
        self.add_widget(ColorCard())
    def remove_card(self, color_card):
        self.remove_widget(color_card)


class AVCard(Screen):
    pass

class LTCNTTCard(Screen):
    pass

class THCNTTCard(Screen):
    pass

class LTLTCard(Screen):
    pass

class THLTCard(Screen):
    pass

class TDCard(Screen):
    pass

class LTTRRCard(Screen):
    pass

class THTRRCard(Screen):
    pass

class LTVTPCard(Screen):
    pass

class THVTPCard(Screen):
    pass


class UpdateVariables(Screen): 
    timelablepr = ObjectProperty(None)
    currentpr = ObjectProperty(None)
    nextpr = ObjectProperty(None)

    # mon_cardpr = ObjectProperty(None)
    # tue_cardpr = ObjectProperty(None)
    # wed_cardpr =  ObjectProperty(None)
    # thu_cardpr = ObjectProperty(None)
    # fri_cardpr = ObjectProperty(None)
    # sat_cardpr = ObjectProperty(None)


    # t1_cardpr = ObjectProperty(None)
    # t2_cardpr = ObjectProperty(None)
    # t3_cardpr = ObjectProperty(None)
    # t4_cardpr = ObjectProperty(None)
    # t5_cardpr = ObjectProperty(None)
    # t6_cardpr = ObjectProperty(None)
    # t7_cardpr = ObjectProperty(None)
    # t8_cardpr = ObjectProperty(None)
    # t9_cardpr = ObjectProperty(None)
    # t10_cardpr = ObjectProperty(None)

    weekday = StringProperty()
    hour = NumericProperty()
    minute = NumericProperty()
    second = NumericProperty()
    minute_in_day = NumericProperty()

    mon_avpr = ObjectProperty(None)
    mon_cntt_ltpr = ObjectProperty(None)
    mon_cntt_thpr = ObjectProperty(None)
    mon_lt_ltpr = ObjectProperty(None)
    mon_lt_thpr = ObjectProperty(None)
    mon_tdpr = ObjectProperty(None)
    mon_trr_ltpr = ObjectProperty(None)
    mon_trr_thpr = ObjectProperty(None)
    mon_vtp_ltpr = ObjectProperty(None)
    mon_vtp_thpr = ObjectProperty(None)

    tiet1 = 7*60 + 30
    tiet2 = tiet1+60
    tiet3 = tiet2+50
    tiet3_5 = tiet3+25
    tiet4 = tiet3+60
    tiet5 = tiet4+50
    tiet6 = 12*60+30
    tiet7 = tiet6+50
    tiet8 = tiet7+60
    tiet8_5 = tiet8+25
    tiet9 = tiet8+50
    tiet10 = tiet9+60
    print(tiet9)

    print(tiet6, " , " ,tiet8_5)

    d = []
    blue = defaultdict(lambda: d)
    blue["bright"] = [0/255, 0/255, 155/255, 1]
    blue["dark"] = [100/255, 100/255, 1, 1]

    red = [200/255, 0/255, 0/255, 1]
    fcs_red = [159/255, 0/255, 0/255, 1]
    yellow = [200/255, 200/255, 0/255, 1]
    fcs_yellow = [150/255, 150/255, 0/255, 1]
    green = [0/255, 200/255, 0/255, 1]
    fcs_green = [0/255, 150/255, 0/255, 1]


    def __init__(self,**kwargs):
        super(UpdateVariables,self).__init__(**kwargs)
        Clock.schedule_interval((self.update_time), 1)
        self.now = datetime.now()

    def update_time(self, dt):
        #TimeWidget
        if time.strftime('%w') == "0":
            self.timelablepr.text = '[size=20][b]Chủ nhật, ' + time.strftime('ngày %d, tháng %m') + ', năm ' + time.strftime('%Y  -  %H:%M:%S')
        else:
            self.timelablepr.text = '[size=20][b]Thứ ' + str(int(time.strftime('%w')) + 1) + time.strftime(', ngày %d, tháng %m') + ', năm ' + time.strftime('%Y  -  %H:%M:%S')

        #Current-Sbj_colorWidget
        self.weekday = (time.strftime("%w"))
        self.hour = int(time.strftime("%H"))
        self.minute = int(time.strftime("%M"))
        self.second = int(time.strftime("%S"))
        self.minute_in_day = self.hour*60 + self.minute

        #binding_default_attributes
        self.currentpr.text = "Hiện tại không có môn nào"
        self.nextpr.text = "Kế tiếp không còn môn nào"
        # self.mon_cardpr.md_bg_color = self.blue[ScreenApp().mode]
        # self.tue_cardpr.md_bg_color = self.blue[ScreenApp().mode]
        # self.wed_cardpr.md_bg_color = self.blue[ScreenApp().mode]
        # self.thu_cardpr.md_bg_color = self.blue[ScreenApp().mode]
        # self.fri_cardpr.md_bg_color = self.blue[ScreenApp().mode]
        # self.sat_cardpr.md_bg_color = self.blue[ScreenApp().mode]

        self.mon_avpr.md_bg_color = self.green
        self.mon_avpr.focus_color = self.fcs_green
        self.mon_avpr.unfocus_color = self.green
        self.mon_cntt_ltpr.md_bg_color = self.green
        self.mon_cntt_ltpr.focus_color = self.fcs_green
        self.mon_cntt_ltpr.unfocus_color = self.green
        self.mon_cntt_thpr.md_bg_color = self.green
        self.mon_cntt_thpr.focus_color = self.fcs_green
        self.mon_cntt_thpr.unfocus_color = self.green
        self.mon_lt_ltpr.md_bg_color = self.green
        self.mon_lt_ltpr.focus_color = self.fcs_green
        self.mon_lt_ltpr.unfocus_color = self.green
        self.mon_lt_thpr.md_bg_color = self.green
        self.mon_lt_thpr.focus_color = self.fcs_green
        self.mon_lt_thpr.unfocus_color = self.green
        self.mon_tdpr.md_bg_color = self.green
        self.mon_tdpr.focus_color = self.fcs_green
        self.mon_tdpr.unfocus_color = self.green
        self.mon_trr_ltpr.md_bg_color = self.green
        self.mon_trr_ltpr.focus_color = self.fcs_green
        self.mon_trr_ltpr.unfocus_color = self.green
        self.mon_trr_thpr.md_bg_color = self.green
        self.mon_trr_thpr.focus_color = self.fcs_green
        self.mon_trr_thpr.unfocus_color = self.green
        self.mon_vtp_ltpr.md_bg_color = self.green
        self.mon_vtp_ltpr.focus_color = self.fcs_green
        self.mon_vtp_ltpr.unfocus_color = self.green
        self.mon_vtp_thpr.md_bg_color = self.green
        self.mon_vtp_thpr.focus_color = self.fcs_green
        self.mon_vtp_thpr.unfocus_color = self.green

        #if_statements
        if self.weekday == "1":
            if self.minute_in_day in range (self.tiet6):
                self.currentpr.text = "Hiện tại không có môn nào"
                self.nextpr.text = "Môn kế tiếp: [font=BarlowCondensed-SemiBold]Anh Văn[/font]\n(Bắt đầu sau " + str(((self.tiet6 - self.minute_in_day)//60)) + " giờ " + str(((self.tiet6 - self.minute_in_day)%60) - 1) + " phút " + str(60-self.second-1) + " giây)"
                self.mon_avpr.md_bg_color = self.yellow
                self.mon_avpr.focus_color = self.fcs_yellow
                self.mon_avpr.unfocus_color = self.yellow
            elif self.minute_in_day in range (self.tiet6, self.tiet9+50):
                self.currentpr.text = "Môn hiện tại: [font=BarlowCondensed-SemiBold]Anh Văn[/font]\n(Kết thúc sau " + str(((self.tiet9+50 - self.minute_in_day)//60)) + " giờ " + str(((self.tiet9+50 - self.minute_in_day)%60) - 1) + " phút " + str(60-self.second-1) + " giây)"
                self.nextpr.text = "Kế tiếp không còn môn nào"
                self.mon_avpr.md_bg_color = self.red
                self.mon_avpr.focus_color = self.fcs_red
                self.mon_avpr.unfocus_color = self.red

        elif self.weekday == "2":
            if self.minute_in_day in range (self.tiet1):
                self.currentpr.text = "Hiện tại không có môn nào"
                self.nextpr.text = "Môn kế tiếp: [font=BarlowCondensed-SemiBold]Thực hành Vi tích phân 1B[/font]\n(Bắt đầu sau " + str((self.tiet1 - self.minute_in_day)//60) + " giờ " + str(((self.tiet1 - self.minute_in_day)%60) - 1) + " phút " + str(60-self.second-1) + " giây)"
                self.mon_vtp_thpr.md_bg_color = self.yellow
                self.mon_vtp_thpr.focus_color = self.fcs_yellow
                self.mon_vtp_thpr.unfocus_color = self.yellow
                self.mon_trr_thpr.md_bg_color = self.yellow
                self.mon_trr_thpr.focus_color = self.fcs_yellow
                self.mon_trr_thpr.unfocus_color = self.yellow
            elif self.minute_in_day in range (self.tiet1, self.tiet3_5+1):
                self.currentpr.text = "Môn hiện tại: [font=BarlowCondensed-SemiBold]Thực hành Vi tích phân 1B[/font]\n(Kết thúc sau " + str(((self.tiet3_5 - self.minute_in_day)//60)) + " giờ " + str(((self.tiet3_5 - self.minute_in_day)%60) - 1) + " phút " + str(60-self.second-1) + " giây)"
                self.nextpr.text = "Môn kế tiếp: [font=BarlowCondensed-SemiBold]Thực hành Toán rời rạc[/font]\n(Bắt đầu sau " + str(((self.tiet3_5 - self.minute_in_day)//60)) + " giờ " + str(((self.tiet3_5 - self.minute_in_day)%60) - 1) + " phút " + str(60-self.second-1) + " giây)"
                self.mon_vtp_thpr.md_bg_color = self.red
                self.mon_vtp_thpr.focus_color = self.fcs_red
                self.mon_vtp_thpr.unfocus_color = self.red
                self.mon_trr_thpr.md_bg_color = self.yellow
                self.mon_trr_thpr.focus_color = self.fcs_yellow
                self.mon_trr_thpr.unfocus_color = self.yellow
            elif self.minute_in_day in range (self.tiet3_5, self.tiet5+50):
                self.currentpr.text = "Môn hiện tại: [font=BarlowCondensed-SemiBold]Thực hành Toán rời rạc[/font]\n(Kết thúc sau " + str(((self.tiet3_5 - self.minute_in_day)//60)) + " giờ " + str(((self.tiet3_5 - self.minute_in_day)%60) - 1) + " phút " + str(60-self.second-1) + " giây)"
                self.nextpr.text = "Kế tiếp không còn môn nào"
                self.mon_vtp_thpr.md_bg_color = self.green
                self.mon_vtp_thpr.focus_color = self.fcs_green
                self.mon_vtp_thpr.unfocus_color = self.green
                self.mon_trr_thpr.md_bg_color = self.red
                self.mon_trr_thpr.focus_color = self.fcs_red
                self.mon_trr_thpr.unfocus_color = self.red

        elif self.weekday == "3":
            if self.minute_in_day in range (self.tiet1):
                self.currentpr.text = "Hiện tại không có môn nào"
                self.nextpr.text = "Môn kế tiếp: [font=BarlowCondensed-SemiBold]Lí thuyết Toán rời rạc[/font]\n(Bắt đầu sau " + str((self.tiet1 - self.minute_in_day)//60) + " giờ " + str(((self.tiet1 - self.minute_in_day)%60) - 1) + " phút " + str(60-self.second-1) + " giây)"
                self.mon_trr_ltpr.md_bg_color = self.yellow
                self.mon_trr_ltpr.focus_color = self.fcs_yellow
                self.mon_trr_ltpr.unfocus_color = self.yellow
                self.mon_lt_thpr.md_bg_color = self.yellow
                self.mon_lt_thpr.focus_color = self.fcs_yellow
                self.mon_lt_thpr.unfocus_color = self.yellow
            elif self.minute_in_day in range (self.tiet1, self.tiet4+50):
                self.currentpr.text = "Môn hiện tại: [font=BarlowCondensed-SemiBold]Lí thuyết Toán rời rạc[/font]\n(Kết thúc sau " + str(((self.tiet4+50 - self.minute_in_day)//60)) + " giờ " + str(((self.tiet4+50 - self.minute_in_day)%60) - 1) + " phút " + str(60-self.second-1) + " giây)"
                self.nextpr.text = "Môn kế tiếp: [font=BarlowCondensed-SemiBold]Thực hành Nhập môn lập trình[/font]\n(Bắt đầu sau " + str(((self.tiet6 - self.minute_in_day)//60)) + " giờ " + str(((self.tiet6 - self.minute_in_day)%60) - 1) + " phút " + str(60-self.second-1) + " giây)"
                self.mon_trr_ltpr.md_bg_color = self.red
                self.mon_trr_ltpr.focus_color = self.fcs_red
                self.mon_trr_ltpr.unfocus_color = self.red
                self.mon_lt_thpr.md_bg_color = self.yellow
                self.mon_lt_thpr.focus_color = self.fcs_yellow
                self.mon_lt_thpr.unfocus_color = self.yellow
            elif self.minute_in_day in range (self.tiet6, self.tiet8_5):
                self.currentpr.text = "Môn hiện tại: [font=BarlowCondensed-SemiBold]Thực hành Nhập môn lập trình[/font]\n(Kết thúc sau " + str(((self.tiet8_5 - self.minute_in_day)//60)) + " giờ " + str(((self.tiet8_5 - self.minute_in_day)%60) - 1) + " phút " + str(60-self.second-1) + " giây)"
                self.nextpr.text = "Kế tiếp không còn môn nào"
                self.mon_trr_ltpr.md_bg_color = self.green
                self.mon_trr_ltpr.focus_color = self.fcs_green
                self.mon_trr_ltpr.unfocus_color = self.green
                self.mon_lt_thpr.md_bg_color = self.red
                self.mon_lt_thpr.focus_color = self.fcs_red
                self.mon_lt_thpr.unfocus_color = self.red

        elif self.weekday == "4":
            if self.minute_in_day in range (self.tiet1):
                self.currentpr.text = "Hiện tại không có môn nào"
                self.nextpr.text = "Môn kế tiếp: [font=BarlowCondensed-SemiBold]Lí thuyết Vi tích phân 1B[/font]\n(Bắt đầu sau " + str((self.tiet1 - self.minute_in_day)//60) + " giờ " + str(((self.tiet1 - self.minute_in_day)%60) - 1) + " phút " + str(60-self.second-1) + " giây)"
                self.mon_vtp_ltpr.md_bg_color = self.yellow
                self.mon_vtp_ltpr.focus_color = self.fcs_yellow
                self.mon_vtp_ltpr.unfocus_color = self.yellow
                self.mon_cntt_thpr.md_bg_color = self.yellow
                self.mon_cntt_thpr.focus_color = self.fcs_yellow
                self.mon_cntt_thpr.unfocus_color = self.yellow
            elif self.minute_in_day in range (self.tiet1, self.tiet4+50):
                self.currentpr.text = "Môn hiện tại: [font=BarlowCondensed-SemiBold]Lí thuyết Vi tích phân 1B[[/font]\n(Kết thúc sau " + str(((self.tiet4+50 - self.minute_in_day)//60)) + " giờ " + str(((self.tiet4+50 - self.minute_in_day)%60) - 1) + " phút " + str(60-self.second-1) + " giây)"
                self.nextpr.text = "Môn kế tiếp: [font=BarlowCondensed-SemiBold]Thực hành Nhập môn CNTT[/font]\n(Bắt đầu sau " + str(((self.tiet6 - self.minute_in_day)//60)) + " giờ " + str(((self.tiet6 - self.minute_in_day)%60) - 1) + " phút " + str(60-self.second-1) + " giây)"
                self.mon_vtp_ltpr.md_bg_color = self.red
                self.mon_vtp_ltpr.focus_color = self.fcs_red
                self.mon_vtp_ltpr.unfocus_color = self.red
                self.mon_cntt_thpr.md_bg_color = self.yellow
                self.mon_cntt_thpr.focus_color = self.fcs_yellow
                self.mon_cntt_thpr.unfocus_color = self.yellow
            elif self.minute_in_day in range (self.tiet6, self.tiet8_5):
                self.currentpr.text = "Môn hiện tại: [font=BarlowCondensed-SemiBold]Thực hành Nhập môn CNTT[/font]\n(Kết thúc sau " + str(((self.tiet8_5 - self.minute_in_day)//60)) + " giờ " + str(((self.tiet8_5 - self.minute_in_day)%60) - 1) + " phút " + str(60-self.second-1) + " giây)"
                self.nextpr.text = "Kế tiếp không còn môn nào"
                self.mon_vtp_ltpr.md_bg_color = self.green
                self.mon_vtp_ltpr.focus_color = self.fcs_green
                self.mon_vtp_ltpr.unfocus_color = self.green
                self.mon_cntt_thpr.md_bg_color = self.red
                self.mon_cntt_thpr.focus_color = self.fcs_red
                self.mon_cntt_thpr.unfocus_color = self.red

        elif self.weekday == "5":
            if self.minute_in_day in range (self.tiet1):
                self.currentpr.text = "Hiện tại không có môn nào"
                self.nextpr.text = "Môn kế tiếp: [font=BarlowCondensed-SemiBold]Lí thuyết Nhập môn lập trình[/font]\n(Bắt đầu sau " + str((self.tiet1 - self.minute_in_day)//60) + " giờ " + str(((self.tiet1 - self.minute_in_day)%60) - 1) + " phút " + str(60-self.second-1) + " giây)"
                self.mon_lt_ltpr.md_bg_color = self.yellow
                self.mon_lt_ltpr.focus_color = self.fcs_yellow
                self.mon_lt_ltpr.unfocus_color = self.yellow
                self.mon_tdpr.md_bg_color = self.yellow
                self.mon_tdpr.focus_color = self.fcs_yellow
                self.mon_tdpr.unfocus_color = self.yellow
            elif self.minute_in_day in range (self.tiet1, self.tiet4+50):
                self.currentpr.text = "Môn hiện tại: [font=BarlowCondensed-SemiBold]Lí thuyết Nhập môn lập trình[/font]\n(Kết thúc sau " + str(((self.tiet4+50 - self.minute_in_day)//60)) + " giờ " + str(((self.tiet4+50 - self.minute_in_day)%60) - 1) + " phút " + str(60-self.second-1) + " giây)"
                self.nextpr.text = "Môn kế tiếp: [font=BarlowCondensed-SemiBold]Thể dục[/font]\n(Bắt đầu sau " + str(((self.tiet8 - self.minute_in_day)//60)) + " giờ " + str(((self.tiet8 - self.minute_in_day)%60) - 1) + " phút " + str(60-self.second-1) + " giây)"
                self.mon_lt_ltpr.md_bg_color = self.red
                self.mon_lt_ltpr.focus_color = self.fcs_red
                self.mon_lt_ltpr.unfocus_color = self.red
                self.mon_tdpr.md_bg_color = self.yellow
                self.mon_tdpr.focus_color = self.fcs_yellow
                self.mon_tdpr.unfocus_color = self.yellow
            elif self.minute_in_day in range (self.tiet8, self.tiet9+50):
                self.currentpr.text = "Môn hiện tại: [font=BarlowCondensed-SemiBold]Thể dục[/font]\n(Kết thúc sau " + str(((self.tiet9+50 - self.minute_in_day)//60)) + " giờ " + str(((self.tiet9+50 - self.minute_in_day)%60) - 1) + " phút " + str(60-self.second-1) + " giây)"
                self.nextpr.text = "Kế tiếp không còn môn nào"
                self.mon_lt_ltpr.md_bg_color = self.green
                self.mon_lt_ltpr.focus_color = self.fcs_green
                self.mon_lt_ltpr.unfocus_color = self.green
                self.mon_tdpr.md_bg_color = self.red
                self.mon_tdpr.focus_color = self.fcs_red
                self.mon_tdpr.unfocus_color = self.red

        elif self.weekday == "6":
            if self.minute_in_day in range (self.tiet1):
                self.currentpr.text = "Hiện tại không có môn nào"
                self.nextpr.text = "Môn kế tiếp: [font=BarlowCondensed-SemiBold]Lí thuyết Nhập môn CNTT[/font]\n(Bắt đầu sau " + str((self.tiet1 - self.minute_in_day)//60) + " giờ " + str(((self.tiet1 - self.minute_in_day)%60) - 1) + " phút " + str(60-self.second-1) + " giây)"
                self.mon_cntt_ltpr.md_bg_color = self.yellow
                self.mon_cntt_ltpr.focus_color = self.fcs_yellow
                self.mon_cntt_ltpr.unfocus_color = self.yellow
            elif self.minute_in_day in range (self.tiet1, self.tiet4+50):
                self.currentpr.text = "Môn hiện tại: [font=BarlowCondensed-SemiBold]Lí thuyết Nhập môn CNTT[/font]\n(Kết thúc sau " + str(((self.tiet4+50 - self.minute_in_day)//60)) + " giờ " + str(((self.tiet4+50 - self.minute_in_day)%60) - 1) + " phút " + str(60-self.second-1) + " giây)"
                self.nextpr.text = "Kế tiếp không còn môn nào"
                self.mon_cntt_ltpr.md_bg_color = self.red
                self.mon_cntt_ltpr.focus_color = self.fcs_red
                self.mon_cntt_ltpr.unfocus_color = self.red


            


class ScreenApp(MDApp):
    bgimage = 'images/home_background' + str(randint(1, 9)) + '.jpg'

    red = [200/255, 0/255, 0/255, 1]
    fcs_red = [170/255, 0/255, 0/255, 1]
    yellow = [200/255, 200/255, 0/255, 1]
    fcs_yellow = [170/255, 170/255, 0/255, 1]
    green = [0/255, 200/255, 0/255, 1]
    fcs_green = [0/255, 170/255, 0/255, 1]

    d = []
    blue = defaultdict(lambda: d)
    blue["bright"] = [0/255, 0/255, 155/255, 1]
    blue["dark"] = [100/255, 100/255, 1, 1]

    dft_card_bg = defaultdict(lambda: d)
    dft_card_bg["dark"] = [0, 0, 0, 0.2]
    dft_card_bg["bright"] = [1, 1, 1, 0.2]

    fcs_card_bg = defaultdict(lambda: d)
    fcs_card_bg["dark"] = [0, 0, 0, 0.3]
    fcs_card_bg["bright"] = [1, 1, 1, 0.3]

    dft_thu_bg = defaultdict(lambda: d)
    dft_thu_bg["dark"] = [1, 1, 1, 0.1]
    dft_thu_bg["bright"] = [0, 0, 0, 0.1]

    fcs_thu_bg = defaultdict(lambda: d)
    fcs_thu_bg["dark"] = [1, 1, 1, 0.2]
    fcs_thu_bg["bright"] = [0, 0, 0, 0.2]

    dft_thu_bg_on = defaultdict(lambda: d)
    dft_thu_bg_on["dark"] = [1, 55/255, 55/255, 0.2]
    dft_thu_bg_on["bright"] = [200/255, 0, 0, 0.2]

    fcs_thu_bg_on = defaultdict(lambda: d)
    fcs_thu_bg_on["dark"] = [1, 55/255, 55/255, 0.3]
    fcs_thu_bg_on["bright"] = [200/255, 0, 0, 0.3]

    mode = StringProperty('bright')
    weekday = (time.strftime("%w"))

    def build(self):
        sm = ScreenManager(transition=FadeTransition(duration=0.1))
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(AVCard(name='av'))
        sm.add_widget(LTCNTTCard(name='cntt_lt'))
        sm.add_widget(THCNTTCard(name='cntt_th'))
        sm.add_widget(LTLTCard(name='lt_lt'))
        sm.add_widget(THLTCard(name='lt_th'))
        sm.add_widget(TDCard(name='td'))
        sm.add_widget(LTTRRCard(name='trr_lt'))
        sm.add_widget(THTRRCard(name='trr_th'))
        sm.add_widget(LTVTPCard(name='vtp_lt)'))
        sm.add_widget(THVTPCard(name='vtp_th'))
        return sm

    def __init__(self,**kwargs):
        super(ScreenApp,self).__init__(**kwargs)
        self.stored_data = JsonStore('data.json')
    
    def check(self, instance, value):
        if value:
            self.mode = 'dark'
        else:
            self.mode = 'bright'
    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()
    def selected(self,filename):
        self.ids.image.source = filename[0]
        

if __name__ == '__main__':
    ScreenApp().run()