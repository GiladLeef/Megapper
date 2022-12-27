from setuptools import setup

if __name__ == '__main__':
    setup(
        name="Megapper",
        version='1.0.0',
        description="End-to-end image upscaling toolkit",
        long_description=open('README.md', encoding='utf-8').read(),
        long_description_content_type='text/markdown',
        url='https://github.com/giladleef/megapper',
        author='GiladLeef',
        author_email='giladleefbox@gmail.com',
        packages=['Megapper'],
        include_package_data=True,
        classifiers=[
            'Intended Audience :: Science/Research',
            'Programming Language :: Python :: 3 ',
        ],
        keywords='deep learning, super resolution',
        install_requires=[
            'numpy',
            'onnxruntime',
            'opencv-python',
            'shapely',
            'pyclipper',
            'pillow',
        ],
    )