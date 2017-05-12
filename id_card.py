# encoding:utf-8

import os
import random
import sys
from datetime import datetime

from data import list_prvoince, list_city, list_district

try:
    from tkinter import *
except ImportError:  # Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    # Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    # Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    # import tkFileDialog
    # import tkSimpleDialog
else:  # Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    # import tkinter.filedialog as tkFileDialog
    # import tkinter.simpledialog as tkSimpleDialog    #askstring()


class ApplicationUI(Frame):
    # 这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)

        # 主窗体
        self.top = self.winfo_toplevel()
        self.master.title(u'身份证号码生成器')
        self.master.geometry('495x450+468+165')
        self.master.resizable(width=False, height=False)

        # 创建控件
        self.style = Style()
        self.frm_auto = LabelFrame(self.top, text=u'随机生成', style='frm_auto.TLabelframe')
        self.lbl_frm_auto_txt1 = Label(self.frm_auto, text=u'随机生成', style='lbl_frm_auto_txt1.TLabel')
        self.ety_frm_auto_count = Entry(self.frm_auto, text='1', font=(u'微软雅黑', 9))
        self.lbl_frm_auto_txt2 = Label(self.frm_auto, text=u'个身份证号码', style='lbl_frm_auto_txt2.TLabel')
        self.txt_frm_auto_id = Text(self.frm_auto, wrap=WORD, font=(u'微软雅黑', 9))
        self.btn_frm_auto_generate = Button(self.frm_auto, text=u'开始生成', style='btn_frm_auto_generate.TButton')

        self.frm_condition = LabelFrame(self.top, text=u'选择生成', style='frm_condition.TLabelframe', relief='groove',
                                        borderwidth="4")
        self.lbl_frm_condition_district = Label(self.frm_condition, text=u'选择地区：',
                                                style='lbl_frm_condition_district.TLabel')
        self.cmb_frm_condition_province = Combobox(self.frm_condition, font=(u'微软雅黑', 9))
        self.cmb_frm_condition_city = Combobox(self.frm_condition, font=(u'微软雅黑', 9))
        self.cmb_frm_condition_district = Combobox(self.frm_condition, font=(u'微软雅黑', 9))
        self.cmb_frm_condition_year = Combobox(self.frm_condition, font=(u'微软雅黑', 9))
        self.cmb_frm_condition_month = Combobox(self.frm_condition, font=(u'微软雅黑', 9))
        self.cmb_frm_condition_day = Combobox(self.frm_condition, font=(u'微软雅黑', 9))
        self.lbl_frm_condition_birthday = Label(self.frm_condition, text=u'出生日期：',
                                                style='lbl_frm_condition_birthday.TLabel')
        self.lbl_frm_condition_gender = Label(self.frm_condition, text=u'性别：', style='lbl_frm_condition_gender.TLabel')
        self.cmb_frm_condition_gender = Combobox(self.frm_condition, font=(u'微软雅黑', 9))
        self.lbl_frm_condition_id = Label(self.frm_condition, text=u'身份证号码：', style='lbl_frm_condition_id.TLabel')
        self.ety_frm_condition_id = Entry(self.frm_condition, font=(u'微软雅黑', 9))
        self.btn_frm_condition_generate = Button(self.frm_condition, text=u'开始生成',
                                                 style='btn_frm_condition_generate.TButton')

        self.frm_parse = LabelFrame(self.top, text=u'解析身份证号码', style='frm_parse.TLabelframe')
        self.label_frm_parse_id = Label(self.frm_parse, text=u'身份证号码：', style='label_frm_parse_id.TLabel')
        self.ety_frm_parse_id = Entry(self.frm_parse, font=(u'微软雅黑', 9))
        self.lbl_frm_parse_district = Label(self.frm_parse, text=u'地区：', style='lbl_frm_parse_district.TLabel')
        self.ety_frm_parse_district = Entry(self.frm_parse, text=u'广东省深证市南山区', font=(u'微软雅黑', 9))
        self.lbl_frm_parse_birthday = Label(self.frm_parse, text=u'生日：', style='lbl_frm_parse_birthday.TLabel')
        self.ety_frm_parse_birthday = Entry(self.frm_parse, font=(u'微软雅黑', 9))
        self.ety_frm_parse_gender = Entry(self.frm_parse, font=(u'微软雅黑', 9))
        self.lbl_frm_parse_gender = Label(self.frm_parse, text=u'性别：', style='lbl_frm_parse_gender.TLabel')
        self.btn_frm_parse_reset = Button(self.frm_parse, text=u'清空内容', style='btn_frm_parse_reset.TButton')
        self.btn_frm_parse_parse = Button(self.frm_parse, text=u'开始解析', style='btn_frm_parse_parse.TButton')

        self.create_widgets()

    def create_widgets(self):
        # 随机生成身份证号码
        self.style.configure('frm_auto.TLabelframe', font=(u'微软雅黑', 9))
        self.frm_auto.place(x=5, y=5, width=190, height=240)

        self.style.configure('lbl_frm_auto_txt1.TLabel', anchor='center', font=(u'微软雅黑', 9))
        self.lbl_frm_auto_txt1.place(x=0, y=10, width=70, height=23)

        self.ety_frm_auto_count.place(x=70, y=10, width=30, height=23)

        self.style.configure('lbl_frm_auto_txt2.TLabel', anchor='w', font=(u'微软雅黑', 9))
        self.lbl_frm_auto_txt2.place(x=100, y=10, width=80, height=23)

        self.txt_frm_auto_id.place(x=20, y=50, width=140, height=105)

        self.style.configure('btn_frm_auto_generate.TButton', font=(u'微软雅黑', 9))
        self.btn_frm_auto_generate.place(x=20, y=170, width=60, height=25)

        # 选择生成身份证号码
        self.style.configure('frm_condition.TLabelframe', font=(u'微软雅黑', 9))
        self.frm_condition.place(x=190, y=5, width=300, height=240)

        self.style.configure('lbl_frm_condition_district.TLabel', anchor='w', font=(u'微软雅黑', 9))
        self.lbl_frm_condition_district.place(x=10, y=10, width=60, height=23)

        self.cmb_frm_condition_province.place(x=80, y=10, width=60, height=23)

        self.cmb_frm_condition_city.place(x=150, y=10, width=60, height=23)

        self.cmb_frm_condition_district.place(x=220, y=10, width=60, height=23)

        self.style.configure('lbl_frm_condition_birthday.TLabel', anchor='w', font=(u'微软雅黑', 9))
        self.lbl_frm_condition_birthday.place(x=10, y=50, width=60, height=23)

        self.cmb_frm_condition_year.place(x=80, y=50, width=50, height=23)

        self.cmb_frm_condition_month.place(x=140, y=50, width=40, height=23)

        self.cmb_frm_condition_day.place(x=190, y=50, width=40, height=23)

        self.style.configure('lbl_frm_condition_gender.TLabel', anchor='w', font=(u'微软雅黑', 9))
        self.lbl_frm_condition_gender.place(x=10, y=90, width=40, height=23)

        self.cmb_frm_condition_gender.place(x=80, y=90, width=40, height=23)

        self.style.configure('lbl_frm_condition_id.TLabel', anchor='w', font=(u'微软雅黑', 9))
        self.lbl_frm_condition_id.place(x=10, y=130, width=75, height=23)

        self.ety_frm_condition_id.place(x=90, y=130, width=140, height=23)

        self.style.configure('btn_frm_condition_generate.TButton', font=(u'微软雅黑', 9))
        self.btn_frm_condition_generate.place(x=10, y=170, width=60, height=25)

        # 解析身份证号码
        self.style.configure('frm_parse.TLabelframe', font=(u'微软雅黑', 9))
        self.frm_parse.place(x=5, y=241, height=200, width=485)

        self.style.configure('label_frm_parse_id.TLabel', anchor='w', font=(u'微软雅黑', 9))
        self.label_frm_parse_id.place(x=20, y=20, width=80, height=23)

        self.ety_frm_parse_id.place(x=100, y=20, width=140, height=23)

        self.style.configure('lbl_frm_parse_district.TLabel', anchor='w', font=(u'微软雅黑', 9))
        self.lbl_frm_parse_district.place(x=20, y=50, width=40, height=23)

        self.ety_frm_parse_district.place(x=100, y=50, width=140, height=23)

        self.style.configure('lbl_frm_parse_birthday.TLabel', anchor='w', font=(u'微软雅黑', 9))
        self.lbl_frm_parse_birthday.place(x=20, y=80, width=40, height=23)

        self.ety_frm_parse_birthday.place(x=100, y=80, width=140, height=23)

        self.style.configure('lbl_frm_parse_gender.TLabel', anchor='w', font=(u'微软雅黑', 9))
        self.lbl_frm_parse_gender.place(x=20, y=110, width=40, height=23)

        self.ety_frm_parse_gender.place(x=100, y=110, width=30, height=23)

        self.style.configure('btn_frm_parse_parse.TButton', font=(u'微软雅黑', 9))
        self.btn_frm_parse_parse.place(x=20, y=145, width=60, height=25)

        self.style.configure('btn_frm_parse_reset.TButton', font=(u'微软雅黑', 9))
        self.btn_frm_parse_reset.place(x=180, y=145, width=60, height=25)


