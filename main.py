#================================================== LIBRARIES ===========================================================
from PIL import Image, ImageFont, ImageDraw 
import textwrap
import json

#================================================== FUNCTIONS ===========================================================

#function to generate an effect monster
def monstercreate(myimage, name, text):

	# fetching template
	image = Image.open("img/me_template.png")

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
	back_im.paste(myimage, (100, 220))
	back_im.save('result.jpg', quality=95)


#function to generate an effect monster
def spellcreate(myimage, name, text):

	# fetching template
	image = Image.open("img/spell_template.png")

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
	back_im.paste(myimage, (100, 220))
	back_im.save('result.jpg', quality=95)


#function to generate an effect monster
def trapcreate(myimage, name, text):

	# fetching template
	image = Image.open("img/trap_template.png")

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
	back_im.paste(myimage, (100, 220))
	back_im.save('result.jpg', quality=95)

#=======================================================================================================================
#============================================== MAIN ===================================================================

# getting parameters
my_image = Image.open("img/skystriker.png")

name = "Blue-Eyes Black Magician"

text = "You can only Special Summon once per turn. When this card declares an attack: You can place 1 Spell Counter on it. Once per opponent's turn (Quick Effect): You can remove 3 Spell Counters from your field; Special Summon 1 monster from your Deck that you can place a Spell Counter on. If this card in the Monster Zone is destroyed: You can place this card in your Pendulum Zone, then place the same number of Spell Counters on it that it had as a monster."

attribute = "spell"

if attribute == "spell":
	spellcreate(my_image, name, text)
elif attribute == "trap":
	trapcreate(my_image, name, text)
else:
	monstercreate(my_image, name, text)
