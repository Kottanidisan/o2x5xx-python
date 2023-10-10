from o2x5xx import image_client
import o2x5xx
import matplotlib.pyplot as plt
import os 
from matplotlib.pyplot import savefig, imsave
import numpy as np


image_viewer = o2x5xx.ImageClient(address="192.168.1.69", port=50010)
#image_viewer.connect()
with image_viewer as i:
    image_viewer.turn_process_interface_output_on_or_off(0)
    answer = image_viewer.upload_process_interface_output_configuration(o2x5xx.images_config)
    if answer != "*":
        raise

    image_viewer.turn_process_interface_output_on_or_off(1)

    image_viewer.read_image_ids()
    image_viewer.read_next_frames()
    imglst = image_viewer.frames[0]

    print(len(imglst))
    print(len(imglst[0]))
    print(f"Gesamt:  {len(imglst) * len(imglst[0])}")

    plt.imshow(np.array(imglst), cmap="gray", interpolation="nearest")
    plt.savefig("D:/LernenBetrieb/PythonO2D/Programme/images/bild.png")
#image_viewer.disconnect()