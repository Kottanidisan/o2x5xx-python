try:
    from o2x5xx import O2x5xxRPCDevice
except ModuleNotFoundError:
    from source.rpc.client import O2x5xxRPCDevice
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        address = sys.argv[1]
    else:
        address = '192.168.0.69'

    # create device
    device = O2x5xxRPCDevice(address)

    print("Requesting new session...")
    session = device.requestSession()
    session.setOperatingMode(mode=1)
    edit = session.edit
    print("Operation Mode {} (Edit) set".format(session.OperatingMode))
    newApplicationIndex = edit.createApplication()
    print("Created new application with index: " + str(newApplicationIndex))
    application = edit.editApplication(applicationIndex=newApplicationIndex)
    print("Starting editing application with index: " + str(newApplicationIndex))
    application.Name = "My new application"
    print("Changed name of application: " + application.Name)
    application.Description = "My new description"
    print("Changed description of application: " + application.Description)
    application.TriggerMode = 2  # continuous trigger mode
    print("Trigger Mode {} set".format(application.TriggerMode))

    # Setup of image001
    image001 = application.editImage(imageIndex=1)
    print("Start calculating auto exposure time...")
    image001.startCalculateExposureTime()
    print("End of calculating exposure time with recommended value: " + str(image001.ExposureTime))
    print("Start calculating autofocus...")
    image001.startCalculateAutofocus()
    print("End of calculating autofocus with recommended value(s): " + str(image001.getAutofocusDistances()))
    image001.Name = "My new image001"
    print("Changed name of image001: " + image001.Name)
    image001.FilterType = 1
    print("Changed filter type: " + str(image001.FilterType))
    image001.FilterStrength = 1
    print("Changed filter strength: " + str(image001.FilterStrength))

    # Setup of image002
    print("Creating new imager (image002) for application.")
    newImagerIndex = application.createImagerConfig()
    image002 = application.editImage(imageIndex=newImagerIndex)
    image002.Name = "My new image002"
    print("Changed name of image002: " + image002.Name)
    print("Start calculating auto exposure time...")
    image002.startCalculateExposureTime()
    image002.FilterType = 1
    image002.FilterStrength = 5
    image002.FilterInvert = True
    imageQuality = image002.ImageQualityCheck
    imageQuality.enabled = True
    print("image002: Quality check enabled: " + str(imageQuality.enabled))
    imageQuality.sharpness_thresholdMinMax = {"min": 1000, "max": 10000}
    imageQuality.meanBrightness_thresholdMinMax = {"min": 10, "max": 233}
    imageQuality.underexposedArea_thresholdMinMax = {"min": 10, "max": 88}
    imageQuality.overexposedArea_thresholdMinMax = {"min": 33, "max": 55}

    # Setup of image003
    print("Creating new imager (image003) for application.")
    newImagerIndex = application.createImagerConfig()
    image003 = application.editImage(imageIndex=newImagerIndex)
    image003.Name = "My new image003"
    print("Changed name of image003: " + image003.Name)
    print("Start calculating auto exposure time...")
    image003.startCalculateExposureTime()
    image003.startCalculateAutofocus()
    image003.FilterType = 3
    image003.FilterStrength = 1

    # Setup of image004
    print("Creating new imager (image004) for application.")
    newImagerIndex = application.createImagerConfig()
    image004 = application.editImage(imageIndex=newImagerIndex)
    image004.Name = "My new image004"
    print("Changed name of image004: " + image004.Name)
    image004.startCalculateAutofocus()
    image004.AnalogGainFactor = 1
    image004.ExposureTime = 15000
    image004.FilterInvert = True

    # Setup of image005
    print("Creating new imager (image005) for application.")
    newImagerIndex = application.createImagerConfig()
    image005 = application.editImage(imageIndex=newImagerIndex)
    image005.Name = "My new image005"
    print("Changed name of image005: " + image005.Name)
    image005.startCalculateAutofocus()
    image005.AnalogGainFactor = 2
    image005.ExposureTime = 7500

    application.save()
    print("Saving parameter consistent to memory for application " + application.Name)
    session.setOperatingMode(mode=0)
    print("Operation Mode {} (Run) set".format(session.OperatingMode))
    session.cancelSession()
    print("Session closed")
    device.switchApplication(applicationIndex=newApplicationIndex)
    print("Application with new index {} now active".format(newApplicationIndex))
