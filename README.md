1. python version = 3.9.0
2. create a conda environment
    conda create -n oncology python=3.9.0
3. Pytorch is necessary for this project
    conda install pytorch torchvision torchaudio cpuonly -c pytorch --> CPU
    conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia --> GPU

4. install the package
    pip install -r requirements.txt