import obswebsocket as obsws
import obswebsocket.requests as obsrq

# Global variables for the Streamlabs script
blur_active = False  # To track if the blur is active
blur_intensity = 5  # Default intensity of the blur (customizable)
map_key = "M"  # Default key to trigger map (customizable)

# Connect to Streamlabs OBS WebSocket
client = obsws.obsws("localhost", 4444, "your_password")  # Ensure this is set up correctly

def toggle_blur():
    global blur_active
    global blur_intensity

    try:
        client.connect()  # Connect to the Streamlabs OBS WebSocket server
    except:
        print("Could not connect to Streamlabs OBS WebSocket. Make sure it's running.")

    # Get the current active scene
    current_scene = client.call(obsrq.GetCurrentScene()).getName()
    source_name = "Your Game Capture Source"

    if blur_active:
        # Remove blur filter from source if it's active
        client.call(obsrq.RemoveFilterFromSource(sourceName=source_name, filterName="Blur"))
        blur_active = False
    else:
        # Add blur filter to the source
        filter_settings = {
            "filter.blur_size": blur_intensity
        }
        client.call(obsrq.AddFilterToSource(sourceName=source_name, filterName="Blur", filterSettings=filter_settings))
        blur_active = True

    client.disconnect()

def handle_keypress(event):
    if event.key == map_key and event.pressed:
        toggle_blur()

# The function to set keybinding and other script settings
def script_properties():
    props = obs.obs_properties_create()

    obs.obs_properties_add_int_slider(props, "blur_intensity", "Blur Intensity", 1, 20, 1)
    obs.obs_properties_add_text(props, "map_key", "Map Key", obs.OBS_TEXT_DEFAULT)

    return props

# Update function for changes in properties
def script_update(settings):
    global blur_intensity
    global map_key

    blur_intensity = obs.obs_data_get_int(settings, "blur_intensity")
    map_key = obs.obs_data_get_string(settings, "map_key")
