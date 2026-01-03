# KSP-LMP-Server-Save-Importer
Lost some vessels from your Luna Multiplayer server? Want to copy a singleplayer save to multiplayer?
Transfer vessels from KSP save files (ending in .sfs, often found in the KSP saves backup directory of any client recently connected to the server) into the LMP server vessels format.

# Usage:
1. Shutdown the LMP Server if running.
2. Find your KSP save file path, usually in your KSP install directory. For example, `C:/Steam/SteamApps/Common/Kerbal Space Program/Saves/LunaMultiplayer/Backup/persistent (...).sfs` <img width="829" height="266" alt="image" src="https://github.com/user-attachments/assets/93844c46-0470-4faf-b634-c6af269a9448" />
3. Find your LMP Server vessels directory. This will depend on where your LMP Server is installed. You will need the `.../LMPServer/Universe/Vessels/` directory. <img width="1036" height="706" alt="image" src="https://github.com/user-attachments/assets/b22c404e-b547-4b6c-9f07-ac99713482f6" />
4. Make a backup of your current vessels directory. For example by renaming it to `Vessels.old`, or copying it elsewhere.
5. Run the python script and input the directories when prompted.
7. Restart the server and enjoy your vessels back!
