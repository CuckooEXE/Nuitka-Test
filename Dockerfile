FROM alpine:latest

# Add required packages to build python with all extensions
RUN apk --no-cache add coreutils git gcc musl make  \
                       build-base \
                       jpeg-dev \
                       bzip2-dev \
                       bzip2 \
                       zlib-dev \
                       freetype-dev \
                       lcms2-dev \
                       openjpeg-dev \
                       tiff-dev \
                       tk-dev \
                       tcl-dev \
                       openssl \
                       openssl-dev \
                       libffi-dev

# Clone the Python project
RUN git clone -b 3.10 https://github.com/python/cpython.git /cpython/

# Build/Install the Python project with defaults
WORKDIR /cpython/
RUN ./configure
RUN make -j`nproc` install

# Copy over project files
COPY ./ /nuitka-test/
WORKDIR /nuitka-test/

# Install dependencies/Build dependencies/Build test
RUN python3 -m pip install requests nuitka
RUN gcc -shared test_library.c -o test_library.so
# RUN python3 -m nuitka --static-libpython=yes --follow-imports nuitka-test.py
