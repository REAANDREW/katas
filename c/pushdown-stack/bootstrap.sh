if [ -d "gyp" ]; then
    echo "gyp directory already exists so skipping clone"
else
    git clone https://chromium.googlesource.com/external/gyp.git
fi
mkdir -p build
./gyp/gyp -f make --depth . --generator-output build/ pushdown-stack.gyp
(cd build/ ; make)
