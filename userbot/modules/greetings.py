from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo Semua Saya {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("`Hae Semua Nya....`")
    sleep(3)
    await msg.delete()
# @GabuterTololsCH


@register(outgoing=True, pattern='^p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo Semua Saya {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("`Hae Semua Nya.....`")
    sleep(3)
    await msg.delete()
# @GabuterTololsCH


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Lah ngatur...`")
    sleep(1)
    await typew.edit("`Hae too.....`")
    sleep(3)
    await msg.delete()
# @GabuterTololsCH


@register(outgoing=True, pattern='^l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Lah ngatur...`")
    sleep(1)
    await typew.edit("`Hae too.....`")
    sleep(3)
    await msg.delete()
# @GabuterTololsCH


@register(outgoing=True, pattern='^aa(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("Gawr gura : **AaaaaaaaaaaaaaaaaaA** ")
# @GabuterTololsCH

CMD_HELP.update({
    "greetingwra":
    "`P`\
\nUsage: Untuk Memberi salam.\
\n\n`L`\
\nUsage: Greetings tapi boong .\
\n\n`aa`\
\nUsage : Be Gwra."
})
