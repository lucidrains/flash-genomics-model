from setuptools import setup, find_packages

setup(
  name = 'flash-genomics-model',
  packages = find_packages(exclude=[]),
  version = '0.0.1',
  license='MIT',
  description = 'Flash Genomics Model (FGM)',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/lucidrains/flash-genomics-model',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'transformers',
    'attention mechanism',
    'long context',
    'genomics',
    'pre-training'
  ],
  install_requires=[
    'einops>=0.6.1',
    'MEGABYTE-pytorch',
    'torch>=1.6',
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
