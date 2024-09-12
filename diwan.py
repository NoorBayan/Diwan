####
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from bidi.algorithm import get_display
import arabic_reshaper
poems=pd.read_csv('corpus/Diwan.csv',sep='\t',encoding='utf-16')
def arab(text):
    return get_display(arabic_reshaper.reshape(text))


poem_art_type_dic={'_': 0, 'قديمة': 1, 'حديثة': 2}
poem_art_type={poem_art_type_dic[i]:i for i in poem_art_type_dic}
####
poem_art_dic={'_': 0,
             'قريض': 1,
             'موشح': 2,
             'دوبيت': 3,
             'الكان كان': 4,
             'مواليا': 5,
             'سلسلة': 6,
             'زجل': 7,
             'حر': 8,
             'نثر': 9,
             'موضوعي': 10,
             'ترجمات': 11}
poem_art={poem_art_dic[i]:i for i in poem_art_dic}
####
lang_type_dic={'_': 0, 'فصحى': 1, 'عامية': 2}
lang_type={lang_type_dic[i]:i for i in lang_type_dic}
####
writing_style_dic={'_': 0, 'عموديه': 1, 'غير عموديه': 2}
writing_style={writing_style_dic[i]:i for i in writing_style_dic}
####
meter_system_dic={'_': 0,
                 'الفراهيدي': 1,
                 'مستعارة': 2,
                 'شعبي': 3,
                 'تفعيلات': 4,
                 'لا يوجد': 5}
meter_system={meter_system_dic[i]:i for i in meter_system_dic}
####
supermeter_dic={'_': 0,
                 'الطويل': 1,
                 'المديد': 2,
                 'البسيط': 3,
                 'الوافر': 4,
                 'الكامل': 5,
                 'الهزج': 6,
                 'الرجز': 7,
                 'الرمل': 8,
                 'السريع': 9,
                 'المنسرح': 10,
                 'الخفيف': 11,
                 'المضارع': 12,
                 'المقتضب': 13,
                 'المجتث': 14,
                 'المتقارب': 15,
                 'المتدارك': 16,
                 'الدوبيت': 17,
                 'السلسلة': 18,
                 'القوما': 19,
                 'الموشح': 20,
                 'الزجل': 21,
                 'الكان كان': 22,
                 'المواليا': 23,
                 'الهجيني': 24,
                 'المسحوب': 25,
                 'الخبب': 26,
                 'اللويحاني': 27,
                 'الحداء': 28,
                 'الصخري': 29,
                 'تفعيلات': 30,
                 'لا يوجد': 31}
supermeter={supermeter_dic[i]:i for i in supermeter_dic}
####
submeter_dic={'_': 0,
             'تام': 1,
             'مجزوء': 2,
             'مشطور': 3,
             'منهوك': 4,
             'أحذ': 5,
             'مقطوع': 6,
             'مخلع': 7,
             'مربع': 8,
             'تفعيلات': 9,
             'لا يوجد': 10}
submeter={submeter_dic[i]:i for i in submeter_dic}
####
topics_dic={'_': 0,
             'متعددة': 1,
             'غزل': 2,
             'رثاء': 3,
             'حكمة': 4,
             'عدل': 5,
             'صبر': 6,
             'هجاء': 7,
             'مدح': 8,
             'انشاد': 9,
             'عتاب': 10,
             'فراق': 11,
             'ابتهال': 12,
             'نصيحة': 13,
             'دينية': 14,
             'اعتذار': 15,
             'حزينة': 16,
             'جود': 17,
             'شوق': 18,
             'رحمة': 19,
             'سياسة': 20,
             'وطنية': 21}
topics={topics_dic[i]:i for i in topics_dic}
####
Gender={0:'غير مصنف',
       1:'شاعر',
       2:'شاعرة'}
