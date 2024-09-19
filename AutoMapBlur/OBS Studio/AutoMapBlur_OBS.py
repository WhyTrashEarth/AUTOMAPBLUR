import obspython as obs

# Global variables to store script settings
blur_active = False  # Track if blur is currently active
blur_intensity = 5  # Default blur intensity (adjustable)
map_key = "M"  # Default key for map (adjustable)

# Callback function to toggle blur on and off when the map key is pressed
def toggle_blur(pressed):
    global blur_active
    global blur_intensity

    if pressed:  # Only trigger on key press, not key release
        source_name = obs.obs_data_get_string(settings, "source")
        source = obs.obs_get_source_by_name(source_name)

        if source is None:
            print(f"Source '{source_name}' not found.")
            return

        if not blur_active:
            apply_blur(source)
            blur_active = True
        else:
            remove_blur(source)
            blur_active = False

        obs.obs_source_release(source)

# Apply blur effect to the selected source
def apply_blur(source):
    blur_filter = obs.obs_source_get_filter_by_name(source, "blur")
    if blur_filter is None:  # Create blur filter if it doesn't exist
        create_blur_filter(source)
    else:
        update_blur_intensity(blur_filter, blur_intensity)

# Create a new blur filter on the source
def create_blur_filter(source):
    filter_settings = obs.obs_data_create()
    obs.obs_data_set_int(filter_settings, "filter.blur_size", blur_intensity)

    blur_filter = obs.obs_source_create("gpu_blur_filter", "blur", filter_settings, None)
    obs.obs_source_filter_add(source, blur_filter)
    obs.obs_data_release(filter_settings)

# Update the intensity of the existing blur filter
def update_blur_intensity(blur_filter, intensity):
    settings = obs.obs_source_get_settings(blur_filter)
    obs.obs_data_set_int(settings, "filter.blur_size", intensity)
    obs.obs_source_update(blur_filter, settings)
    obs.obs_data_release(settings)

# Remove the blur filter
def remove_blur(source):
    blur_filter = obs.obs_source_get_filter_by_name(source, "blur")
    if blur_filter is not None:
        obs.obs_source_filter_remove(source, blur_filter)
        obs.obs_source_release(blur_filter)

# Hotkey event handler
def on_event(event):
    if event == obs.OBS_FRONTEND_EVENT_KEY_PRESSED:
        toggle_blur(True)

# Script properties (GUI settings)
def script_properties():
    props = obs.obs_properties_create()

    obs.obs_properties_add_text(props, "source", "Source Name", obs.OBS_TEXT_DEFAULT)
    obs.obs_properties_add_int_slider(props, "blur_intensity", "Blur Intensity", 1, 20, 1)
    obs.obs_properties_add_text(props, "map_key", "Map Key", obs.OBS_TEXT_DEFAULT)

    return props

# Script update function (for settings)
def script_update(settings):
    global blur_intensity
    global map_key

    blur_intensity = obs.obs_data_get_int(settings, "blur_intensity")
    map_key = obs.obs_data_get_string(settings, "map_key")

# Script load function (called when the script is loaded)
def script_load(settings):
    obs.obs_frontend_add_event_callback(on_event)
