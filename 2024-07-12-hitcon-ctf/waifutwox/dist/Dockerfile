FROM ubuntu:22.04

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y wget unzip cmake build-essential libopencv-dev git vim clang llvm
RUN wget -q https://download.pytorch.org/libtorch/cpu/libtorch-shared-with-deps-2.1.0%2Bcpu.zip
RUN unzip libtorch-shared-with-deps-2.1.0+cpu.zip -d /usr/share

COPY waifutwox /root

WORKDIR /root

CMD ["/root/waifutwox"]
