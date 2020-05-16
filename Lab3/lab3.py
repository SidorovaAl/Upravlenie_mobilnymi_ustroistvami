from fpdf import FPDF
from datetime import datetime
from num2words import num2words
import time

def layout(Num, CustName, CustINN, CustAddress, amlabel, pricelabel):
	pdf = FPDF()
	pdf.add_page()
	pdf.add_font('Times', '', r"c:\WINDOWS\Fonts\times.ttf", uni=True)
	pdf.add_font('Times', 'b', r"c:\WINDOWS\Fonts\timesbd.ttf", uni=True)
	pdf.set_font('Times')
	pdf.set_font_size(12)
	
	CompINN = '784012345663'
	CompKPP = '784044123'
	BankName = 'ПАО «Банк «Санкт-Петербург»'
	CompName = 'ООО «Консенсус»'
	CompAddress = 'г.Выдрополь, б-в.Сказочный, д.13, корп.Г, оф.7'
	BIK = '047800123'
	KorS4 = '31001000000000000123'
	RasS4 = '40717810178781234567'
	
	ordstart = pdf.get_y()
	pdf.set_font_size(10)
	pdf.cell(120,7, 'Банк получателя', 0,1,'L')
	pdf.set_font_size(12)
	pdf.multi_cell(120, 5, BankName, 0,'L')
	ord = pdf.get_y()
	height = ord - ordstart
	if (height < 20):
		height = 20
	pdf.rect(10,10,120,height)
	ord = ordstart + height
	pdf.set_y(ord)
	pdf.cell(60,5, 'ИНН  '+ CompINN, 1,0,'L')
	pdf.cell(60,5, 'КПП  '+ CompKPP, 1,1,'L')
	pdf.set_font_size(10)
	pdf.cell(120,7, 'Получатель', 0,1,'L')
	pdf.set_font_size(12)
	pdf.multi_cell(120,5, CompName, 0,'L')
	ordend = pdf.get_y()
	height = ordend - ord
	if (height < 20):
		height = 20
	pdf.rect(10,ord+5,120,height)
	pdf.set_y(ord+height)

	pdf.rect(130,ordstart,20,7)
	pdf.text(131,ordstart+5,'БИК')
	pdf.rect(130,ordstart+7,20,ord-ordstart-7)
	pdf.text(131,ordstart+15,'Сч №')
	pdf.rect(130,ord,20,height+5)
	pdf.text(131,ord+5,'Сч №')
	
	pdf.rect(150,ordstart,50,ord-ordstart)
	pdf.text(151,ordstart+5,BIK)
	pdf.text(151,ordstart+15,KorS4)
	pdf.rect(150,ord,50,height+5)
	pdf.text(151,ord+5,RasS4)
	pdf.ln(+10)

	pdf.set_font('Times', 'B', 16)
	pdf.cell(190, 15,'Счет № '+ Num.__str__() +' от '+ datetime.today().strftime('%d.%m.%Y'),0,1,'C')
	pdf.ln(+5)
	
	pdf.set_font('Times', '', 12)
	pdf.cell(20,5, 'Поставщик: ', 0,0,'L')
	ord = pdf.get_y()
	pdf.set_font('Times', 'B')
	pdf.set_left_margin(35)
	pdf.set_y(ord)
	pdf.write(5, CompName + ', ИНН '+ CompINN + ', КПП' + CompKPP + ', ' + CompAddress)
	pdf.ln(+10)
	
	pdf.set_left_margin(10)
	pdf.set_x(10)
	
	pdf.set_font('Times', '', 12)
	pdf.cell(20,5, 'Покупатель: ', 0,0,'L')
	ord = pdf.get_y()
	pdf.set_font('Times', 'B')
	pdf.set_left_margin(35)
	pdf.set_x(35)
	pdf.set_y(ord)
	pdf.write(5, CustName + ', ИНН '+ CustINN + ', ' + CustAddress)
	
	pdf.set_left_margin(10)	
	pdf.set_x(10)

	pdf.ln(+15)
	abs = pdf.get_x()
	ord = pdf.get_y()
	pricesum = 0
	namelabel = ['Входящие звонки', 'Исходящие звонки', 'СМС', 'Интернет']
	edlabel = ['мин', 'мин', 'шт', 'Мб']

	pdf.set_font('Times', 'B')
	pdf.cell(10,10, '№', 1,0,'C')
	pdf.cell(90,10, 'Товары (работы, услуги)', 1,0,'C')
	pdf.cell(20,10, 'Единица', 1,0,'C')
	pdf.cell(20,10, 'Кол-во', 1,0,'C')
	pdf.cell(20,10, 'Цена', 1,0,'C')
	pdf.cell(30,10, 'Сумма', 1,1,'C')

	pdf.set_font('Times', '')
	for x in range(1,5):
		pdf.cell(10,10, ' '+x.__str__(), 1,0,'C')
		pdf.cell(90,10, ' '+namelabel[x-1], 1,0,'L')
		pdf.cell(20,10, edlabel[x-1], 1,0,'C')
		pdf.cell(20,10, amlabel[x-1].__str__()+' ', 1,0,'R')
		pdf.cell(20,10, pricelabel[x-1].__str__()+' ', 1,0,'R')
		pdf.cell(30,10, (amlabel[x-1]*pricelabel[x-1]).__str__()+' ', 1,1,'R')
		pricesum += amlabel[x-1]*pricelabel[x-1]

	pdf.set_font('Times', 'B')
	pdf.cell(160,10, 'Итого: ', 0,0,'R')
	pdf.cell(30,10, pricesum.__str__(), 1,1,'R')
	pdf.cell(160,10, 'В том числе НДС (20%): ', 0,0,'R')
	pdf.cell(30,10, (pricesum*0.2).__str__(), 1,1,'R')	
	pdf.cell(160,10, 'Всего к оплате: ', 0,0,'R')
	pdf.cell(30,10, pricesum.__str__(), 1,1,'R')

	pdf.set_line_width(0.4)
	pdf.rect(abs, ord, 190, 10)
	pdf.set_line_width(0.6)
	pdf.rect(abs, ord, 190, 50)
	
	pdf.set_font('Times', '')
	pdf.set_y(-70)
	pdf.write(5,'Всего наименований 4 на сумму ' + pricesum.__str__() + ' рублей.')
	pdf.ln(+5)
	pdf.set_font('Times', 'B')
	pdf.write(5, num2words(int(pricesum), lang='ru').capitalize() + ' рублей ' + num2words(int(pricesum%1),lang='ru') + ' копеек.')

	pdf.set_line_width(0.6)
	pdf.set_y(-50)
	ord = pdf.get_y()
	pdf.line(10,ord,200,ord)
	
	pdf.set_font('Times', '')
	pdf.set_line_width(0.2)
	pdf.set_y(-45)
	pdf.cell(10,10)
	pdf.cell(55,10, 'Руководитель предприятия')
	pdf.cell(50,7, '', 'B',0)
	pdf.cell(35,10, '/Колобок И.Ю./',0,1,'R')
	
	pdf.set_y(-33)
	pdf.cell(10,10)
	pdf.cell(40,10, 'Главный бухгалтер')
	pdf.cell(50,7, '', 'B',0)
	pdf.cell(30,10, '/Лисина А.В./',0,1,'R')
		
	pdf.output("Internet_oplata.pdf")


layout(
	Num = 1,
	CustName = 'ИП Зеленоглазый',
	CustINN = '784044444400',
	CustAddress = 'г.Выдрополь, ул.Камышовая, д.200, оф.154',
	amlabel = [10, 92, 57, 177],
	pricelabel = [1.00, 3.00, 1.00, 1.00])