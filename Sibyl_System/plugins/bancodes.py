from Sibyl_System import system_cmd, System
from Sibyl_System.strings import ban_codes_string



@System.on(system_cmd(pattern=r"bancodes", allow_enforcer=True, allow_inspector=True))
async def bancodes(event):
    try:
        await event.reply("{ban_codes_string}")
        return
