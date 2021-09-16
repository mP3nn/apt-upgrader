import subprocess
import os
from dotenv import load_dotenv
from discord_webhook import DiscordWebhook, DiscordEmbed

# simple error handling with stderr output to webhook
def handleError(cmd):
    embed.set_title('Failure!')
    embed.add_embed_field(name='Traceback:', value=cmd.stderr.decode('utf-8'))
    embed.set_color('ff0033')
    embed.set_footer(text='This message was sent automatically by ' + os.getlogin())

# load .env into script, fetch webhook url
load_dotenv()
hook_url=os.getenv('URL')

# create webhook instance and embed message type instance
webhook = DiscordWebhook(url=hook_url)
embed = DiscordEmbed()

# run apt repository update
update = subprocess.run(['apt-get', 'update'], capture_output=True)

if update.returncode == 0:
    
    # if the update is successful, run the packages upgrade
    upgrade = subprocess.run(['apt-get', 'upgrade', '-y'], capture_output=True)
    
    # if the upgrade is successful, parse the output and send to webhook
    if upgrade.returncode == 0:
            
        out = upgrade.stdout.decode('utf-8').split('\n')

        try:
            # index of 'The following packages will be upgraded:' + 1 is where the pkgs names are
            pkgs_index = out.index('The following packages will be upgraded:') + 1

            embed.set_title('Update Successful!')
            embed.add_embed_field(name='Updated Packages:', value=out[pkgs_index].strip().replace(' ', ', '))
            embed.set_color('4bb543')
            embed.set_footer(text='This message was sent automatically by ' + os.getlogin())
            
        # if the strings is not present (thus no pkgs needed upgrades), .index() returns ValueError    
        except ValueError:
            embed.set_title('No Update Needed!')
            embed.set_description('All packages are up-to-date, yay!')
            embed.set_color('0099cc')
            embed.set_footer(text='This message was sent automatically by ' + os.getlogin())
    
    
    else:
        handleError(upgrade)
else:
    handleError(update)

webhook.add_embed(embed)
webhook.execute()
