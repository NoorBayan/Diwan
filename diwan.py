####
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from bidi.algorithm import get_display
import arabic_reshaper
poems=pd.read_csv('corpus/Diwan.csv',sep='\t',encoding='utf-16')
def arab(text):
    return get_display(arabic_reshaper.reshape(text))


poem_form_dic={'_': 0, 'قديمة': 1, 'حديثة': 2}
poem_form={poem_form_dic[i]:i for i in poem_form_dic}
####
poem_genre_dic={'_': 0,
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
poem_genre={poem_genre_dic[i]:i for i in poem_genre_dic}
####
language_type_dic={'_': 0, 'فصحى': 1, 'عامية': 2}
language_type={language_type_dic[i]:i for i in language_type_dic}
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
main_meter_dic={'_': 0,
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
main_meter={main_meter_dic[i]:i for i in main_meter_dic}
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
them_dic={'_': 0,
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
them={them_dic[i]:i for i in them_dic}
####
poet_gender={0:'غير مصنف',
               1:'شاعر',
               2:'شاعرة'}
####
nationality_dic={'_': 0, 'عربي': 1, 'أجنبي': 2}
nationality={nationality_dic[i]:i for i in nationality_dic}
####
rhyme_dic={'_': 0,
         'ء': 1,
         'ا': 2,
         'ال': 3,
         'إ': 4,
         'أ': 5,
         'ب': 6,
         'ة': 7,
         'ت': 8,
         'ث': 9,
         'ج': 10,
         'ح': 11,
         'خ': 12,
         'د': 13,
         'ذ': 14,
         'ر': 15,
         'ز': 16,
         'س': 17,
         'ش': 18,
         'ص': 19,
         'ض': 20,
         'ط': 21,
         'ظ': 22,
         'ع': 23,
         'غ': 24,
         'ف': 25,
         'ق': 26,
         'ك': 27,
         'ل': 28,
         'لا': 29,
         'م': 30,
         'ن': 31,
         'ه': 32,
         'و': 33,
         'ؤ': 34,
         'ى': 35,
         'ي': 36,
         'ئ': 37}
rhyme={rhyme_dic[i]:i for i in rhyme_dic}
####
poet_country_dic={'_': 0,
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
poet_country={poet_country_dic[i]:i for i in poet_country_dic}
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

report={0: ['poem_form','أنواع الفنون الشعرية',poem_form],
         1: ['poem_genre','الفنون الشعرية',poem_genre],
         2: ['language_type','اللغة المستخدمة',language_type],
         3: ['writing_style','نمط الكتابة',writing_style],
         4: ['meter_system','نظام العروض',meter_system],
         5: ['main_meter','البحر الرئيسي',main_meter],
         6: ['submeter','البحر الفرعي',submeter],
         7: ['them','موضوع القصيدة',them],
         8: ['poet_gender','جنس الشاعر',poet_gender],
         9: ['poet_era','عصر الشعر',poet_era],
         10: ['nationality','جنسية الشاعر',nationality],
         11: ['poet_country','موطن الشاعر',poet_country],
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
    if report in ['poem_form','language_type','writing_style','nationality','poet_gender']:
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

style1="""<!DOCTYPE html>
<html lang="ar">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        .container {
            width: 1200px;
            /* عرض الحاوية */
            margin: 0 auto;
            /* توسيط الحاوية */
        }

        .ayat-container {
          flex: 1;
          width: 100%;
          overflow: auto;
          /* إمكانية التمرير إذا كان الجدول كبيرًا */
        }
        
        .table-container {
          flex: 1;
          width: 90%;
          overflow: auto;
          /* إمكانية التمرير إذا كان الجدول كبيرًا */
        }

        table {
          width: 100%;
          border-collapse: collapse;
        }

        th,
        td {
          border: 1px solid #ccc;
          padding: 8px;
          text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
    """

style2="""                  <style>                      
                    .paragraph-style {
                      direction: rtl; /* اتجاه النص من اليمين إلى اليسار */
                      margin-top: 0in; /* هامش أعلى */
                      margin-right: 0.2in; /* هامش يمين */
                      margin-bottom: 0.05in; /* هامش أسفل */
                      margin-left: 0in; /* هامش يسار */
                      text-align: justify; /* محاذاة النص */
                      line-height: normal; /* ارتفاع السطر */
                      color: black; /* Font color */
                      font-family: 'Traditional Arabic', serif; /* Traditional Arabic font */
                    }
                
                      
                    .paragraph-ayah-tfsir {
                      direction: rtl; /* اتجاه النص من اليمين إلى اليسار */
                      margin-top: 0.5in; /* هامش أعلى */
                      margin-right: 0in; /* هامش يمين */
                      margin-bottom: 0.2in; /* هامش أسفل */
                      margin-left: 0in; /* هامش يسار */
                      text-align: center; /* توسيط النص */
                      line-height: normal; /* ارتفاع السطر */
                      color: blue; /* Font color */
                      font-family: 'Traditional Arabic', serif; /* Traditional Arabic font */
                      font-size: 22px; /* Font size */
                      font-weight: bold; /* جعل الخط غامقًا */
                    }

                    .paragraph-th {
                      direction: rtl; /* اتجاه النص من اليمين إلى اليسار */
                      margin-top: 0in; /* هامش أعلى */
                      margin-right: 0in; /* هامش يمين */
                      margin-bottom: 0in; /* هامش أسفل */
                      margin-left: 0in; /* هامش يسار */
                      text-align: start; /* توسيط النص */
                      line-height: normal; /* ارتفاع السطر */
                      color: blue; /* Font color */
                      font-family: 'Traditional Arabic', serif; /* Traditional Arabic font */
                      font-size: 20px; /* Font size */
                      font-weight: bold; /* جعل الخط غامقًا */
                    }

                    .paragraph-style {
                      direction: rtl; /* اتجاه النص من اليمين إلى اليسار */
                      margin-top: 0in; /* هامش أعلى */
                      margin-right: 0in; /* هامش يمين */
                      margin-bottom: 0in; /* هامش أسفل */
                      margin-left: 0in; /* هامش يسار */
                      text-align: center; /* توسيط النص */
                      line-height: normal; /* ارتفاع السطر */
                      color: green; /* Font color */
                      font-family: 'hafs', hafs-qc; /* Traditional Arabic font */
                      font-size: 28px; /* Font size */
                      font-weight: bold; /* جعل الخط غامقًا */
                      
                    }
                    
                    .paragraph-style [font-family="hafs"] {
                          font-family: 'hafs-qc'
                      }

                    
                    @font-face {
                          font-family: 'hafs-qc';
                          src: url('https://fonts.nuqayah.com/hafs-qc.woff2');
                    }
                    
                    .word-style-class {
                      color: black; /* Font color */
                      font-family: 'Aldhabi', 'Traditional Arabic', serif; /* Traditional Arabic font */
                      font-size: 30px; /* Font size */
                      font-weight: bold; /* جعل الخط غامقًا */
                    }
                    
                    .td-cell-style {
                      width: 250px; /* عرض الخلية */
                      border-top: none; /* إزالة الحدود العلوية */
                      border-right: none; /* إزالة الحدود اليمنى */
                      border-left: none; /* إزالة الحدود اليسرى */
                      border-image: initial; /* تعيين صورة الحدود */
                      border-bottom: 1pt solid rgb(127, 127, 127); /* حدود سفلية صلبة بلون رمادي */
                      padding: 0in 5.4pt; /* حشو الخلية */
                      vertical-align: middle; /* محاذاة عمودية أعلى */
                    } 
                    
                    .td2-cell-style {
                      width: 850px; /* عرض الخلية */
                      border-bottom: 1pt solid rgb(127, 127, 127); /* حدود سفلية صلبة بلون رمادي */
                      vertical-align: top; /* محاذاة عمودية أعلى */
                    }
                    
                    h3 {
                      color: #2222ff; /* تغيير لون الخط */
                      font-weight: bold; /* جعل الخط غامقًا */
                      font-family: 'Traditional Arabic', serif; /* Traditional Arabic font */
                    }

                    h4 {
                      color: #2222ff; /* تغيير لون الخط */
                      font-weight: bold; /* جعل الخط غامقًا */
                      text-align: start; /* محاذاة النص في البداية */
                      margin-bottom: 8px; /* إضافة هامش أسفل التاج */
                      font-family: 'Traditional Arabic', serif; /* Traditional Arabic font */
                    }
                    
                    table thead {
                      font-family: 'Traditional Arabic', serif; /* Traditional Arabic font */
                      font-size: 20px; /* Font size */
                      font-weight: bold; /* جعل الخط غامقًا */
                      border: none;
                      color: blue; /* Font color */
                    }
                    
                    table thead th {
                      border: none; /* إخفاء جميع حدود خلايا الترويسة */
                      border-bottom: 2px solid #ddd; /* حد سفلي رمادي فاتح بسمك 2 بكسل */
                    }

                    
                </style>
    </div>
</body>
</html>
"""
#                      background-color: #007bff; /* أزرق كهربائي */


TABLE="""    <div class="table-container">
        <table dir="rtl">
            <tbody>
              {table}
            </tbody>
          </table>
    </div>"""
TR="""          <tr>
                {info}
              </tr>"""
TD="""         <td class="td-cell-style">
                    {para}
                </td>"""
PARA="""                  <p dir="RTL" class="paragraph-style">
                    {spans}
                  </p>"""
SPAN="""                <span class="word-style-class" style="color: {};">{}</span>"""

POEM = """
        <div class="main-poem">
        {content}
        </div>"""
