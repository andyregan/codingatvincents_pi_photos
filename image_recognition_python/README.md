# Example Image Recognition App For Coding@Vincents

## Take a photo of an object and use MXNet to identify it

## Clone this project

```bash
mkdir -p ~/code
cd code
git clone https://github.com/andyregan/codingatvincents_pi_photos.git
```

## Enable the Camera

Run `sudo raspi-config` and choose in the menu to enable the pi camera. A reboot is needed after this.

```bash
sudo apt-get update
sudo apt-get install python3-picamera
```

Review https://www.raspberrypi.org/documentation/usage/camera/python/README.md .

## Install Pip3

```bash
sudo apt-get update
sudo apt-get install python3-pip
```

## Install Pipenv
```bash
pip3 install pipenv
```

## Set up a new pipenv for your project

```bash
cd ~/code/codingatvincents_pi_photos/image_recognition_python
pipenv --three --site-packages install
pipenv shell
pipenv install mxnet
pipenv install --dev ipython
```

## Run Example

```bash
cd ~/code/codingatvincents_pi_photos/image_recognition_python
pipenv shell
python recognize.py images/image1.jpg
```

You should see the following output.

```
I'm 85% sure that this is a banana.
```

## Resources

* https://www.raspberrypi.org/documentation/linux/software/python.md
* https://github.com/kennethreitz/pipenv
* https://medium.com/@julsimon/johnny-pi-i-am-your-father-part-5-adding-mxnet-for-local-image-classification-bc27a5fd2c27
* https://github.com/juliensimon/johnnypi/blob/master/part5/pi/inception.py