####
location_type_dic={'_': 0, 'عربي': 1, 'أجنبي': 2}
location_type={location_type_dic[i]:i for i in location_type_dic}
####
rhyme_dic={'_': 0,
         'ء': 1,
         'أ': 2,
         'ؤ': 3,
         'إ': 4,
         'ئ': 5,
         'ا': 6,
         'ب': 7,
         'ة': 8,
         'ت': 9,
         'ث': 10,
         'ج': 11,
         'ح': 12,
         'خ': 13,
         'د': 14,
         'ذ': 15,
         'ر': 16,
         'ز': 17,
         'س': 18,
         'ش': 19,
         'ص': 20,
         'ض': 21,
         'ط': 22,
         'ظ': 23,
         'ع': 24,
         'غ': 25,
         'ف': 26,
         'ق': 27,
         'ك': 28,
         'ل': 29,
         'م': 30,
         'ن': 31,
         'ه': 32,
         'و': 33,
         'ى': 34,
         'ي': 35}
rhyme={rhyme_dic[i]:i for i in rhyme_dic}
####
poet_location_dic={'_': 0,
                 'الإمارات': 1,
                 'الأردن': 2,
                 'البحرين': 3,
                 'الجزائر': 4,
                 'السعودية': 5,
                 'السودان': 6,
                 'الصومال': 7,
                 'العراق': 8,
                 'الكويت': 9,
                 'المغرب': 10,
                 'اليمن': 11,
                 'إريتريا': 12,
                 'تونس': 13,
                 'سورية': 14,
                 'عمان': 15,
                 'فلسطين': 16,
                 'قطر': 17,
                 'لبنان': 18,
                 'ليبيا': 19,
                 'مصر': 20,
                 'موريتانيا': 21,
                 'الارض الخضراء': 22,
                 'غير عربية': 23,
                 'الأرجنتين': 24,
                 'البرازيل': 25,
                 'البرتغال': 26,
                 'البوسنة والهرسك': 27,
                 'الدنمارك': 28,
                 'السنغال': 29,
                 'السويد': 30,
                 'الصين': 31,
                 'الفلبين': 32,
                 'المكسيك': 33,
                 'المملكة المتحدة': 34,
                 'النرويج': 35,
                 'النمسا': 36,
                 'الهند': 37,
                 'الولايات المتحدة الأمريكية': 38,
                 'اليابان': 39,
                 'اليونان': 40,
                 'إسبانيا': 41,
                 'إستونيا': 42,
                 'إقليم المحيط البريطاني الهندي': 43,
                 'إندونيسيا': 44,
                 'إيران': 45,
                 'إيطاليا': 46,
                 'أثيوبيا': 47,
                 'أخرى': 48,
                 'أذربيجان': 49,
                 'أرمينيا': 50,
                 'أستراليا': 51,
                 'أفغانستان': 52,
                 'ألبانيا': 53,
                 'ألمانيا': 54,
                 'أنغولا': 55,
                 'أوروغواي': 56,
                 'أوغندا': 57,
                 'أوكرانيا': 58,
                 'أيرلندا': 59,
                 'أيسلندا': 60,
                 'بابوا غينيا الجديدة': 61,
                 'باكستان': 62,
                 'بلجيكا': 63,
                 'بوركينا فاسو': 64,
                 'بولندا': 65,
                 'بوليفيا': 66,
                 'بيرو': 67,
                 'تايلاند': 68,
                 'تايوان': 69,
                 'تركيا': 70,
                 'تشاد': 71,
                 'تشيلي': 72,
                 'تنزانيا': 73,
                 'جمهورية التشيك': 74,
                 'جمهورية الدومنيكان': 75,
                 'جنوب أفريقيا': 76,
                 'روسيا': 77,
                 'رومانيا': 78,
                 'زامبيا': 79,
                 'زمبابوي': 80,
                 'سانت لوسيا': 81,
                 'سلوفاكيا': 82,
                 'سنغافورة': 83,
                 'سويسرا': 84,
                 'سيريلانكا': 85,
                 'صربيا': 86,
                 'طاجيكستان': 87,
                 'غامبي': 88,
                 'غينيا': 89,
                 'فانواتو': 90,
                 'فرنسا': 91,
                 'فنلندا': 92,
                 'فيتنام': 93,
                 'كرواتيا (هرفاتسكا)': 94,
                 'كندا': 95,
                 'كوبا': 96,
                 'كوريا الشمالية': 97,
                 'كوستا ريكا': 98,
                 'كولومبيا': 99,
                 'كينيا': 100,
                 'لاوس': 101,
                 'ليتوانيا': 102,
                 'مالاوي': 103,
                 'مالي': 104,
                 'ماليزيا': 105,
                 'مدغشقر': 106,
                 'موريشيوس': 107,
                 'ناميبيا': 108,
                 'نيبال': 109,
                 'نيجيريا': 110,
                 'نيكاراغوا': 111,
                 'نيوزيلاندا': 112,
                 'هايتي': 113,
                 'هنغاريا': 114,
                 'هولندا': 115}
