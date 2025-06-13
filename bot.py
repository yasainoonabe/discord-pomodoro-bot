import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

# .envからトークン読み込み
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Intents設定
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# グローバル変数で状態管理
is_running = False

@bot.event
async def on_ready():
    print(f"✅ ログイン完了！Bot名：{bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("ポモドーロBot起動中🍅")

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"✅ 接続完了：{channel.name} に入ったンゴ")
    else:
        await ctx.send("⚠️ 先にボイスチャンネルに入ってンゴ")

@bot.command()
async def pomo(ctx, work_time: int = 25, break_time: int = 5, cycles: int = 4):
    global is_running
    if is_running:
        await ctx.send("⚠️ すでにポモドーロタイマーが動いてるンゴ")
        return
    is_running = True

    await ctx.send(f"🍅 ポモドーロ開始！{cycles}セット（{work_time}分作業 + {break_time}分休憩）")

    for i in range(cycles):
        if not is_running:
            await ctx.send("🛑 ポモドーロを中断しましたンゴ")
            break
        await ctx.send(f"▶️ **セット{i+1}/{cycles}**：{work_time}分作業開始！")
        await asyncio.sleep(work_time * 60)

        if not is_running:
            await ctx.send("🛑 ポモドーロを中断しましたンゴ")
            break
        if i < cycles - 1:
            await ctx.send(f"💤 セット{i+1}終了。{break_time}分休憩ンゴ〜")
            await asyncio.sleep(break_time * 60)

    if is_running:
        await ctx.send("✅ 全セット完了ンゴ🍵")

    is_running = False

@bot.command()
async def stop(ctx):
    global is_running
    if is_running:
        is_running = False
        await ctx.send("🛑 タイマーを停止したンゴ")
    else:
        await ctx.send("⚠️ 今はタイマー動いてないンゴ")


bot.run(TOKEN)
