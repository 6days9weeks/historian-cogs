from .cog import OnConnect


async def setup(bot):
    n = OnConnect(bot)
    bot.add_cog(n)
    await n.build_cache()
