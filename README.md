# Assignment 1



## 1. System Information
cat /etc/os-release
#VERSION="22.04.5 LTS (Jammy Jellyfish)"
uname -r
#6.8.0-138-generic
lscpu
#架构：                       x86_64
#  CPU 运行模式：             32-bit, 64-bit
#  Address sizes:             48 bits physical, 48 bits virtual
# 字节序：                   Little Endian
#CPU:                         12
lspci | grep -Ei 'vga|3d|display'
#04:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Renoir (rev ce)
#04:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Renoir (rev ce)
lspci -k | grep -EA3 'VGA|3D|Display'
#04:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Renoir (rev ce)
#	Subsystem: Lenovo Renoir
#	Kernel driver in use: amdgpu
#	Kernel modules: amdgpu
echo "$XDG_SESSION_TYPE"
#wayland
无NAVIDA GPU
无CUDA



## 2. Python Project A
conda create -n robocon_a python=3.10 -y
#Channels:
# - https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge
# - conda-forge
#Platform: linux-64
#Collecting package metadata (repodata.json): done
conda activate robocon_a
python --version
#Python 3.10.21
which python
#/home/hu/miniforge3/envs/robocon_a/bin/python
pip install -e .
#Looking in indexes: https://pypi.tuna.tsinghua.edu.cn/simple
#Obtaining file:///home/hu/%E6%A1%8C%E9%9D%A2/ROBOCON-Vision-Assignment-1/ROBOCON-Vision-#Assignment1-Starter/python_A
#  Installing build dependencies ... done
#  Checking if build backend supports build_editable ... done
#  Getting requirements to build editable ... done
python camera.py --output ../../assets/python_a/raw_capture第五次.mp4
#Captured frames: 336
#Elapsed time:    34.5 s
#Loop rate:       9.7 frame/s



## 3. Process Observation
python camera.py --output ../../assets/python_a/文档观察2.mp4
pgrep -af 'python.*camera.py'
#6919 python camera.py --output ../../assets/python_a/文档观察2.mp4
ps -o pid,ppid,cmd,%cpu,%mem,etime -p 6919
#    PID    PPID CMD                         %CPU %MEM     ELAPSED
#   6919    2991 python camera.py --output .  136  0.9       00:57
pstree -p 6919
#python(6919)─┬─{python}(6920)
#             ├─{python}(6921)
#             ├─{python}(6922)
#             ├─{python}(6923)
#             ├─{python}(6924)
#             ├─{python}(6925)
#             ├─{python}(6926)
#             ├─{python}(6927)
#             ├─{python}(6928)
#             ├─{python}(6929)
#             ├─{python}(6930)
#             ├─{python}(6931)
#             ├─{python}(6932)
#             ├─{python}(6933)
#             ├─{python}(6934)
#             ├─{python}(6935)
#             ├─{python}(6936)
#             ├─{python}(6937)
#             ├─{python}(6938)
#             ├─{python}(6939)
#             ├─{python}(6940)
#             ├─{python}(6941)
#             └─{python}(6943)
htop



## 4. Python Project B
conda create -n robocon_b python=3.13 
conda activate robocon_b
python --version
#Python 3.13.15
which python
#/home/hu/miniforge3/envs/robocon_b/bin/python
pip install -e .
#  pip install [options] <requirement specifier> [package-index-options] ...
#  pip install [options] -r <requirements file> [package-index-options] ...
#  pip install [options] [-e] <vcs project url> ...
#  pip install [options] [-e] <local project path> ...
#  pip install [options] <archive url/path> ...

#-e option requires 1 argument
python analyze_video.py --input ../../assets/python_a/raw_capture第五次.mp4 --output ../../assets/python_b/processed_output.mp4
#Processed 300 frames...
#Processed 330 frames...
#Input:  /home/hu/桌面/ROBOCON-Vision-Assignment-1/assets/python_a/raw_capture第五次.mp4



## 5. C++ Manual Build
mkdir -p build
g++ -std=c++17 src/main.cpp src/transform.cpp \
  -Iinclude \
  -I/usr/include/eigen3 \
  $(pkg-config --cflags opencv4) \
  -o build/manual_cpp \
  $(pkg-config --libs opencv4)
  mkdir -p ../../assets/cpp
./build/manual_cpp ../../assets/python_a/raw_capture第五次.mp4 ../../assets/cpp/cpp_manual_output.mp4
#Input: ../../assets/python_a/raw_capture第五次.mp4
#Output: ../../assets/cpp/cpp_manual_output.mp4
#Frames: 336
#Mean scene luma: 55.7657
#Panels: original | Otsu binary | Canny edges
Q1：-I作用是什么
A1：全称Include（头文件，让代码能正确地被分开编译） path，可以指明头文件在磁盘中的位置
Q2：为什么transform.hpp不单独作为cpp文件编译
A2：缺少main函数，编译器无法编译。而transform包含了代码的流程，负责被调用但不需要执行流程。
Q3：为什么只写main.cpp往往无法得到完整程序
A3：main.cpp只负责组装，无法提供具体函数。
Q4：编译成功产生的文件是什么
A4：中间文件（.o）



## 6. CMake Build
cat > CMakeLists.txt << 'EOF'
cmake_minimum_required(VERSION 3.16)

project(robocon_cpp LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(OpenCV REQUIRED)
find_package(Eigen3 REQUIRED)

add_executable(cpp_task
    src/main.cpp
    src/transform.cpp
)

target_include_directories(cpp_task PRIVATE
    include
    ${OpenCV_INCLUDE_DIRS}
)

target_link_libraries(cpp_task PRIVATE
    ${OpenCV_LIBS}
    Eigen3::Eigen
)
EOF

cmake -S . -B build
#Build files have been written to: /home/hu/桌面/ROBOCON-Vision-Assignment-1/ROBOCON-Vision-Assignment1-Starter/cpp/build
cmake --build build -j$(nproc)
# Built target cpp_task
 mkdir -p ../../assets/cpp
./build/cpp_task ../../assets/python_a/raw_capture第五次.mp4 ../../assets/cpp/cpp_cmake_output.mp4
#Input: ../../assets/python_a/raw_capture第五次.mp4
#Output: ../../assets/cpp/cpp_cmake_output.mp4
#Frames: 336
#Mean scene luma: 55.7657
#Panels: original | Otsu binary | Canny edges



## 7. Git / GitHub

## 8. Problems and Note
