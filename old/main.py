#================================================== LIBRARIES ===========================================================
from PIL import Image, ImageFont, ImageDraw 
import textwrap
import requests
from io import BytesIO

#================================================== FUNCTIONS ===========================================================

#function to generate an effect monster
def monstercreate(myimage, atk, dff, level, attribute, race):

	response = requests.get('https://db.ygoprodeck.com/api/v7/randomcard.php')

	json_data = response.json() if response and response.status_code == 200 else None

	name = json_data['name']

	response = requests.get('https://db.ygoprodeck.com/api/v7/randomcard.php')

	json_data = response.json() if response and response.status_code == 200 else None

	text = json_data['desc']

	# fetching template
	image = Image.open("img/me_template.png")

	if(len(name)<20):
		title_font = ImageFont.truetype('fonts/Yu-Gi-Oh!1.ttf', 80)
	else:
		title_font = ImageFont.truetype('fonts/Yu-Gi-Oh!1.ttf', 60)

	if(len(text) < 300):
		effect_font = ImageFont.truetype('fonts/Yu-Gi-Oh!2.ttf', 25)
		width=58
	else:
		effect_font = ImageFont.truetype('fonts/Yu-Gi-Oh!2.ttf', 18)
		width=85

	title_text = name

	image_editable = ImageDraw.Draw(image)

	image_editable.text((72,69), title_text, (0, 0, 0), font=title_font)

	caption = text;



	wrapper = textwrap.TextWrapper(width) 
	word_list = wrapper.wrap(text=caption) 
	caption_new = ''
	for ii in word_list[:-1]:
		caption_new = caption_new + ii + '\n'
	caption_new += word_list[-1]

	margin = 70
	offset = 920
	image_editable.text((margin, offset), caption_new, font=effect_font, fill="#000000")

	#acquisizione
	back_im = image.copy()
	back_im.paste(myimage, (85, 215))
	back_im.save('result.jpg', quality=95)


#function to generate an effect monster
def spellcreate(myimage):

	response = requests.get('https://db.ygoprodeck.com/api/v7/randomcard.php')

	json_data = response.json() if response and response.status_code == 200 else None

	name = json_data['name']

	response = requests.get('https://db.ygoprodeck.com/api/v7/randomcard.php')

	json_data = response.json() if response and response.status_code == 200 else None

	text = json_data['desc']
	race = json_data['race']

	# fetching template
	image = Image.open("img/spell_template.png")

	if(len(name)<20):
		title_font = ImageFont.truetype('fonts/Yu-Gi-Oh!1.ttf', 80)
	else:
		title_font = ImageFont.truetype('fonts/Yu-Gi-Oh!1.ttf', 60)

	if(len(text) < 300):
		effect_font = ImageFont.truetype('fonts/Yu-Gi-Oh!2.ttf', 25)
		width=58
	else:
		effect_font = ImageFont.truetype('fonts/Yu-Gi-Oh!2.ttf', 18)
		width=85

	title_text = name

	image_editable = ImageDraw.Draw(image)

	image_editable.text((72,69), title_text, (0, 0, 0), font=title_font)

	caption = text;



	wrapper = textwrap.TextWrapper(width) 
	word_list = wrapper.wrap(text=caption) 
	caption_new = ''
	for ii in word_list[:-1]:
		caption_new = caption_new + ii + '\n'
	caption_new += word_list[-1]

	margin = 70
	offset = 900
	image_editable.text((margin, offset), caption_new, font=effect_font, fill="#000000")

	#acquisizione
	back_im = image.copy()
	back_im.paste(myimage, (85, 215))
	back_im.save('result.jpg', quality=95)


#function to generate an effect monster
def trapcreate(myimaget):

	response = requests.get('https://db.ygoprodeck.com/api/v7/randomcard.php')

	json_data = response.json() if response and response.status_code == 200 else None

	name = json_data['name']

	response = requests.get('https://db.ygoprodeck.com/api/v7/randomcard.php')

	json_data = response.json() if response and response.status_code == 200 else None
	
	text = json_data['desc']
	race = json_data['race']


	# fetching template
	image = Image.open("img/trap_template.png")

	if(len(name)<20):
		title_font = ImageFont.truetype('fonts/Yu-Gi-Oh!1.ttf', 80)
	else:
		title_font = ImageFont.truetype('fonts/Yu-Gi-Oh!1.ttf', 60)

	if(len(text) < 300):
		effect_font = ImageFont.truetype('fonts/Yu-Gi-Oh!2.ttf', 25)
		width=58
	else:
		effect_font = ImageFont.truetype('fonts/Yu-Gi-Oh!2.ttf', 18)
		width=85

	title_text = name

	image_editable = ImageDraw.Draw(image)

	image_editable.text((72,69), title_text, (0, 0, 0), font=title_font)

	caption = text;



	wrapper = textwrap.TextWrapper(width) 
	word_list = wrapper.wrap(text=caption) 
	caption_new = ''
	for ii in word_list[:-1]:
		caption_new = caption_new + ii + '\n'
	caption_new += word_list[-1]

	margin = 70
	offset = 900
	image_editable.text((margin, offset), caption_new, font=effect_font, fill="#000000")

	#acquisizione
	back_im = image.copy()
	back_im.paste(myimaget, (85, 215))
	back_im.save('result.jpg', quality=95)

#=======================================================================================================================
#============================================== MAIN ===================================================================

# getting random type from json
response = requests.get('https://db.ygoprodeck.com/api/v7/randomcard.php')

json_data = response.json() if response and response.status_code == 200 else None

type = json_data['type']
linkImg = json_data['id']
linkImg = str(linkImg)

# getting parameters
response2 = requests.get("https://images.ygoprodeck.com/images/cards_cropped/"+linkImg+".jpg")
my_image = Image.open(BytesIO(response2.content))


if type == "Spell Card":
	spellcreate(my_image)
elif type == "Trap Card":
	trapcreate(my_image)
else:
	atk = json_data['atk']
	dff = json_data['def']
	level = json_data['level']
	attribute = json_data['attribute']
	race = json_data['race']
	monstercreate(my_image, atk, dff, level, attribute, race)
