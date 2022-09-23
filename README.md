
> *NOTE:* This is a fork of [xdspacelab/openvslam](https://github.com/xdspacelab/openvslam). The original repository is no longer available. Please read the [official statement of termination](https://github.com/xdspacelab/openvslam/wiki/Termination-of-the-release) carefully and understand it before using this. The similarities with ORB_SLAM2 in the original version are not removed. We share this code on GPLv3 License as in [ORB_SLAM2](https://github.com/raulmur/ORB_SLAM2/blob/master/LICENSE.txt).

# Clone repo

```
git clone https://github.com/MapsHD/openvslam-fork.git
```

# Prepare dataset

Download files from [Release](https://github.com/MapsHD/openvslam-fork/releases)

Dataset directory structure:

```
- dataset
  - images/
  - config_openvslam.yaml
```

# Build container

```
docker build -t vslam -f Dockerfile . --build-arg NUM_THREADS=4
```

# Run container

## Run on Linux

```
sudo xhost +
docker run -it --rm --device=/dev/dri:/dev/dri -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix:ro --volume /on_the_host/data/path/to/dataset:/dataset:rw vslam
./build/run_image_slam -v /openvslam/orb_vocab.dbow2 -i /dataset/images/ -c /dataset/config_openvslam.yaml --no-sleep --auto-term --map-db /dataset/map.msg
python3 scripts/openvslam2json.py /dataset/map.msg /dataset/map.json
cat /dataset/map.json
```

## Run on Windows

1. Start XLaunch

2. Using WSL terminal:

```
export DISPLAY=127.0.0.1:0.0
docker run --rm -it -e DISPLAY=host.docker.internal:0.0 -e LIBGL_ALWAYS_INDIRECT=0 --volume /mnt/c/on_the_host/data/path/to/dataset:/dataset:rw vslam
export DISPLAY=host.docker.internal:0.0
./build/run_image_slam -v /openvslam/orb_vocab.dbow2 -i /dataset/images/ -c /dataset/config_openvslam.yaml --no-sleep --auto-term --map-db /dataset/map.msg
python3 scripts/openvslam2json.py /dataset/map.msg /dataset/map.json
cat /dataset/map.json
```
