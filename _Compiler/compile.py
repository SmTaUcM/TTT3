# USAGE: from cmd.exe type 'python compile.py py2exe --includes sip'

# NOTE: C:\Python27\Lib\site-packages\PyQt4\uic\port_v3 must be deleted to allow Py2EXE to work.

# Copy Resource folder into dist folder.

from distutils.core import setup
import py2exe
import os

os.chdir("..")
ttt3Dir = os.path.abspath(os.curdir)

setup(
      zipfile = None, # Gets rid of library.zip.
      windows=
              [
               {
                "script": ttt3Dir + r"\TTT3.py",
                "icon_resources" : [(0, ttt3Dir + r"\_Resource\ttt3.ico")],
               }
              ],

    options=
             {
              "py2exe" : {
                          "optimize"     : 2,
##                          "ascii"        : 1, # Do Not use. Breaks TTT3
                          "packages"     : ["resource"], # Imports resource.py, must be in this files folder.
                          "includes"     : ["sip"],
                          "bundle_files" : 3, # 3 = don't bundle (default) 2 = bundle everything but the Python interpreter 1 = bundle everything, including the Python interpreter.
                          "compressed"   : 1,
                          "dll_excludes" : ['libgstreamer-1.0-0.dll',
                                            'CRYPT32.DLL',
                                            'DNSAPI.DLL',
                                            'IPHLPAPI.DLL',
                                            'MPR.dll',
                                            'MSIMG32.DLL',
                                            'MSWSOCK.dll',
                                            'NSI.dll',
                                            'PDH.DLL',
                                            'PSAPI.DLL',
                                            'POWRPROF.dll',
                                            'USP10.DLL',
                                            'WINNSI.DLL',
                                            'WTSAPI32.DLL',
                                            'api-ms-win-core-apiquery-l1-1-0.dll',
                                            'api-ms-win-core-crt-l1-1-0.dll',
                                            'api-ms-win-core-crt-l2-1-0.dll',
                                            'api-ms-win-core-debug-l1-1-1.dll',
                                            'api-ms-win-core-delayload-l1-1-1.dll',
                                            'api-ms-win-core-errorhandling-l1-1-0.dll',
                                            'api-ms-win-core-errorhandling-l1-1-1.dll',
                                            'api-ms-win-core-file-l1-1-0.dll',
                                            'api-ms-win-core-file-l1-2-1.dll',
                                            'api-ms-win-core-handle-l1-1-0.dll',
                                            'api-ms-win-core-heap-l1-1-0.dll',
                                            'api-ms-win-core-heap-l1-2-0.dll',
                                            'api-ms-win-core-heap-obsolete-l1-1-0.dll',
                                            'api-ms-win-core-io-l1-1-1.dll',
                                            'api-ms-win-core-kernel32-legacy-l1-1-0.dll',
                                            'api-ms-win-core-kernel32-legacy-l1-1-1.dll',
                                            'api-ms-win-core-libraryloader-l1-2-0.dll',
                                            'api-ms-win-core-libraryloader-l1-2-1.dll',
                                            'api-ms-win-core-localization-l1-2-1.dll',
                                            'api-ms-win-core-localization-obsolete-l1-2-0.dll',
                                            'api-ms-win-core-memory-l1-1-0.dll',
                                            'api-ms-win-core-memory-l1-1-2.dll',
                                            'api-ms-win-core-perfstm-l1-1-0.dll',
                                            'api-ms-win-core-processenvironment-l1-2-0.dll',
                                            'api-ms-win-core-processthreads-l1-1-0.dll',
                                            'api-ms-win-core-processthreads-l1-1-2.dll',
                                            'api-ms-win-core-profile-l1-1-0.dll',
                                            'api-ms-win-core-registry-l1-1-0.dll',
                                            'api-ms-win-core-registry-l2-1-0.dll',
                                            'api-ms-win-core-string-l1-1-0.dll',
                                            'api-ms-win-core-string-obsolete-l1-1-0.dll',
                                            'api-ms-win-core-synch-l1-1-0.dll',
                                            'api-ms-win-core-synch-l1-2-0.dll',
                                            'api-ms-win-core-sysinfo-l1-1-0.dll',
                                            'api-ms-win-core-sysinfo-l1-2-1.dll',
                                            'api-ms-win-core-threadpool-l1-2-0.dll',
                                            'api-ms-win-core-timezone-l1-1-0.dll',
                                            'api-ms-win-core-util-l1-1-0.dll',
                                            'api-ms-win-eventing-classicprovider-l1-1-0.dll',
                                            'api-ms-win-eventing-consumer-l1-1-0.dll',
                                            'api-ms-win-eventing-controller-l1-1-0.dll',
                                            'api-ms-win-eventlog-legacy-l1-1-0.dll',
                                            'api-ms-win-perf-legacy-l1-1-0.dll',
                                            'api-ms-win-security-base-l1-2-0.dll',
                                            'w9xpopen.exe',
                                        ],
                        }
             }
      )
