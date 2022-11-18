#================================================== LIBRARIES ===========================================================
from PIL import Image, ImageFont, ImageDraw 
import textwrap
import requests
from io import BytesIO

#================================================== CLASSES ===========================================================
class Card:

    # Attributes
    type = ''
    name = ''
    text = ''
    atf = ''
    dff = ''
    level = ''
    attribute = ''
    race = ''

    def randomSeed(self):

        response = requests.get('https://db.ygoprodeck.com/api/v7/randomcard.php')

        json_data = response.json() if response and response.status_code == 200 else None

        return json_data

    def getType(self):

        json_data = self.randomSeed()

        # getting random type from json
        return json_data['type']

    def getName(self):

        json_data = self.randomSeed()

        return json_data['name']

    def getDesc(self):

        json_data = self.randomSeed()

        return json_data['desc']

    def getAtk(self):

        json_data = self.randomSeed()

        return json_data['atk']	

    def getDef(self):

        json_data = self.randomSeed()

        return json_data['def']
    
    def getAttribute(self):

        json_data = self.randomSeed()

        return json_data['attribute']

    def getLevel(self):

        json_data = self.randomSeed()

        return json_data['level']

    def getRace(self):

        json_data = self.randomSeed()

        return json_data['race']

    def getImage(self):

        json_data = self.randomSeed()

        linkImg = json_data['id']
        linkImg = str(linkImg)

        # getting parameters
        response2 = requests.get("https://images.ygoprodeck.com/images/cards_cropped/"+linkImg+".jpg")
        my_image = Image.open(BytesIO(response2.content))

        return my_image

    def __init__(self):  
        self.type = self.getType()

    def printCard(self, image, myimage):

        img_resized = myimage.resize((582, 585), Image.Resampling.LANCZOS)

        #acquisizione
        back_im = image.copy()
        back_im.paste(img_resized, (115, 244))
        back_im.save('result.jpg', quality=95)

    # Method
    def monsterGen(self):

        myimage = self.getImage()
        
        caption = self.getDesc()

        title_text = self.getName()

        # fetching template
        image = Image.open("img/me_template.png")

        if(len(title_text)<20):
            title_font = ImageFont.truetype('fonts/Yu-Gi-Oh!1.ttf', 80)
        else:
            title_font = ImageFont.truetype('fonts/Yu-Gi-Oh!1.ttf', 55)

        if(len(caption) < 400):
            effect_font = ImageFont.truetype('fonts/Yu-Gi-Oh!2.ttf', 25)
            width=58
        else:
            effect_font = ImageFont.truetype('fonts/Yu-Gi-Oh!2.ttf', 15)
            width=85
    
        image_editable = ImageDraw.Draw(image)

        image_editable.text((72,69), title_text, (0, 0, 0), font=title_font)

        wrapper = textwrap.TextWrapper(width) 
        word_list = wrapper.wrap(text=caption) 
        caption_new = ''
        for ii in word_list[:-1]:
            caption_new = caption_new + ii + '\n'
        caption_new += word_list[-1]

        margin = 70
        offset = 920
        image_editable.text((margin, offset), caption_new, font=effect_font, fill="#000000")

        self.printCard(image, myimage)

    def spellGen(self):

        myimage = self.getImage()

        title_text = self.getName()

        caption = self.getDesc()

        # fetching template
        image = Image.open("img/spell_template.png")

        if(len(title_text)<20):
            title_font = ImageFont.truetype('fonts/Yu-Gi-Oh!1.ttf', 80)
        else:
            title_font = ImageFont.truetype('fonts/Yu-Gi-Oh!1.ttf', 55)

        if(len(caption) < 400):
            effect_font = ImageFont.truetype('fonts/Yu-Gi-Oh!2.ttf', 25)
            width=58
        else:
            effect_font = ImageFont.truetype('fonts/Yu-Gi-Oh!2.ttf', 15)
            width=85

        image_editable = ImageDraw.Draw(image)

        image_editable.text((72,69), title_text, (0, 0, 0), font=title_font)

        wrapper = textwrap.TextWrapper(width) 
        word_list = wrapper.wrap(text=caption) 
        caption_new = ''
        for ii in word_list[:-1]:
            caption_new = caption_new + ii + '\n'
        caption_new += word_list[-1]

        margin = 70
        offset = 900
        image_editable.text((margin, offset), caption_new, font=effect_font, fill="#000000")

        self.printCard(image, myimage)

    def trapGen(self):
        
        myimage = self.getImage()
        
        title_text = self.getName()

        caption = self.getDesc()

        # fetching template
        image = Image.open("img/trap_template.png")

        if(len(title_text)<20):
            title_font = ImageFont.truetype('fonts/Yu-Gi-Oh!1.ttf', 80)
        else:
            title_font = ImageFont.truetype('fonts/Yu-Gi-Oh!1.ttf', 55)

        if(len(caption) < 400):
            effect_font = ImageFont.truetype('fonts/Yu-Gi-Oh!2.ttf', 25)
            width=58
        else:
            effect_font = ImageFont.truetype('fonts/Yu-Gi-Oh!2.ttf', 15)
            width=85

        image_editable = ImageDraw.Draw(image)

        image_editable.text((72,69), title_text, (0, 0, 0), font=title_font)

        wrapper = textwrap.TextWrapper(width) 
        word_list = wrapper.wrap(text=caption) 
        caption_new = ''
        for ii in word_list[:-1]:
            caption_new = caption_new + ii + '\n'
        caption_new += word_list[-1]

        margin = 70
        offset = 900
        image_editable.text((margin, offset), caption_new, font=effect_font, fill="#000000")

        self.printCard(image, myimage)




#=======================================================================================================================
#============================================== MAIN ===================================================================


randomCard = Card()

if randomCard.getType() == "Spell Card":
    randomCard.spellGen()
elif randomCard.getType() == "Trap Card":
    randomCard.trapGen()
else:
    randomCard.monsterGen()
