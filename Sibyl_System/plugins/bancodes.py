from Sibyl_System import system_cmd, System
import os



@System.on(system_cmd(pattern=r"bancodes"))
async def bancodes(event):
    try:
        user_id = event.text.split(" ", 1)[1]
    except IndexError:
        return
        await event.reply("HERE ARE THE BAN CODES FOR EDITH -X :

• `ED-X_01` - RAID PARTICIPANT
• `ED-X_02` - RAID/SPAM INFLAMMER
• `ED-X_03` - SCAMMER
• `ED-X_04` - SPAM ADDING MEMBER
• `ED-X_05` - ABUSE SPAM 
• `ED-X_06` - NSFW SPAMMER
• `ED-X_07` - IMPERSONATION
• `ED-X_08` - MD/BTC SCAM
• `ED-X_09` - ADDING SPAMBOTS
• `ED-X_10` - ILLEGAL
• `ED-X_11` - PHISHING
• `ED-X_12` - FRAUD PROMOTION  (ANY KIND)
• `ED-X_13` - CYBER THREATENING/CYBER BULLY 
• `ED-X_14` - CHILD ABUSE 
• `ED-X_15` - BAN EVASION 
• `ED-X_16` - SPAMBOT
• `ED-X_17` - RAID INITIALIZOR
• `ED-X_18` - CRIMINAL ACT


THIS SCANNER BANS ONLY APPLY TO YOUR GROUP IF U ARE USING ANY ONE OF THE BOTS IN [THIS LIST](https://t.me/EdithXinfo/12)")
        return
