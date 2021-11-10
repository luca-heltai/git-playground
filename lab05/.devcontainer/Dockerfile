FROM pytorch/pytorch:latest

RUN useradd normal
RUN mkdir /home/normal
RUN chown normal:normal /home/normal
RUN /opt/conda/bin/pip install pytest
RUN /opt/conda/bin/conda install --name base autopep8 -y

USER normal

RUN mkdir -p /home/normal/.vscode-server/extensions
RUN mkdir -p /home/normal/.vscode-server-insiders/extensions

RUN conda init bash
