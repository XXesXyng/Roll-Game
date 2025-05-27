import discord
from discord.ext import commands
import random
import os

# ----- 설정 -----
TOKEN = os.getenv("TOKEN")

# 채널 ID 따로따로


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# 주사위 이미지가 저장된 폴더
DICE_IMAGE_DIR = "dice_images"

started = False

@bot.event
async def on_ready():
    global started
    if not started:
        print(f"✅ 봇 로그인됨: {bot.user}")
        started = True

@bot.command(name="주사위")
async def roll_dice(ctx):
    dice_result = random.randint(1, 6)
    embed = discord.Embed(
        title="🎲 주사위 결과!",
        description=f"{ctx.author.mention}님이 굴린 주사위는 **{dice_result}** 입니다!",
        color=discord.Color.blurple()
    )

    image_path = os.path.join(DICE_IMAGE_DIR, f"{dice_result}.png")

    if os.path.exists(image_path):
        file = discord.File(image_path, filename="dice.png")
        embed.set_thumbnail(url="attachment://dice.png")
        await ctx.send(embed=embed, file=file)
    else:
        embed.add_field(name="⚠️ 이미지 없음", value="주사위 이미지 파일을 찾을 수 없습니다.")
        await ctx.send(embed=embed)

# 디스코드 봇 토큰으로 실행
if __name__ == "__main__":
    bot.run(TOKEN)
