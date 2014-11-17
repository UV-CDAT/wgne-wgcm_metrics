from distutils.core import setup
import glob,subprocess

Version="0.6.0"
p = subprocess.Popen(("git","describe","--tags"),stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
try:
  descr = p.stdout.readlines()[0].strip()
  Version = "-".join(descr.split("-")[:-2])
except:
  Version = "0.9.pre-release"
  descr = Version

p = subprocess.Popen(("git","log","-n1","--pretty=short"),stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
try:
  commit = p.stdout.readlines()[0].split()[1]
except:
  commit = ""
f = open("src/python/version.py","w")
print >>f, "__version__ = '%s'" % Version
print >>f, "__git_tag_describe__ = '%s'" % descr
print >>f, "__git_sha1__ = '%s'" % commit
f.close()

portrait_files          = ["src/python/graphics/share/portraits.scr",]
cmip5_amip_json         = glob.glob("data/CMIP_metrics_results/CMIP5/amip/*.json")
cmip5_historical_json   = glob.glob("data/CMIP_metrics_results/CMIP5/historical/*.json")

setup (name         = "pcmdi_metrics",
       version      = descr,
       author       = "PCMDI",
       description  = "model metrics tools",
       url          = "http://github.com/PCMDI/pcmdi_metrics",
       packages     = ['pcmdi_metrics','pcmdi_metrics.io','pcmdi_metrics.pcmdi','pcmdi_metrics.graphics'],  
       package_dir  = {'pcmdi_metrics': 'src/python',
                       'pcmdi_metrics.io': 'src/python/io',
                       'pcmdi_metrics.pcmdi': 'src/python/pcmdi',
                       'pcmdi_metrics.graphics': 'src/python/graphics',
                       },
       scripts      = ["src/python/pcmdi/scripts/pcmdi_metrics_driver.py"],
       data_files   = [('share/pcmdi',('doc/obs_info_dictionary.json',)),
                       ('share/CMIP_metrics_results/CMIP5/amip',cmip5_amip_json),
                       ('share/CMIP_metrics_results/CMIP5/historical',cmip5_historical_json),
                       ('share/graphics/vcs',portrait_files),
                       ('doc',('doc/parameter_files/pcmdi_input_parameters_sample.py',)),
                       ]
       #include_dirs = [numpy.lib.utils.get_include()],
       #       ext_modules = [
       #    Extension('pcmdi_metrics.exts',
       #              ['src/C/add.c',],
       #              library_dirs = [],
       #              libraries = [],
       #              define_macros = [],
       #              extra_compile_args = [],
       #              extra_link_args = [],
       #              ),
       #    ]
      )

