# AutoMapBlur for Streamlabs OBS

AutoMapBlur allows you to automatically blur your game capture whenever the in-game map is opened, protecting sensitive information and preventing stream sniping.

## Features
- **Toggle Blur:** Press the map key (default: "M") to toggle the blur on/off for your game capture in Streamlabs OBS.
- **Customizable Keybinding:** You can customize the key used to trigger the blur.
- **Adjustable Blur Intensity:** Modify the blur intensity to suit your preference, from 1 (light blur) to 20 (heavy blur).

## Installation Instructions

### Step 1: Set Up WebSocket in Streamlabs OBS
1. Make sure **WebSocket** is enabled in Streamlabs OBS.
   - Go to **Settings > Remote Control** and enable WebSocket.
   - Set a WebSocket password (you’ll need this for the script to connect).

### Step 2: Add the Script to Streamlabs OBS
1. Download the script `AutoMapBlur_Streamlabs.py`.
2. In Streamlabs OBS, go to **Tools > Scripts**.
3. Click the **+** button and browse to select `AutoMapBlur_Streamlabs.py` from your downloads.
4. After adding, the script will appear in the Scripts window.

### Step 3: Configure the Script
1. Select the **source** you want to apply the blur to (e.g., game capture).
   - You will see a text field called **Source Name** in the script settings panel.
2. Adjust the **blur intensity** to your preference.
   - Use the **Blur Intensity** slider to choose a value between 1 and 20.
3. Set the **Map Key** (optional).
   - If you want to use a key other than the default "M", enter the key in the **Map Key** field.

### Step 4: Start Streaming
1. Once configured, AutoMapBlur will automatically activate the blur effect when you press the map key during your stream.
2. Press the map key again to remove the blur.

## Project Board
Stay up to date with progress and contribute via our [AutoMapBlur Project Board](https://github.com/users/WhyTrashEarth/projects/1).

## GitHub Repository
Find the complete source code and additional details at our [GitHub Repository](https://github.com/WhyTrashEarth/AUTOMAPBLUR).

## Usage
- **Toggle Blur:** Press the map key to apply the blur effect when the in-game map is open. Press again to remove the blur.
- **Customization:** The blur intensity and keybinding can be modified via the script settings panel in Streamlabs OBS.

## Troubleshooting
- Ensure the **Source Name** matches exactly with the name of your game capture or desired source in Streamlabs OBS.
- If the blur effect does not activate, check the keybinding or increase the blur intensity.
- If the script isn’t working, try removing it and re-adding it under **Tools > Scripts**.

## Contributing
If you’d like to contribute or report issues, please visit the [AutoMapBlur GitHub Repository](https://github.com/WhyTrashEarth/AUTOMAPBLUR).

## Credits
AutoMapBlur was conceptualized by [@WhyTrashEarth](https://x.com/WhyTrashEarth) and developed with the support of the community.

## License
This project is licensed under the **CC0 1.0 Universal (Creative Commons Zero v1.0)** Public Domain Dedication. Feel free to use, modify, and distribute this tool as you see fit.
