from PIL import Image, ImageDraw, ImageFont

CONVIDADOS = ["Eduardo Castilho"]

LEFT_BORDER = 300
#font1 = ImageFont.truetype("./font1.tff", size=60)
font1 = ImageFont.truetype("/home/vkn/Documentos/CursosAlura/Python3/Python_img/font1.ttf", size=60)
font2 = ImageFont.truetype("/home/vkn/Documentos/CursosAlura/Python3/Python_img/font2.ttf", size=50)

for convidado in CONVIDADOS:
    imagem = Image.open("/home/vkn/Documentos/CursosAlura/Python3/Python_img/certificado.jpg").convert("RGBA")

    lapis = ImageDraw.Draw(imagem)

    lapis.text((LEFT_BORDER, 500), text=f"Olá {convidado}", fill="#000", font=font1)

    #lapis.line((LEFT_BORDER, 145, 398, 145), fill="#ccc", width=5)

    lapis.text(
        (LEFT_BORDER, 600),
        text="Você concluiu o curso de Barra de Access",fill="#000", font=font2,
    )

    lapis.text(
        (LEFT_BORDER, 680), text="No Dia 28/02/2020", fill="#000", font=font2
    )

    lapis.text((LEFT_BORDER, 760), text="Abraços!", fill="#000", font=font2)

    imagem.save(f"/home/vkn/Documentos/CursosAlura/Python3/Python_img/convite_{convidado}.png")
