docker run -t --user $(id -u):$(id -g) -v `pwd`:/workspace custom-pytorch /bin/bash -c "cd /workspace; $@"