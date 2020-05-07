APJ_TOOL = '/home/calfan/ardupilot/Tools/scripts/apj_tool.py'
AP_HAL_REL = '../../libraries/AP_HAL_ChibiOS'
AP_HAL_ROOT = '/home/calfan/ardupilot/libraries/AP_HAL_ChibiOS'
AP_LIBRARIES = ['AP_HAL_ChibiOS', 'AP_UAVCAN', 'modules/uavcan/libuavcan/src/**/*.cpp', 'modules/uavcan/libuavcan_drivers/stm32/driver/src/*.cpp']
AP_LIBRARIES_OBJECTS_KW = {'features': ['ch_ap_library']}
AP_PROGRAM_FEATURES = ['ch_ap_program']
AR = ['/cygdrive/c/Program Files (x86)/GNU Tools ARM Embedded/6 2017-q2-update/bin/arm-none-eabi-ar']
ARFLAGS = ['rcs']
BINDIR = '/usr/bin'
BOARD = 'fmuv3'
BOARD_MK = '/home/calfan/ardupilot/libraries/AP_HAL_ChibiOS/hwdef/common/chibios_board.mk'
BOOTLOADER = False
BOOTLOADER_OPTION = ''
BUILDDIR = '/home/calfan/ardupilot/build/fmuv3/modules/ChibiOS'
BUILDDIR_REL = 'modules/ChibiOS'
BUILDROOT = '/home/calfan/ardupilot/build/fmuv3'
BUILD_SUMMARY_HEADER = ['target', 'size_text', 'size_data', 'size_bss', 'size_total']
CC = ['/cygdrive/c/Program Files (x86)/GNU Tools ARM Embedded/6 2017-q2-update/bin/arm-none-eabi-gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('6', '3', '1')
CFLAGS = ['-ffunction-sections', '-fdata-sections', '-fsigned-char', '-Wall', '-Wextra', '-Wformat', '-Wshadow', '-Wpointer-arith', '-Wcast-align', '-Wundef', '-Wno-missing-field-initializers', '-Wno-unused-parameter', '-Wno-redundant-decls', '-Wno-unknown-pragmas', '-Wno-trigraphs', '-MMD', '-DUAVCAN_STM32_CHIBIOS=1', '-DUAVCAN_STM32_NUM_IFACES=2']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = []
CHIBIOS_BOARD_NAME = 'HAL_BOARD_NAME="fmuv3"'
CHIBIOS_BUILD_FLAGS = 'USE_FATFS=yes CHIBIOS_STARTUP_MK=os/common/startup/ARMCMx/compilers/GCC/mk/startup_stm32f4xx.mk CHIBIOS_PLATFORM_MK=os/hal/ports/STM32/STM32F4xx/platform.mk'
CHIBIOS_SCRIPTS = '/home/calfan/ardupilot/libraries/AP_HAL_ChibiOS/hwdef/scripts'
CH_ROOT = '/home/calfan/ardupilot/modules/ChibiOS'
CH_ROOT_REL = '../../modules/ChibiOS'
COMPILER_CC = 'gcc'
COMPILER_CXX = 'g++'
CPPPATH_ST = '-I%s'
CXX = ['/cygdrive/c/Program Files (x86)/GNU Tools ARM Embedded/6 2017-q2-update/bin/arm-none-eabi-g++']
CXXFLAGS = ['-std=gnu++11', '-fdata-sections', '-ffunction-sections', '-fno-exceptions', '-fsigned-char', '-Wall', '-Wextra', '-Wformat', '-Wshadow', '-Wpointer-arith', '-Wcast-align', '-Wundef', '-Wno-unused-parameter', '-Wno-missing-field-initializers', '-Wno-reorder', '-Wno-redundant-decls', '-Wno-unknown-pragmas', '-Werror=format-security', '-Werror=array-bounds', '-Werror=uninitialized', '-Werror=init-self', '-Werror=switch', '-Werror=sign-compare', '-Wfatal-errors', '-Wno-trigraphs', '-Werror=unused-but-set-variable', '-Wlogical-op', '-Wframe-larger-than=1300', '-fsingle-precision-constant', '-Wno-attributes', '-Wno-error=double-promotion', '-Wno-error=missing-declarations', '-Wno-error=float-equal', '-Wno-error=undef', '-Wno-error=cpp', '-Wno-cast-align', '-fno-exceptions', '-fno-rtti', '-fno-threadsafe-statics', '-Wall', '-Wextra', '-Wno-sign-compare', '-Wfloat-equal', '-Wpointer-arith', '-Wmissing-declarations', '-Wno-unused-parameter', '-Werror=array-bounds', '-Wfatal-errors', '-Werror=unused-variable', '-Werror=uninitialized', '-Werror=init-self', '-Wframe-larger-than=1024', '-Werror=unused-but-set-variable', '-Wno-missing-field-initializers', '-Wno-trigraphs', '-Os', '-fno-strict-aliasing', '-fomit-frame-pointer', '-falign-functions=16', '-ffunction-sections', '-fdata-sections', '-fno-strength-reduce', '-fno-builtin-printf', '-fno-builtin-fprintf', '-fno-builtin-vprintf', '-fno-builtin-vfprintf', '-fno-builtin-puts', '-mcpu=cortex-m4', '-mno-thumb-interwork', '-mthumb', '-mfpu=fpv4-sp-d16', '-mfloat-abi=hard', '-DCHIBIOS_BOARD_NAME="fmuv3"', '-DCYGWIN_BUILD', '-MMD', '-Wno-error=cast-align', '-DUAVCAN_STM32_CHIBIOS=1', '-DUAVCAN_STM32_NUM_IFACES=2']
CXXFLAGS_MACBUNDLE = ['-fPIC']
CXXFLAGS_cxxshlib = ['-fPIC']
CXXLNK_SRC_F = []
CXXLNK_TGT_F = ['-o']
CXX_NAME = 'gcc'
CXX_SRC_F = []
CXX_TGT_F = ['-c', '-o']
DEBUG = False
DEFINES = ['SKETCHBOOK="/home/calfan/ardupilot"', 'CONFIG_HAL_BOARD=HAL_BOARD_CHIBIOS', 'HAVE_OCLOEXEC=0', 'HAVE_STD_NULLPTR_T=0', 'UAVCAN_CPP_VERSION=UAVCAN_CPP03', 'UAVCAN_NO_ASSERTIONS=1', 'UAVCAN_NULLPTR=nullptr']
DEFINES_ST = '-D%s'
DEFINE_COMMENTS = {'WAF_BUILD': '', '__STDC_FORMAT_MACROS': '', 'HAVE_CMATH_ISFINITE': '', 'HAVE_CMATH_ISINF': '', 'HAVE_CMATH_ISNAN': '', 'NEED_CMATH_ISFINITE_STD_NAMESPACE': '', 'NEED_CMATH_ISINF_STD_NAMESPACE': '', 'NEED_CMATH_ISNAN_STD_NAMESPACE': '', 'HAVE_ENDIAN_H': '', 'HAVE_BYTESWAP_H': '', 'PYTHONDIR': '', 'PYTHONARCHDIR': '', '_GNU_SOURCE': ''}
DEST_BINFMT = 'elf'
DEST_CPU = 'arm'
DEST_OS = 'cygwin'
DSDL_COMPILER = '/home/calfan/ardupilot/modules/uavcan/libuavcan/dsdl_compiler/libuavcan_dsdlc'
DSDL_COMPILER_DIR = '/home/calfan/ardupilot/modules/uavcan/libuavcan/dsdl_compiler'
ENABLE_GCCDEPS = ['c', 'cxx']
ENABLE_HEADER_CHECKS = False
FLASH_RESERVE_START_KB = '16'
GIT = ['/usr/bin/git']
GIT_SUBMODULES = ['ChibiOS', 'mavlink']
HAL_WITH_UAVCAN = '1'
HAS_GTEST = False
HAVE_INTEL_HEX = False
HWDEF = '/home/calfan/ardupilot/libraries/AP_HAL_ChibiOS/hwdef/fmuv3/hwdef.dat'
IMPLIB_ST = '-Wl,--out-implib,%s'
INCLUDES = ['/home/calfan/ardupilot/libraries/', '/home/calfan/ardupilot/libraries/AP_Common/missing', '/home/calfan/ardupilot/modules/uavcan/libuavcan/include', '/home/calfan/ardupilot/modules/uavcan/libuavcan_drivers/stm32/driver/include']
LIB = ['gcc', 'm']
LIBDIR = '/usr/lib'
LIBPATH_ST = '-L%s'
LIB_ST = '-l%s'
LINKFLAGS = ['-mcpu=cortex-m4', '-Os', '-fomit-frame-pointer', '-falign-functions=16', '-ffunction-sections', '-fdata-sections', '-u_port_lock', '-u_port_unlock', '-u_exit', '-u_kill', '-u_getpid', '-u_errno', '-uchThdExit', '-u_printf_float', '-fno-common', '-nostartfiles', '-mfloat-abi=hard', '-mfpu=fpv4-sp-d16', '-mno-thumb-interwork', '-mthumb', '-L/home/calfan/ardupilot/build/fmuv3', '-L/home/calfan/ardupilot/modules/ChibiOS/os/common/startup/ARMCMx/compilers/GCC/ld', '-L/home/calfan/ardupilot/libraries/AP_HAL_ChibiOS/hwdef/common', '-Wl,--gc-sections,--no-warn-mismatch,--library-path=/ld,--script=ldscript.ld,--defsym=__process_stack_size__=0x400,--defsym=__main_stack_size__=0x400']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared', '-Wl,--enable-auto-image-base']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINKFLAGS_cxxshlib = ['-shared']
LINKFLAGS_cxxstlib = ['-Wl,-Bstatic']
LINK_CC = ['/cygdrive/c/Program Files (x86)/GNU Tools ARM Embedded/6 2017-q2-update/bin/arm-none-eabi-gcc']
LINK_CXX = ['/cygdrive/c/Program Files (x86)/GNU Tools ARM Embedded/6 2017-q2-update/bin/arm-none-eabi-g++']
MAKE = ['/usr/bin/make']
MAVGEN = '/home/calfan/ardupilot/modules/mavlink/pymavlink/tools/mavgen.py'
MAVLINK_DIR = '/home/calfan/ardupilot/modules/mavlink'
OBJCOPY = ['/cygdrive/c/Program Files (x86)/GNU Tools ARM Embedded/6 2017-q2-update/bin/arm-none-eabi-objcopy']
PREFIX = '/usr'
PT_DIR = '/home/calfan/ardupilot/Tools/ardupilotwaf/chibios/image'
PYC = 1
PYFLAGS = ''
PYFLAGS_OPT = '-O'
PYO = 1
PYTAG = 'cpython-36'
PYTHON = ['/usr/bin/python']
PYTHONARCHDIR = '/usr/lib/python3.6/site-packages'
PYTHONDIR = '/usr/lib/python3.6/site-packages'
PYTHON_VERSION = '3.6'
ROMFS_FILES = [('io_firmware.bin', 'Tools/IO_Firmware/fmuv2_IO.bin'), ('bootloader.bin', '/home/calfan/ardupilot/Tools/bootloaders/fmuv3_bl.bin')]
RPATH_ST = '-Wl,-rpath,%s'
RSYNC = ['/usr/bin/rsync']
SERIAL_PORT = '/home/calfan/ardupilot/dev/serial/by-id/*_STLink*'
SHLIB_MARKER = '-Wl,-Bdynamic'
SIZE = ['/cygdrive/c/Program Files (x86)/GNU Tools ARM Embedded/6 2017-q2-update/bin/arm-none-eabi-size']
SONAME_ST = '-Wl,-h,%s'
SRCROOT = '/home/calfan/ardupilot'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = '-Wl,-Bstatic'
STLIB_ST = '-l%s'
SUBMODULE_UPDATE = False
TOOLCHAIN = 'arm-none-eabi'
TOOLS_SCRIPTS = '/home/calfan/ardupilot/Tools/scripts'
UPLOAD_TOOLS = '/home/calfan/ardupilot/Tools/ardupilotwaf'
cfg_files = ['/home/calfan/ardupilot/build/fmuv3/ap_config.h']
cprogram_PATTERN = '%s.exe'
cshlib_PATTERN = 'cyg%s.dll'
cstlib_PATTERN = 'lib%s.a'
cxxprogram_PATTERN = '%s'
cxxshlib_PATTERN = 'lib%s.so'
cxxstlib_PATTERN = 'lib%s.a'
define_key = []
implib_PATTERN = 'lib%s.dll.a'
macbundle_PATTERN = '%s.bundle'