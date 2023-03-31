from aiogram import *
from PIL import Image
from moviepy.editor import *
 
token = "token here"

# Разработчик https://t.me/osh1script
# Разработчик https://t.me/osh1script
# Разработчик https://t.me/osh1script

bot = Bot(token=token) # Токен
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def welcome(message):
    await message.answer("Привет, я помогу тебе наложить лого нептуна на твое фото")

# Разработчик https://t.me/osh1script

@dp.message_handler(content_types=["photo"])
async def welcome(message):
    await message.photo[-1].download("filename.jpg")
    img = Image.open("filename.jpg")
    watermark = Image.open("logo-small.png")
    (width, height) = img.size
    (widthh, heightt) = watermark.size
    a = widthh//2
    b = heightt//2
    y = width//2-a
    x = height//2-b
    img.paste(watermark, (y, x), watermark)
    img.save("inlogo.jpg")
    photo = open("inlogo.jpg", "rb")
    await bot.send_photo(chat_id=message.chat.id, photo=photo)

# Разработчик https://t.me/osh1script

@dp.message_handler(content_types=["video"])
async def download_video(message: types.Message):
    file_id = message.video.file_id 
    file = await bot.get_file(file_id) 
    await bot.download_file(file.file_path, "video.mp4")
    video1 = VideoFileClip(r"video.mp4")  
     
    logo = (ImageClip(r"logo-small.png")  
            .set_duration(video1.duration) 
              .resize(height=100)  
              .set_pos(("center"))) 
     
    final = CompositeVideoClip([video1, logo])  
    final.write_videofile(r"kino10.mp4", audio=True) 
    await bot.send_video(message.chat.id, open('kino10.mp4', 'rb'))

# Разработчик https://t.me/osh1script
# Разработчик https://t.me/osh1script
# Разработчик https://t.me/osh1script

if __name__ == '__main__':
 executor.start_polling(dp)
    
