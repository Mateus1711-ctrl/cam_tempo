from setuptools import setup, find_packages

setup(
    name='Projeto Câmera',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'opencv-python',
    ],
    entry_points={
        'console_scripts': [
            'demo=demo:main',
        ],
    },
    author='João Delomo, Mateus Porto',
    author_email='delominho@gmail.com',
    description='Projeto Câmera',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Mateus1711-ctrl/cam_tempo?tab=readme-ov-file',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