poet_location={poet_location_dic[i]:i for i in poet_location_dic}
####
poet_era_dic={'_': 0,
             'العصر الجاهلي': 1,
             'العصر الإسلامي': 2,
             'المخضرمين': 3,
             'العصر الأموي': 4,
             'العصر العباسي': 5,
             'العصر الأندلسي': 6,
             'عصر ما بين الدولتين': 7,
             'العصر الأيوبي': 8,
             'العصر المملوكي': 9,
             'العصر الفاطمي': 10,
             'العصر العثماني': 11,
             'العصر الحديث': 12}
poet_era={poet_era_dic[i]:i for i in poet_era_dic}
####

report={0: ['poem_art_type','أنواع الفنون الشعرية',poem_art_type],
         1: ['poem_art','الفنون الشعرية',poem_art],
         2: ['lang_type','اللغة المستخدمة',lang_type],
         3: ['writing_style','نمط الكتابة',writing_style],
         4: ['meter_system','نظام العروض',meter_system],
         5: ['supermeter','البحر الرئيسي',supermeter],
         6: ['submeter','البحر الفرعي',submeter],
         7: ['topics','موضوع القصيدة',topics],
         8: ['Gender','جنس الشاعر',Gender],
         9: ['poet_era','عصر الشعر',poet_era],
         10: ['location_type','جنسية الشاعر',location_type],
         11: ['poet_location','موطن الشاعر',poet_location],
         12: ['rhyme','قوافي القصائد',rhyme],}


def get_not_class_report(report,title):
    sizes  =[len(poems[poems[report]!=0]),len(poems[poems[report]==0])]
    labels =[arab(i) for i in ['مصنف','غير مصنف']]
    fig, ax = plt.subplots(figsize= (5,5), dpi = 100)
    explode = (0.1,0)
    ax.pie(sizes, labels = labels, autopct = '%1.1f%%', shadow = True,
          startangle = 90, explode = explode)
    plt.title(arab(title), bbox={'facecolor':'1', 'pad':5})
    return plt.show()

def get_pie_report(report,title,label):
    r=poems[poems[report]!=0].groupby(report).size().to_frame('size').reset_index( ).sort_values("size", ascending=[False])
    if len(r) <= 4:
        sizes = r['size']
        labels = [arab(label[i]) for i in r[report]]
        fig, ax = plt.subplots(figsize= (5,5), dpi = 100)
        explode = (0.1,0)
        ax.pie(sizes, labels = labels, autopct = '%1.1f%%', shadow = True,
              startangle = 90, explode = explode)
        plt.title(arab(title), bbox={'facecolor':'1', 'pad':5})
    return plt.show()

def get_bar_report(report,title,label):
    r=poems[poems[report]!=0].groupby(report).size().to_frame('size').reset_index( ).sort_values("size", ascending=[False])
    if report in ['poem_art_type','lang_type','writing_style','location_type','Gender']:
        aspect=.5
    else:
        aspect=3    
          
    r[report]=[arab(label[i]) for i in r[report]]

    fig=sns.catplot(x = report, y = 'size', kind = 'bar', data = r,height=6, aspect=aspect,palette='ch:1.25')\
    .set(title=arab(title))
    ax = fig.facet_axis(0,0)
    for p in ax.patches:
        ax.text(p.get_x() - 0.01, 
                p.get_height() * 1.02, 
               '{0:.1f}'.format(p.get_height()),   #Used to format it K representation
                color='black', 
                rotation='horizontal', 
                size='large')
    return fig
