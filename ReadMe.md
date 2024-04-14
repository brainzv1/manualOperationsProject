Note:It looks better on code editor.

How to run
To execute the code, we created a conda environment named “openmmlab” (see ref)
Make sure you have 3.8.19 and torch 1.9.0+cu111. Run in terminal: pip install mmcv==2.1.0 and pip install mmengine==0.10.3.
mmaction2 should be installed from source, make sure the .py files we wrote (the source code) are in the directory Yosef+Yuval_Project.
open a directory named “DataSet” in the “mmaction2” directory and inside it put the data under the directory “Data”. You can use the following picture for reference:


Last but not least it is very important that before you run train you change the code of the tsn file: Yosef+Yuval_Project\mmaction2\configs\recognition\tsn\tsn_imagenet-pretrained-r50_8xb32-1x1x3-100e_kinetics400-rgb.py
Entering the version from our source code will allow you to train and presumably achieve similar outcomes to what we had.
To process the data prior to training we created the filesToRun.py file which activates a series of the files we wrote ourselves to organize data.
If you followed all the instructions as follow you are supposed to be able to run the command in your terminal
python tools/train.py configs/recognition/tsn/tsn_imagenet-pretrained-r50_8xb32-1x1x3-100e_kinetics400-rgb.py

Notice: the train process is heavy on the GPU, and it uses a lot of resources from your computer, make sure to give it a lot of time to run.
You can also configure the number of epochs or other variables.
git repisotry for our code https://github.com/brainzv1/manualOperationsProject/edit/main/ReadMe.md
If there any problem here is the result of pip list using our conda env

(openmmlab) PS C:\AAAWork\Yosef+Yuval_Project\mmaction2> pip list
Package                 Version      Editable project location
----------------------- ------------ ----------------------------------------
absl-py                 2.1.0
addict                  2.4.0
aliyun-python-sdk-core  2.15.0
aliyun-python-sdk-kms   2.16.2
appdirs                 1.4.4
attrs                   23.2.0
audioread               3.0.1
av                      12.0.0
Brotli                  1.0.9
cachetools              5.3.3
certifi                 2024.2.2
cffi                    1.16.0
charset-normalizer      2.0.4
click                   8.1.7
colorama                0.4.6
contourpy               1.1.1
coverage                7.4.4
crcmod                  1.7
cryptography            42.0.5
cycler                  0.12.1
decorator               4.4.2
decord                  0.6.0
docker-pycreds          0.4.0
einops                  0.7.0
exceptiongroup          1.2.0
filelock                3.13.1
flake8                  7.0.0
fonttools               4.50.0
fsspec                  2024.3.1
ftfy                    6.2.0
future                  1.0.0
gitdb                   4.0.11
GitPython               3.1.42
gmpy2                   2.1.2
google-auth             2.29.0
google-auth-oauthlib    1.0.0
grpcio                  1.62.1
idna                    3.4
imageio                 2.34.0
imageio-ffmpeg          0.4.9
imgaug                  0.4.0
importlib_metadata      7.1.0
importlib_resources     6.4.0
iniconfig               2.0.0
interrogate             1.5.0
isort                   4.3.21
Jinja2                  3.1.3
jmespath                0.10.0
joblib                  1.3.2
kiwisolver              1.4.5
lazy_loader             0.3
librosa                 0.10.1
llvmlite                0.41.1
lmdb                    1.4.1
Markdown                3.6
markdown-it-py          3.0.0
MarkupSafe              2.1.3
matplotlib              3.7.5
mccabe                  0.7.0
mdurl                   0.1.2
mkl-fft                 1.3.8
mkl-random              1.2.4
mkl-service             2.4.0
mmaction2               1.2.0        c:\aaawork\yosef+yuval_project\mmaction2
mmcv                    2.1.0
mmengine                0.10.3
model-index             0.1.11
moviepy                 1.0.3
mpmath                  1.3.0
msgpack                 1.0.8
networkx                3.1
ninja                   1.11.1.1
numba                   0.58.1
numpy                   1.24.3
oauthlib                3.2.2
openai-clip             1.0.1
opencv-contrib-python   4.9.0.80
opencv-python           4.9.0.80
opendatalab             0.0.10
openmim                 0.3.9
openxlab                0.0.37
ordered-set             4.1.0
oss2                    2.17.0
packaging               24.0
pandas                  2.0.3
parameterized           0.9.0
pillow                  10.2.0
PIMS                    0.6.1
pip                     23.3.1
platformdirs            4.2.0
pluggy                  1.4.0
pooch                   1.8.1
proglog                 0.1.10
protobuf                4.25.3
psutil                  5.9.8
py                      1.11.0
pyasn1                  0.6.0
pyasn1_modules          0.4.0
pycodestyle             2.11.1
pycparser               2.21
pycryptodome            3.20.0
pyflakes                3.2.0
Pygments                2.17.2
pyparsing               3.1.2
PySocks                 1.7.1
pytest                  8.1.1
pytest-runner           6.0.1
python-dateutil         2.9.0.post0
PyTurboJPEG             1.7.3
pytz                    2023.4
PyWavelets              1.4.1
pywin32                 306
PyYAML                  6.0.1
regex                   2023.12.25
requests                2.28.2
requests-oauthlib       2.0.0
rich                    13.4.2
rsa                     4.9
scikit-image            0.21.0
scikit-learn            1.3.2
scipy                   1.10.1
sentry-sdk              1.43.0
setproctitle            1.3.3
setuptools              60.2.0
shapely                 2.0.3
six                     1.16.0
slicerator              1.1.0
smmap                   5.0.1
soundfile               0.12.1
soxr                    0.3.7
sympy                   1.12
tabulate                0.9.0
tensorboard             2.14.0
tensorboard-data-server 0.7.2
termcolor               2.4.0
threadpoolctl           3.4.0
tifffile                2023.7.10
toml                    0.10.2
tomli                   2.0.1
torch                   1.9.0+cu111
torchaudio              0.9.0
torchvision             0.10.0+cu111
tqdm                    4.65.2
typing_extensions       4.9.0
tzdata                  2024.1
urllib3                 1.26.18
wandb                   0.16.5
wcwidth                 0.2.13
Werkzeug                3.0.1
wheel                   0.41.2
win-inet-pton           1.1.0
xdoctest                1.1.3
yapf                    0.40.2
zipp                    3.18.1