class Application(ApplicationUI):
    # 这个类实现具体的事件处理回调函数。界面生成代码在ApplicationUI中。

    def __init__(self, master=None):
        ApplicationUI.__init__(self, master)

        # 定义变量
        self.ety_var_frm_auto_count = StringVar(value=1)
        self.ety_frm_auto_count['textvariable'] = self.ety_var_frm_auto_count
        # self.count = self.ety_var_frm_auto_count.get()

        self.txt_var_frm_auto_id = StringVar()

        self.ety_var_frm_parse_id = StringVar()
        self.ety_frm_parse_id['textvariable'] = self.ety_var_frm_parse_id

        self.ety_var_frm_parse_district = StringVar()
        self.ety_frm_parse_district['textvariable'] = self.ety_var_frm_parse_district

        self.ety_var_frm_parse_birthday = StringVar()
        self.ety_frm_parse_birthday['textvariable'] = self.ety_var_frm_parse_birthday

        self.ety_var_frm_parse_gender = StringVar()
        self.ety_frm_parse_gender['textvariable'] = self.ety_var_frm_parse_gender

        self.random_id = []

        # 绑定回调函数
        self.btn_frm_auto_generate['command'] = self.btn_frm_auto_generate_cmd
        self.btn_frm_condition_generate['command'] = self.btn_frm_condition_generate_cmd
        self.btn_frm_parse_parse['command'] = self.btn_frm_parse_parse_cmd
        self.btn_frm_parse_reset['command'] = self.btn_frm_parse_reset_cmd

        # 设置combox列表值
        self.cmblist_frm_condition_province = self.provinces
        self.cmb_frm_condition_province['values'] = self.cmblist_frm_condition_province
        self.cmb_frm_condition_province.set(self.cmblist_frm_condition_province[0])

        self.cmblist_frm_condition_city = self.cities
        self.cmb_frm_condition_city['values'] = self.cmblist_frm_condition_city
        self.cmb_frm_condition_city.set(self.cmblist_frm_condition_city[0])

        self.cmblist_frm_condition_district = self.districts
        self.cmb_frm_condition_district['values'] = self.cmblist_frm_condition_district
        self.cmb_frm_condition_district.set(self.cmblist_frm_condition_district[0])

        self.cmblist_frm_condition_year = self.years
        self.cmb_frm_condition_year['values'] = self.cmblist_frm_condition_year
        self.cmb_frm_condition_year.set(self.cmblist_frm_condition_year[0])

        self.cmblist_frm_condition_month = self.months
        self.cmb_frm_condition_month['values'] = self.cmblist_frm_condition_month
        self.cmb_frm_condition_month.set(self.cmblist_frm_condition_month[0])

        self.cmblist_frm_condition_day = self.days
        self.cmb_frm_condition_day['values'] = self.cmblist_frm_condition_day
        self.cmb_frm_condition_day.set(self.cmblist_frm_condition_day[0])

        self.cmblist_frm_condition_gender = ['男', '女']
        self.cmb_frm_condition_gender['values'] = self.cmblist_frm_condition_gender
        self.cmb_frm_condition_gender.set(self.cmblist_frm_condition_gender[0])

        self.ety_var_frm_condition_id = StringVar()
        self.ety_frm_condition_id['textvariable'] = self.ety_var_frm_condition_id

        # 绑定事件
        self.cmb_frm_condition_province.bind('<<ComboboxSelected>>', self.refresh_current_cities)
        self.cmb_frm_condition_city.bind('<<ComboboxSelected>>', self.refresh_current_districts)
        self.cmb_frm_condition_year.bind('<<ComboboxSelected>>', self.refresh_current_days)
        self.cmb_frm_condition_month.bind('<<ComboboxSelected>>', self.refresh_current_days)

    @property
    def provinces(self):
        all_provinces = []
        for i in range(0, len(list_prvoince)):
            all_provinces.append(list_prvoince[i]['name'])
        return all_provinces

    @property
    def cities(self):
        current_province_code = ''
        for i in range(0, len(list_prvoince)):
            if list_prvoince[i]['name'] == self.cmb_frm_condition_province.get().encode('utf-8'):
                current_province_code = list_prvoince[i]['code']

        current_cities = []
        for x in range(0, len(list_city)):
            if list_city[x]['code'][0:2] == current_province_code[0:2]:
                current_cities.append(list_city[x]['name'].decode('utf-8'))
        return current_cities

    @property
    def districts(self):
        current_city_code = ''
        current_city = self.cmb_frm_condition_city.get()
        for i in range(0, len(list_city)):
            if list_city[i]['name'] == current_city.encode('utf-8'):
                current_city_code = list_city[i]['code']
        print current_city_code

        current_districts = []

        for x in range(0, len(list_district)):
            if list_district[x]['code'][0:4] == current_city_code[0:4]:
                current_districts.append(list_district[x]['name'].decode('utf-8'))
        print current_districts
        return current_districts

    @property
    def years(self):
        years = []
        for i in range(datetime.now().year, 1900, -1):
            years.append(i)
        return years

    @property
    def months(self):
        months = []
        for i in range(1, 13):
            months.append(str(i).zfill(2))
        return months

    @property
    def days(self):
        days = []
        current_year = self.cmb_frm_condition_year.get()
        current_month = self.cmb_frm_condition_month.get()
        if (((int(current_year) % 4 == 0) and (int(current_year) % 100 != 0)) or (
                        int(current_year) % 400 == 0)) and current_month == '02':
            for i in range(1, 30):
                days.append(str(i).zfill(2))
        elif current_month == '02':
            for i in range(1, 29):
                days.append(str(i).zfill(2))
        elif current_month in ('01', '03', '05', '07', '08', '10', '12'):
            for i in range(1, 32):
                days.append(str(i).zfill(2))
        else:
            for i in range(1, 31):
                days.append(str(i).zfill(2))
        return days

    @staticmethod
    def generate_id(district_code=None, year=None, month=None, day=None, gender=None):
        # 身份证号=地区码(6位)+生日(8位)+顺序码(3位,末位代表性别:男奇女偶)+校验码(1)
        if district_code is None:
            district_code = list_district[random.randint(0, len(list_district) - 1)]['code']
        else:
            district_code = district_code

        today = datetime.now()

        if year is None:
            year = str(random.randint(1900, today.year))
        else:
            year = year
        if month is None:
            month = str(random.randint(1, 12)).zfill(2)
        else:
            month = month
        if day is None:
            if (((int(year) % 4 == 0) and (int(year) % 100 != 0)) or int(year) % 400 == 0) and int(month) == 2:
                day = str(random.randint(1, 28)).zfill(2)
            elif str(month) == 2:
                day = str(random.randint(1, 29)).zfill(2)
            elif month in ('01', '03', '05', '07', '08', '10', '12'):
                day = str(random.randint(1, 31)).zfill(2)
            else:
                day = str(random.randint(1, 30)).zfill(2)

        sequence_code = str(random.randint(1, 99)).zfill(2)

        if gender is None:
            gender = str(random.randint(0, 9))
        else:
            gender = gender

        id = ''.join([district_code, year, month, day, sequence_code, gender])

        count = 0
        # 前17位的权重项
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        # 校验码映射
        dict_check_code = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5',
                           '9': '3', '10': '2'}
        # 计算校验码
        for i in range(0, len(id)):
            count += int(id[i]) * weight[i]
        check_code = dict_check_code[str(count % 11)]
        id += check_code

        return id

    @staticmethod
    def parse_id(id):
        result = []
        list_district_code = []
        for district in list_district:
            list_district_code.append(district['code'])

        if len(id) == 18:
            if int(id[6:10]) % 4 == 0 or (int(id[6:10]) % 100 == 0 and int(id[6:10]) % 4 == 0):
                regex = re.compile('^(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]' +
                                   '|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))$')
            else:
                regex = re.compile('^(19[0-9]{2}|20[0-9]{2})((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]' +
                                   '|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))$')

            weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
            check_code = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']

            if id[0:6] in list_district_code:
                province, city, dist = None, None, None
                province_code = id[0:2] + '0000'
                city_code = id[0:4] + '00'
                district_code = id[0:6]
                for p in list_prvoince:
                    if province_code == p['code']:
                        province = p['name']
                for c in list_city:
                    if city_code == c['code']:
                        city = c['name']

                for d in list_district:
                    if district_code == d['code']:
                        dist = d['name']
                district = ''.join([province, city, dist])
                print district
                result.append(district)

                if re.match(regex, id[6:14]):
                    year = id[6:10]
                    month = id[10:12]
                    day = id[12:14]
                    birthday = year + '年' + month + '月' + day + '日'
                    print birthday
                    result.append(birthday)
                    sum = 0
                    for i in range(len(weight)):
                        sum += int(id[i]) * weight[i]
                    if id[17] == check_code[sum % 11]:
                        gender = '男' if int(id[16]) % 2 != 0 else '女'
                        print gender
                        result.append(gender)
                        return result
                    else:
                        showerror('错误提示', '身份证号码校验码校验失败！')
                        return None
                else:
                    showerror('错误提示', '身份证出生年月日不合法！')
                    return None
            else:
                showerror('错误提示', '身份证地区不合法！')
                return None
        else:
            showerror('错误提示', '身份证号码长度不合法！')
            return None

    @staticmethod
    def get_district_code(province, city, dist):
        province_code, city_code, dist_code = None, None, None
        for p in list_prvoince:
            if p['name'] == province.encode('utf-8'):
                province_code = p['code'][0:2]

        for c in list_city:
            if c['name'] == city.encode('utf-8'):
                city_code = c['code'][2:4]

        for d in list_district:
            if d['name'] == dist.encode('utf-8'):
                dist_code = d['code'][4:6]

        district_code = ''.join([province_code, city_code, dist_code])
        return district_code

    def generate_id_random(self):
        count = self.ety_var_frm_auto_count.get()
        if count.isdigit() and int(count) >= 1:
            for i in range(1, int(count) + 1):
                self.random_id.append(self.generate_id())
                print self.random_id
        else:
            showerror('错误提示', '身份证号码个数必须为正整数！')

    def generate_id_with_condition(self):
        current_province = self.cmb_frm_condition_province.get()
        current_city = self.cmb_frm_condition_city.get()
        current_district = self.cmb_frm_condition_district.get()
        district_code = self.get_district_code(current_province, current_city, current_district)
        print 'district code:', district_code

        current_year = self.cmb_frm_condition_year.get()
        current_month = self.cmb_frm_condition_month.get()
        current_day = self.cmb_frm_condition_day.get()
        current_gender = self.cmb_frm_condition_gender.get()

        if current_gender.encode('utf-8') == '男':
            # 列表中随机取一个数
            gender_code = random.sample(['1', '3', '5', '7', '9'], 1)
        else:
            gender_code = random.sample(['0', '2', '4', '6', '8'], 1)

        id = self.generate_id(district_code, current_year, current_month, current_day, gender_code[0])
        return id

    # 回调函数
    def btn_frm_auto_generate_cmd(self, event=None):
        self.generate_id_random()
        self.txt_frm_auto_id.delete(0.0, END)
        self.txt_frm_auto_id.insert(END, '\n'.join(self.random_id))
        self.random_id = []

    def btn_frm_condition_generate_cmd(self, event=None):
        self.ety_var_frm_condition_id.set(self.generate_id_with_condition())

    def btn_frm_parse_parse_cmd(self, event=None):
        result = self.parse_id(self.ety_var_frm_parse_id.get())
        if result is not None:
            self.ety_var_frm_parse_district.set(result[0])
            self.ety_var_frm_parse_birthday.set(result[1])
            self.ety_var_frm_parse_gender.set(result[2])

    def btn_frm_parse_reset_cmd(self, event=None):
        self.ety_var_frm_parse_id.set('')
        self.ety_var_frm_parse_district.set('')
        self.ety_var_frm_parse_birthday.set('')
        self.ety_var_frm_parse_gender.set('')

    def refresh_current_cities(self, event):
        cities = self.cities
        self.cmb_frm_condition_city['values'] = cities
        self.cmb_frm_condition_city.current(0)

    def refresh_current_days(self, event):
        days = []
        current_year = self.cmb_frm_condition_year.get()
        current_month = self.cmb_frm_condition_month.get()
        if (((int(current_year) % 4 == 0) and (int(current_year) % 100 != 0)) or (
                        int(current_year) % 400 == 0)) and current_month == '02':
            for i in range(1, 30):
                days.append(str(i).zfill(2))
        elif current_month == '02':
            for i in range(1, 29):
                days.append(str(i).zfill(2))
        elif current_month in ('01', '03', '05', '07', '08', '10', '12'):
            for i in range(1, 32):
                days.append(str(i).zfill(2))
        else:
            for i in range(1, 31):
                days.append(str(i).zfill(2))
        self.cmb_frm_condition_day['values'] = days
        self.cmb_frm_condition_day.current(0)

    def refresh_current_districts(self, event):
        self.cmb_frm_condition_district['values'] = self.districts
        self.cmb_frm_condition_district.current(0)


if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try:
        top.destroy()
    except:
        pass
